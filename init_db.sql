DROP TABLE IF EXISTS buses;


CREATE TABLE buses (
    id UUID PRIMARY KEY,
    vehicle_number VARCHAR(50) UNIQUE NOT NULL, 
    line VARCHAR(20),
    latitude FLOAT,
    longitude FLOAT,
    bus_time VARCHAR(50), 
    updated_at TIMESTAMP WITH TIME ZONE
);