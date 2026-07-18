import json
import psycopg2
from kafka import KafkaConsumer
from dotenv import load_dotenv
import os


load_dotenv()
conn = psycopg2.connect(dbname = os.getenv('DB_NAME'), user = os.getenv('DB_USER'), host = os.getenv('DB_HOST'), password = os.getenv('DB_PASSWORD'))
cursor = conn.cursor()
consumer = KafkaConsumer(
    'ztm_transport',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print("receiving data")
    data = message.value
    lines = data.get('Lines')
    lon = data.get('Lon')
    VehicleNumber = data.get('VehicleNumber')
    Time = data.get('Time')
    Lat = data.get('Lat')
    Brigade = data.get('Brigade')
    print(data)

    insert_query = """
        INSERT INTO buses (vehicle_number, line, latitude, longitude, bus_time)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (VehicleNumber, lines, Lat, lon, Time))

    conn.commit()