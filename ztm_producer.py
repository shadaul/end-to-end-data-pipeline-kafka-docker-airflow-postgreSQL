import os
from dotenv import load_dotenv
import requests
import json
from kafka import Kafkaproducer

load_dotenv()

API_KEY = os.getenv('API_KEY')

producer = Kafkaproducer(
    bootstrap_servers = 'localhost:9092'
)

value_serializer=lambda v: json.dumps(v).encode('utf-8')

url = https://api.um.warszawa.pl/api/action/busestrams_get/