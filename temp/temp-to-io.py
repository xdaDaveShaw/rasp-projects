#!/usr/bin/env python3

# import standard python modules.
import time
import os
from datetime import datetime

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

READ_TIMEOUT = 60  #Seconds 

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

            output = '{0} - {1:.2f} C,  {2:.2f} hPa,  {3:.3f} %RH'.format(
                datetime.now(),
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity)

#          output = str(datetime.now()) + output

            temperature = '%.2f'%(sensor.data.temperature)
            humidity = '%.2f'%(sensor.data.humidity)
            pressure = '%.2f'%(sensor.data.pressure)
            try:
                aio.send(temperature_feed.key, str(temperature))
                aio.send(humidity_feed.key, str(humidity))
                aio.send(pressure_feed.key, str(pressure))
            except Exception as e:
                print ('Exception Occurred, details to follow')
                print (e)

            print(output)
        else:
            print('Failed to get Reading, trying again in ', READ_TIMEOUT, 'seconds')
        
        # Timeout to avoid flooding Adafruit IO
        time.sleep(READ_TIMEOUT)

except KeyboardInterrupt:
    pass

