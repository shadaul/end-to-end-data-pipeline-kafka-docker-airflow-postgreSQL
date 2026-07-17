import json
import psycopg2
from kafka import KafkaConsumer



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
        INSERT INTO bus_data (vehicle_number, line, latitude, longitude, bus_time)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (VehicleNumber, lines, Lat, lon, Time))

    conn.commit()