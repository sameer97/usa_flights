# Databricks notebook source
import pandas as pd

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://airlinedata@airlineblobstorage.blob.core.windows.net",
  mount_point = "/mnt/airline",
  extra_configs = {"fs.azure.account.key.airlineblobstorage.blob.core.windows.net": "dlo+TU1/+jLaFoYJipB2M+hHKVdvctn+uf8RzjUKSafGh4n397hpmvunCJTbFOfMwnAXXxXxJQWL+AStl/0Baw=="})

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /dbfs/mnt/airline/
# MAGIC ls

# COMMAND ----------

# Importing packages
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType 
from pyspark.sql.types import ArrayType, DoubleType, BooleanType
from pyspark.sql.functions import col,array_contains

# COMMAND ----------

# Implementing CSV file in PySpark 

spark = SparkSession.builder.appName('PySpark Read CSV').getOrCreate()

# Reading csv file
dataframe = spark.read.options(header='True', delimiter=',').csv("/mnt/airline/airline.csv")
dataframe.printSchema()

# COMMAND ----------

len(dataframe.columns)
