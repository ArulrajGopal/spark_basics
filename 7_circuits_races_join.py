# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS  FORMULAONE.CURATED.RACE_DETAILS(
# MAGIC RaceId int,
# MAGIC circuit_name string,
# MAGIC date date
# MAGIC )
# MAGIC using DELTA
# MAGIC location 'abfss://curated@adls9867external.dfs.core.windows.net/race_details'

# COMMAND ----------

races_df = spark.read.table('FORMULAONE.STAGE.RACES')
circuits_df = spark.read.table('FORMULAONE.STAGE.CIRCUITS')

# COMMAND ----------

final_df = races_df\
    .join(circuits_df, races_df.circuitId == circuits_df.circuitId,'left')\
    .select(races_df.raceId, races_df.date, circuits_df.name)\
    .withColumnRenamed('name','circuit_name')

# COMMAND ----------

final_df.write\
    .format('delta')\
    .mode('overwrite')\
    .saveAsTable('formulaone.curated.race_details')

# COMMAND ----------


