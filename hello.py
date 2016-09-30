from flask import Flask, render_template, redirect
from gpiozero import *

app = Flask(__name__)

led = LED(14)


@app.route("/")
def index():
    # print led.is_lit
    return render_template('index.jinja', status=str(led.is_lit))


@app.route("/on")
def switch_on():
    try:
        led.on()
        return redirect("/")
    except GPIOZeroError:
        return "A GPIO Zero error has occurred. Check the pin/connection."


@app.route("/off")
def switch_off():
    try:
        led.off()
        return redirect("/")
    except GPIOZeroError:
        return "A GPIO Zero error has occurred. Check the pin/connection."


@app.route("/areyousure")
def are_you_sure():
    return render_template('index.jinja', status=str(led.is_lit),
                           areyousure=str(True))


if __name__ == "__main__":
    app.run()
