# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS  FORMULAONE.CURATED.WINNER_DETAILS(
# MAGIC name string,
# MAGIC circuit_name string,
# MAGIC date date
# MAGIC )
# MAGIC using DELTA
# MAGIC location 'abfss://curated@adls9867external.dfs.core.windows.net/winner_details'

# COMMAND ----------

drivers_df = spark.read.table('FORMULAONE.STAGE.DRIVERS')
results_df = spark.read.table('FORMULAONE.STAGE.RESULTS')
race_details_df = spark.read.table('FORMULAONE.CURATED.RACE_DETAILS')

# COMMAND ----------

results_winner_df = results_df.filter('rank == 1').select('driverId','raceId')

# COMMAND ----------

races_results_winner_df = results_winner_df\
.join(race_details_df, results_winner_df.raceId == race_details_df.RaceId,'left')\
    .select(results_winner_df.driverId, race_details_df.circuit_name, race_details_df.date)

# COMMAND ----------

final_df =races_results_winner_df\
.join(drivers_df, races_results_winner_df.driverId == drivers_df.driverId,'left')\
    .select(drivers_df.name, races_results_winner_df.circuit_name, races_results_winner_df.date)

# COMMAND ----------

final_df.write\
    .format('delta')\
    .mode('overwrite')\
    .saveAsTable('formulaone.curated.winner_details')

# COMMAND ----------



# COMMAND ----------


