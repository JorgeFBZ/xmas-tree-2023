import time
from rpi_ws281x import PixelStrip, Color

def set_color(strip,color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
