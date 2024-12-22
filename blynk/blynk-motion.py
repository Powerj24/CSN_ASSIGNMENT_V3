import BlynkLib
import time
from sense_hat import SenseHat
from door_motion import is_shaken
#define BLYNK_TEMPLATE_ID "TMPL4TmMpD0aa"
#define BLYNK_TEMPLATE_NAME "Assignment 2"
#define BLYNK_AUTH_TOKEN "rT87EeP-OeqD2BriZLKstl5lROsvZeTe"

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initialise Sense HAT
sense = SenseHat()
sense.clear(GREEN)  # Start with green color

# Blynk authentication token
BLYNK_AUTH = 'rT87EeP-OeqD2BriZLKstl5lROsvZeTe'
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)


if __name__ == "__main__":
    while True:
        blynk.run()
        if is_shaken():
            print("puppy on the move")
            blynk.log_event("motion_event") # motion event 
            sense.clear(RED)  # Set LEDs to red
            blynk.virtual_write(5, 1) #pin 5 for motion
            time.sleep(2)  # Keep red for 2 second
            sense.clear(GREEN)  # Reset back to green
            blynk.virtual_write(5, 0)

        # Short delay to prevent high CPU usage
        time.sleep(0.1)
