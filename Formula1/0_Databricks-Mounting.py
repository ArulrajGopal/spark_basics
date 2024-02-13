# Databricks notebook source
storage_account_name = "teststorageaccount23423"  
accountkey= "vWM4wogy4NzlOJ+1Lbci2OT/Bza2n1Lv8XC7+XvfFUiNsN1LEb0AobHKKA+y5b4jkQ9GlIYXPGCz+AStdKJtng=="  
container_name = "input"
fullname = "fs.azure.account.key." +storage_account_name+ ".blob.core.windows.net"


dbutils.fs.mount(  
  source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/{container_name}", 
  extra_configs = {fullname : accountkey}) 
