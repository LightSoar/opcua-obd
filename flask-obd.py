#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from opcua import Client

app = Flask(__name__)

client = Client("opc.tcp://localhost:4840/opcua-obd/")
client.connect()
root = client.get_root_node()
speed = root.get_child(["0:Objects", "2:MyCar", "2:SPEED"])
rpm = root.get_child(["0:Objects", "2:MyCar", "2:RPM"])

@app.route("/speed/")
def getSpeed():
    return str(speed.get_value())

@app.route("/rpm/")
def getRPM():
    return str(rpm.get_value())

@app.route("/")
def index():
    return render_template('index.html')
