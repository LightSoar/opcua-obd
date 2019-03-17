#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from opcua import Client
import obd
from configparser import ConfigParser

app = Flask(__name__)

client = Client("opc.tcp://localhost:4840/opcua-obd/")
client.connect()

root = client.get_root_node()

config = ConfigParser()
config.read('pids.conf')

opc_vars = {}
for route in config['Routes'].keys():
    pid = config['Routes'][route] # "SPEED", "RPM", etc.
    if obd.commands.has_name(pid):
        #speed = root.get_child(["0:Objects", "2:MyCar", "2:SPEED"])
        #rpm = root.get_child(["0:Objects", "2:MyCar", "2:RPM"])
        opc_vars[route] = root.get_child(["0:Objects", "2:MyCar", "2:%s" % pid])

        #app.add_url_rule('/%s/' % endpoint, view_func=opc_vars[endpoint].get_value)
        view_func = lambda: str(opc_vars[route].get_value())
        app.add_url_rule('/%s/' % route, route, view_func)


# @app.route("/speed/")
# def getSpeed():
#     return str(speed.get_value())
#
# @app.route("/rpm/")
# def getRPM():
#     return str(rpm.get_value())

@app.route("/")
def index():
    return render_template('index.html')
