from sense_hat import SenseHat
import time

# Define colors
GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red
YELLOW = (255, 255, 0)  # RGB for yellow

# Initialize Sense HAT
sense = SenseHat()

# Define threshold for detecting door movement in or out
DOOR_THRESHOLD = 0  # Degrees (0 degree start for orientation)

# Start with yellow LEDs
sense.clear(YELLOW)  # Set LEDs to yellow

# Function to check if the Sense HAT has rotated
def detect_rotation():
    orientation = sense.get_orientation_degrees()
    pitch = orientation['pitch']
    print("pitch {0}".format(pitch))    
#parameters around the clock to indicate sensehat orientation for whether door closed open in or opn out 
    if (DOOR_THRESHOLD + 40) < pitch < (DOOR_THRESHOLD + 180):
        return "IN"
    elif (DOOR_THRESHOLD + 180) < pitch < (DOOR_THRESHOLD + 320):
        return "OUT"
    return "STAY"

while True:
    rotation = detect_rotation()  # Define tolerances here. Set rotation variable to check
    if rotation == "IN":
        print("Hello Puppy")
        sense.clear(GREEN)  # Set LEDs to green
        sense.show_message("Puppy IN", scroll_speed=0.05, text_colour=[0, 255, 0])
        time.sleep(10)  # Keep for 10 seconds 
        sense.clear(YELLOW)  # Reset back to yellow
    elif rotation == "OUT":
        print("Goodbye Puppy")
        sense.clear(RED)  # Set LEDs to red
        sense.show_message("Puppy OUT", scroll_speed=0.05, text_colour=[255, 0, 0])
        time.sleep(10)  # Keep for 10 seconds give sense a chance to calibrate
        sense.clear(YELLOW)  # Reset back to yellow
    else:
        print("Stay Puppy")
        sense.clear(YELLOW)
        sense.show_message("Stay Puppy", scroll_speed=0.05, text_colour=[255, 255, 0])
        time.sleep(10)  # Keep for 10 seconds give sense chance to calibrate
        sense.clear(YELLOW)  # Reset back to yellow
    
    # Short delay to reduce CPU usage
    time.sleep(0.1)
