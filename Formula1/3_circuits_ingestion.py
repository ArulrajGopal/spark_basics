# Databricks notebook source
# MAGIC %run ./1_Functions

# COMMAND ----------

circuits_df = read_file('circuits.csv', 'csv', 'raw')

# COMMAND ----------

circuits_schema = {
'circuitId': 'INT',
 'circuitRef':'STRING',
 'name':'STRING',
 'location':'STRING',
 'country':'STRING',
 'lat':'Double',
 'lng':'Double',
 'alt':'int',
 'url':'STRING'
}

# COMMAND ----------

final_df = data_type_convert(circuits_df, circuits_schema)

# COMMAND ----------

final_df.write\
    .format('delta')\
    .mode('overwrite')\
    .option("path","abfss://stage@adls9867external.dfs.core.windows.net/circuits")\
    .saveAsTable('formulaone.stage.circuits')

# COMMAND ----------


