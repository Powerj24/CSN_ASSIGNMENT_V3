from sense_hat import SenseHat
import time

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initialise Sense HAT
sense = SenseHat()
sense.clear(GREEN)  # Start with green color

# Define threshold for door swing detection
SWING_THRESHOLD = .5  # more sensitive works better

def is_shaken():
    # Get raw accelerometer data
    swing=False
    accel = sense.get_accelerometer_raw()
    x = abs(accel['x'])
    y = abs(accel['y'])#dont need this axis for now
    z = abs(accel['z'])# same
    
    if x > SWING_THRESHOLD :
        swing=True
    # Check if the acceleration exceeds the shake threshold on any axis
    return swing

if __name__ == "__main__":
    while True:
        if is_shaken():
            print("Hello puppy")
            sense.clear(RED)  # Set LEDs to red
            time.sleep(2)  # Keep red for 2 seconds
            sense.clear(GREEN)  # Reset back to green

        # Short delay to prevent high CPU usage
        time.sleep(0.1)
