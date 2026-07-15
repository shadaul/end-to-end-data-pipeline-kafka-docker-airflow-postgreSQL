import json
import psycopg2
from kafka import KafkaConsumer

conn = psycopg2.connect(dbname = 'airflow', user = 'airflow', host = 'localhost', password = 'airflow')

cursor = conn.cursor()
consumer = KafkaConsumer(
    'ztm_transport',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)