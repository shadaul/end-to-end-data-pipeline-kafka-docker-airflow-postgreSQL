import json
import psycopg2
from kafka import KafkaConsumer

conn = psycopg2.connect(dbname = 'airflow', user = 'airflow', host = 'localhost', password = 'airflow')

