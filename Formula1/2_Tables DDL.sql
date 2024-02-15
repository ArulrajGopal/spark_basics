-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS stage

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS curated

-- COMMAND ----------

DROP TABLE IF EXISTS stage.circuits;

CREATE TABLE stage.circuits(
  circuit_id INT,
  circuitref STRING,
  name STRING,
  location STRING,
  country STRING,
  lat Double,
  lng Double,
  alt int,
  loaded_time timestamp
)
using csv
location '/mnt/stage/circuits'

-- COMMAND ----------

DROP TABLE IF EXISTS stage.races;

CREATE TABLE stage.races(
  raceId INT,
  year INT,
  round INT,
  circuitId INT,
  name STRING,
  date date,
  time string,
  loaded_time timestamp
)
using csv
location '/mnt/stage/races'

-- COMMAND ----------


