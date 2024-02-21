# Databricks notebook source
# MAGIC %run ./1_common

# COMMAND ----------

races_df = read_file('races.csv', 'csv')

# COMMAND ----------

races_schema = {
'raceId': 'INT',
 'year':'INT',
 'round':'INT',
 'circuitId':'INT',
 'name':'string',
 'date':'date',
'time':'string',
'url':'string'
}

# COMMAND ----------

final_df = data_type_convert(races_df, races_schema)\
    .withColumn("loaded_time", current_timestamp())\
    .drop("url")

# COMMAND ----------

final_df.write\
    .format('csv')\
    .mode('overwrite')\
    .option("path","/mnt/stage/races")\
    .saveAsTable('stage.races')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from stage.races

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended stage.races

# COMMAND ----------


