# Databricks notebook source
# MAGIC %run ./1_common

# COMMAND ----------

results_df = read_file('results.json', 'json')

# COMMAND ----------

results_schema = {'constructorId': 'INT', 
                  'driverId': 'INT', 
                  'fastestLap': 'INT', 
                  'fastestLapSpeed': 'double', 
                  'fastestLapTime': 'double',
                  'grid': 'INT',
                   'laps': 'INT', 
                   'milliseconds': 'INT', 
                   'number': 'INT', 
                   'points': 'INT',
                   'position': 'INT',
                    'positionOrder': 'INT',
                    'positionText': 'INT',
                    'raceId': 'INT',
                    'rank': 'INT',
                    'resultId': 'INT',
                    'statusId': 'INT',
                    'time': 'string'}

# COMMAND ----------

final_df = data_type_convert(results_df, results_schema)

# COMMAND ----------

final_df.write\
    .format('csv')\
    .mode('overwrite')\
    .option("path","/mnt/stage/results")\
    .saveAsTable('stage.results')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from stage.results

# COMMAND ----------


