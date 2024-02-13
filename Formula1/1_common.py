# Databricks notebook source
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

def read_file(file_name, format):
    df = spark.read\
    .format(f"{format}")\
    .option('Header',True)\
    .load(f'/mnt/raw/{file_name}')
    return df

# COMMAND ----------

def data_type_convert(df, schema):
    lst = []
    for column,type in schema.items():
        lst.append(f"cast({column} as {type}) {column}")
    changed_df = df.selectExpr(lst)
    return changed_df
