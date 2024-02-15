# Databricks notebook source
# MAGIC %run ./1_common

# COMMAND ----------

circuits_df = read_file('circuits.csv', 'csv')\
    .drop('url')

# COMMAND ----------

circuits_schema = {
'circuitId': 'INT',
 'circuitRef':'STRING',
 'name':'STRING',
 'location':'STRING',
 'country':'STRING',
 'lat':'Double',
 'lng':'Double',
 'alt':'int'
}

# COMMAND ----------

final_df = data_type_convert(circuits_df, circuits_schema)\
    .withColumn("loaded_time", current_timestamp())

# COMMAND ----------

final_df.printSchema()

# COMMAND ----------

final_df.display()

# COMMAND ----------

final_df.display()

# COMMAND ----------

final_df.write\
    .format('parquet')\
    .mode('overwrite')\
    .save('/mnt/stage/circuits')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from  stage.circuits

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended stage.circuits
