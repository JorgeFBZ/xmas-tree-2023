from flask import Flask, render_template
from flask import request
from led_control import set_color
import threading

STRIP_1 = 24          # Length first led strip
STRIP_2 = 35          # Length second led strip

LED_COUNT = STRIP_1 + STRIP_2   # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def hex_to_rgb(hex):
  hex = hex.lstrip('#')
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('main.html')

@app.route('/color', methods=['POST'])
def color():
    if request.method == 'POST':
        color = request.form['color_led']
        print(hex_to_rgb(color))
        set_color(hex_to_rgb(color))
        return render_template('main.html')