# Databricks notebook source
display(dbutils.fs.mounts())

# COMMAND ----------

# dbutils.fs.unmount('/mnt/raw')
# dbutils.fs.unmount('/mnt/curated')
# dbutils.fs.unmount('/mnt/stage')

# COMMAND ----------

storage_account_name = "sparkdemosa"  
accountkey= "P5VzG8lPqENEfT8bfiiqNak6ByedW3zSSd+Gq4YLpw/5r2kc+3CiMtG9kegSdODfUeu5U1WjMnhw+AStqQ+A4w=="  
container_name = "raw"
fullname = "fs.azure.account.key." +storage_account_name+ ".blob.core.windows.net"


dbutils.fs.mount(  
  source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/{container_name}", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

dbutils.fs.mount(  
  source = f"wasbs://stage@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/stage", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

dbutils.fs.mount(  
  source = f"wasbs://curated@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/curated", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

display(dbutils.fs.ls("/mnt/raw"))

# COMMAND ----------


