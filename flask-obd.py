#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from opcua import Client
import obd

#connection = obd.OBD()

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

@app.route('/<int:mode>/<int:pid>/')
@app.route('/mode/<int:mode>/pid/<int:pid>/')
def by_pid(mode, pid):
    if not obd.commands.has_pid(mode, pid):
        return "Not a valid mode/pid"

    return str(connection.query(obd.commands[mode][pid]).value)

@app.route('/name/<string:name>/')
def by_name(name):
    if not isinstance(name, str):
        return "Not a valid parameter name"

    name = name.upper()
    if not obd.commands.has_name(name):
        return "Not a valid parameter name"

    return str(connection.query(obd.commands[name.upper()]).value)


@app.route('/eff/')
def ff():
    # connection.query returns an instance of obd.OBDResponse, if connected.
    speed = connection.query(obd.commands.SPEED)
    fuelRate = connection.query(obd.commands.FUEL_RATE)

    if speed.is_null() or fuelRate.is_null():
        return "Error reading speed and/or fuel rate"
    else:
        return str(speed.value/fuelRate.value)
