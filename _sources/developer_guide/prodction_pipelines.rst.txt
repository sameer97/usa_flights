.. _prodction_pipelines:

Production Pipelines
====================

.. _data_ingestion:

Data Ingestion
--------------

Data Ingestion is the process of obtaining huge amounts of data from various
sources and moving it to a location where it can be stored, processed, and analyzed.

Following data ingestion requirements have been met in this project:

#. Ingest all files into the data lake

#. Ingested data must have the schema applied

#. Ingested data must have audit columns

#. Ingested data must be stored in columnar format (i.e parquet format)

#. Must be able to analyze ingested data via SQL

#. Ingestion logic must be able to handle incremental load

.. _data_transformation:

Data Transformation
-------------------

Data Transformation is the process of transforming huge amounts of ingested data
so that it can used for analysis.

Following data transformation requirements have been met in this project:

#.  Join the key information required for reporting to create a new table

#. Join the key information required for analysis to create a new table

#. Transformed tables must have audit columns

#. Transformed data should be available for all workloads such as analysis, ML, SQL query

#. Transformed data must be stored in columnar format (i.e parquet format)

#. Transformation logic must be able to handle incremental load

.. _scheduling:

Scheduling
----------

Scheduling pipelines refers to the act of automating parts or all of a
data pipeline's components at fixed times, dates or intervals.


Following pipline scheduling requirements have been met in this project:

#. Schedule the pipelines to run every EOD

#. Ability to monitor the pipelines

#. Ability to re-run failed pipelines

#. Ability to set-up alerts on failures

