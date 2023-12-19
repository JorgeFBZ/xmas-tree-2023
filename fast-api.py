from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from neopixel import Adafruit_NeoPixel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configuración de la tira LED
LED_COUNT = 16
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False

strip = Adafruit_NeoPixel(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS
)
strip.begin()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.post("/button")
def press_button():
    # Enciende todos los LEDs de color rojo
    for i in range(LED_COUNT):
        strip.setPixelColor(i, strip.Color(255, 0, 0))
    strip.show()

    return {"status": "success"}

@app.post("/set_color")
def set_color(color_led: str):
    # Convierte el color de cadena a un valor entero RGB
    color_int = int(color_led[1:], 16)  # Elimina el primer carácter '#'
    r = (color_int >> 16) & 255
    g = (color_int >> 8) & 255
    b = color_int & 255

    # Cambia el color de todos los LEDs
    for i in range(LED_COUNT):
        strip.setPixelColor(i, strip.Color(r, g, b))
    strip.show()

    return {"status": "success"}