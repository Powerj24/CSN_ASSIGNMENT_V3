import BlynkLib
from time import sleep
from sense_hat import SenseHat
#from capture_image import capture_image #grey out til further need 
#from upload_image import upload_image
#define BLYNK_TEMPLATE_ID "TMPL4TmMpD0aa"
#define BLYNK_TEMPLATE_NAME "Assignment 2"
#define BLYNK_AUTH_TOKEN "rT87EeP-OeqD2BriZLKstl5lROsvZeTe"

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 'rT87EeP-OeqD2BriZLKstl5lROsvZeTe'
IMAGE_PATH="./images/sensehat_image.jpg"
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register handler for virtual pin V1 write event
@blynk.on("V1")
def handle_v1_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')
    
    if button_value=="1":
        sense.clear(255,255,255)
      #  capture_image(IMAGE_PATH) grey out till further use 
      #  result = upload_image(IMAGE_PATH)
        
      #  blynk.set_property(3,"urls",result) #updates ulrs property of widget attached to Datastream2(virtual pin V3)
    else:
        sense.clear()

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            #blynk.virtual_write(0, round(sense.temperature,2))
            sleep(2)  # Add a short delay to avoid high CPU usage
    except KeyboardInterrupt:
        print("Blynk application stopped.")