# Databricks notebook source
# MAGIC %run ./1_Functions

# COMMAND ----------

races_df = read_file('races.csv', 'csv', 'raw')

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

final_df = data_type_convert(races_df, races_schema)

# COMMAND ----------

final_df.write\
    .format('delta')\
    .mode('overwrite')\
    .option("path","abfss://stage@adls9867external.dfs.core.windows.net/races")\
    .saveAsTable('formulaone.stage.races')
