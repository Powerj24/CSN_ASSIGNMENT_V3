from sense_hat import SenseHat

def get_device_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    orientation = sense.get_orientation_degrees()
    pitch = orientation["pitch"]
        
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp, 2),
        "pitch": round(pitch,2)
    }
    
    return data

# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice1"
    device_data = get_device_data(deviceID)
    # Print the data in JSON format for testing
    print(device_data)
    
