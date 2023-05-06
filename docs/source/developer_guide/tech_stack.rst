.. _tech_stack:

Tech Stack
==========

Following are the major technologies or tools used in this project:

.. _databricks:

Azure Databricks
----------------

Databricks is a company created by the founders of Apache Spark,
to make it easier to work with Spark by providing the necessary management layers.
Microsoft makes, the Databricks service available on its Azure Cloud platform as a first party service.
These three offerings together makes Azure Databricks. Azure Databricks leverages, Azure security and
seamlessly integrates with Azure Active Directory and single sign on.
It provides seamless integration and high speed connectors between various Azure data services.

Databricks adds necessary layers on top of apache spark to make it easy for us to use the spark capabilities.

More on it at `azure databricks documentation <https://learn.microsoft.com/en-us/azure/databricks/>`_

.. _azure:

Azure Data Lake Service
-----------------------

Azure Data Lake Service or ADLS is a scalable data storage and analytics service hosted in Azure.
More on it at `ADLS documentation <https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction>`_

.. _pyspark:

PySpark
-------

Apache Spark is a unified analytics engine for big data processing. Its faster that Hadoop because of its in-memory processing and other optimizations.

High level Spark Architecture Components:

#. Spark Core: Contains basic functionalities like scheduling tasks, memory management, fault recovery. Home to sparks abstraction API Resilient Distributed Dataset (RDD)

#. Spark SQL Engine: Converts a query to highly efficient execution plan and takes care of CPU efficiency

#. Higher level API's like Spark SQL, DataFrame, Spark streaming, etc.

#. Spark comes with Standalone resource manager, but we can choose others like YARN, Kubernetes, etc

PySpark is a python API for spark.

More on it at `PySpark documentation <https://hyukjin-spark.readthedocs.io/en/latest/>`_

.. _sql:

SQL
---

Structured Query Language or SQL is a domain-specific language used in programming and designed
for managing data held in a relational database management system, or for stream processing
in a relational data stream management system

More on it at `azure sql documentation <https://learn.microsoft.com/en-us/azure/azure-sql/database/?view=azuresql>`_
