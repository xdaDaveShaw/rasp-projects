#!/usr/bin/env python3

# import standard python modules.
import time
import os

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# import BME860 client
import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)

API_USERNAME = "xdaDaveShaw"
API_KEY = os.environ['AOI_KEY']

READ_TIMEOUT = 15

# Create an instance of the REST client.
aio = Client(API_USERNAME, API_KEY)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('bme680.temperature')
humidity_feed = aio.feeds('bme680.humidity')
pressure_feed = aio.feeds('bme680.pressure')

print('Polling:')
try:
    while True:
        if sensor.get_sensor_data():

            output = '{0:.2f} C,  {1:.2f} hPa,  {2:.3f} %RH'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity)

            temperature = '%.2f'%(sensor.data.temperature)
            humidity = '%.2f'%(sensor.data.humidity)
            pressure = '%.2f'%(sensor.data.pressure)
            
            aio.send(temperature_feed.key, str(temperature))
            aio.send(humidity_feed.key, str(humidity))
            aio.send(pressure_feed.key, str(pressure))

            print(output)
        else:
            print('Failed to get Reading, trying again in ', READ_TIMEOUT, 'seconds')
        
        # Timeout to avoid flooding Adafruit IO
        time.sleep(READ_TIMEOUT)

except KeyboardInterrupt:
    pass

# while True:
#     humidity = 45.2
#     temperature = 16.8
#     if humidity is not None and temperature is not None:
#         print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
#         # Send humidity and temperature feeds to Adafruit IO
#         temperature = '%.2f'%(temperature)
#         humidity = '%.2f'%(humidity)
#         aio.send(temperature_feed.key, str(temperature))
#         aio.send(humidity_feed.key, str(humidity))
#     else:
#         print('Failed to get Reading, trying again in ', READ_TIMEOUT, 'seconds')
#     # Timeout to avoid flooding Adafruit IO
#     time.sleep(READ_TIMEOUT)
