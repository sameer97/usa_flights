import fsspec
import yaml

from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable

def load_yml(path):
    """Load a yml file from the input `path`.

    Parameters
    ----------
    path : string
        Absolute or relative filepath

    Returns
    -------
    dict
        dictionery of the loaded yml file
    """
    fs = fsspec.filesystem("file")
    with fs.open(path, mode="r") as fp:
        return yaml.safe_load(fp)

def add_ingestion_date(input_df):
    output_df = input_df.withColumn("ingestion_date", current_timestamp())
    return output_df

def re_arrange_partition_column(df, partition_column):
    column_list = [column for column in df.schema.names if column != partition_column]
    column_list.append(partition_column)
    
    return df.select(column_list)

def overwrite_partition(df, db_name, table_name, partition_column):
    # partition column needs to be the last column for dynamic overwrite to work
    output_df = re_arrange_partition_column(df, partition_column)
    
    # set partition overwrite conf parameter to dynamic
    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
    
    if (spark.jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
        output_df.write.mode("overwrite").insertInto(f"{db_name}.{table_name}")
    else:
        (output_df.
         write.mode("overwrite").
         partitionBy(partition_column).
         format("parquet").
         saveAsTable(f"{db_name}.{table_name}")
        )

def overwrite_partition_delta(df, folder_path, merge_cond, db_name, table_name, partition_column):
    if (spark.jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
        deltaTable = DeltaTable.forPath(spark, folder_path)
        (deltaTable.alias("dlt").merge(
            df.alias("src"),
            merge_cond).
         whenMatchedUpdateAll().
         whenNotMatchedInsertAll().
         execute()
        )
    else:
        (df.
         write.mode("overwrite").
         partitionBy(partition_column).
         format("delta").
         saveAsTable(f"{db_name}.{table_name}")
        )
