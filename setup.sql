CREATE DATABASE local_climate_detail;
CREATE USER 'sensor_admin'@'localhost' IDENTIFIED BY 'aq12ws';
GRANT ALL PRIVILEGES ON local_climate_detail.* To 'sensor_admin'@'localhost';
FLUSH PRIVILEGES;