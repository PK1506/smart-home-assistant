CREATE TABLE appliances (
    id SERIAL PRIMARY KEY,
    appliance_name VARCHAR(255) NOT NULL,
    power_usage FLOAT NOT NULL,
    temperature FLOAT NOT NULL,
    days_since_last_service INT NOT NULL
);
