import BlynkLib
from time import sleep
from sense_hat import SenseHat 
sense = SenseHat()
sense.clear()

#define BLYNK_TEMPLATE_ID "TMPL4TmMpD0aa"
#define BLYNK_TEMPLATE_NAME "Assignment 2"
#define BLYNK_AUTH_TOKEN "rT87EeP-OeqD2BriZLKstl5lROsvZeTe"

# Blynk authentication token
BLYNK_AUTH = 'rT87EeP-OeqD2BriZLKstl5lROsvZeTe'

# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register handler for virtual pin V1 write event
@blynk.on("V1")
def handle_v1_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')
    if button_value=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            orientation = sense.get_orientation_degrees()
            pitch = orientation["pitch"]
            blynk.virtual_write(2, pitch) #pin 2
            #print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
            print("pitch {0}".format(pitch)) #isolate the pitch
            sleep(5)  # Add a short delay to avoid high CPU usage
    except KeyboardInterrupt:
        print("Blynk application stopped.")