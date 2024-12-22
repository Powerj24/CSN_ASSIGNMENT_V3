from sense_hat import SenseHat
import requests
import time

sense = SenseHat()

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "6V7DCY9P3H50ZDDY"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature, pitch):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': pitch
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


while True:
    # Read temperature and orientation from Sense HAT
    temperature = round(sense.get_temperature(),2),
    orientation = sense.get_orientation_degrees()#
    pitch = orientation["pitch"]#select for pitch
    print(f"Temperature: {temperature} C")
    print(f"pitch: {pitch} degrees")

    # Send the data to ThingSpeak
    send_to_thingspeak(temperature, pitch)

    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(15)
