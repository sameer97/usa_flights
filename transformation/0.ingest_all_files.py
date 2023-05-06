# Databricks notebook source
file_date = "2008-01-01"

# COMMAND ----------

search_flight_status = dbutils.notebook.run(
    "1.search_flight",
    0,
    {"file_date": file_date}
)

# COMMAND ----------

if search_flight_status == "Success":
    print("Search Flight Data Updated")
    airline_standings_status = dbutils.notebook.run(
        "2.airline_standings",
        0
    )
else:
    print("Search Flight Data Update Failed")

# COMMAND ----------

if airline_standings_status == "Success":
    print("Airline Standings Updated")
else:
    print("Airline Standings Update Failed")
