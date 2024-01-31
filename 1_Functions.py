# Databricks notebook source
def read_file(file_name, format, container_name):
    df = spark.read\
    .format(f"{format}")\
    .option('Header',True)\
    .load(f'abfss://{container_name}@adls9867external.dfs.core.windows.net/{file_name}')
    return df

# COMMAND ----------

def data_type_convert(df, schema):
    lst = []
    for column,type in schema.items():
        lst.append(f"cast({column} as {type}) {column}")
    changed_df = df.selectExpr(lst)
    return changed_df

# COMMAND ----------


