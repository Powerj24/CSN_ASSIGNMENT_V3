#!/usr/bin/python3

from flask import Flask, request
from flask_cors import CORS
from sense_hat import SenseHat
from flask import Flask, request, render_template

sense = SenseHat()
deviceID="device1"
#clear sensehat and intialise light_state
sense.clear()

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    msg = {"deviceID": deviceID,"temp":temperature}
    return str(msg)+"\n"

@app.route('/sensehat/orientation',methods=['GET'])
def current_orientation():
    orientation=sense.get_orientation_degrees()
    pitch=orientation["pitch"]
    msg = {"deviceID": deviceID,"pitch":pitch}
    return str(msg)+"\n"


@app.route('/sensehat/light',methods=['GET'])
def light_get():
    #check top left pixel value(==0 - off, >0 - on) 
    print(sense.get_pixel(0, 0)) 
    if sense.get_pixel(0, 0)[0] == 0:
        return '{"state":"off"}'
    else:
        return '{"state":"on"}'

@app.route('/sensehat/light',methods=['POST'])
def light_post():
    state=request.args.get('state')
    print (state)
    if (state=="on"):
        sense.clear(255,255,255)
        return '{"state":"on"}'
    else: 
        sense.clear(0,0,0)
        return '{"state":"off"}'
    
@app.route('/') 
def index():
    celcius = round(sense.temperature, 2)
    fahrenheit = round(1.8 * celcius + 32, 2)
    pitch = round(sense.orientation["pitch"],2)
    return render_template('status.html', celcius=celcius, fahrenheit=fahrenheit, pitch=pitch)


#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)

#opens ok as 192.168.1.23:5000/sensehat/environment