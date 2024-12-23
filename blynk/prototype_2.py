import BlynkLib
import time
from time import sleep
from sense_hat import SenseHat
from capture_image import capture_image
from upload_image import upload_image
from door_motion import is_shaken

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red
BLUE = (0, 0, 255)   # blue
YELLOW = (255, 255, 0) # yellow

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
        capture_image(IMAGE_PATH)
        result = upload_image(IMAGE_PATH)
        
        blynk.set_property(3,"urls",result) #updates ulrs property of widget attached to Datastream2(virtual pin V3)
    else:
        sense.clear()

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            temp = sense.get_temperature()
            if temp <= 24: #temp number sensitivty has to be allowed for 
                print("COLD")
                sense.clear(BLUE)
                blynk.log_event("temp_drop") # log temp drop NEEDS INDENTATATION TO WORK
            #print(temp)
            blynk.virtual_write(0, temp) #pin 0 for temp  
            print("temp:{}".format(round(temp,2)))
            orientation = sense.get_orientation_degrees()
            pitch = orientation["pitch"]
            if pitch > 10 and pitch <350:# pitch number sensitivty has to be allowed for 
                print("door open")
                sense.clear(YELLOW)
                blynk.log_event("door_open") # simplified from original concept
            blynk.virtual_write(2, pitch) #pin 2
            #print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
            print("pitch: {0}".format(round(pitch,2))) #isolate the pitch                
            sleep(5)# Add a short delay to avoid high CPU usage
            if is_shaken():
                print("puppy on the move")
                blynk.log_event("motion_event") # motion event 
                sense.clear(RED)  # Set LEDs to red
                blynk.virtual_write(5, 1) #pin 5 for motion
                time.sleep(5)  # Keep red for 2 second
                sense.clear(GREEN)  # Reset back to green
                blynk.virtual_write(5, 0)
    except KeyboardInterrupt:
        print("Blynk application stopped.")
