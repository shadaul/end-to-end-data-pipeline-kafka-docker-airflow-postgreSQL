CREATE TABLE IF NOT EXISTS buses (
    vehicle_number TEXT,
    line TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    bus_time TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);