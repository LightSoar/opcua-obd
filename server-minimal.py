import sys
import time

from opcua import ua, Server
import obd

from configparser import ConfigParser

if __name__ == "__main__":

    config = ConfigParser()
    config.read('pids.conf')

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840/opcua-obd/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://github.com/lightsoar"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyCar")

    opc_vars = {}
    for route in config['Routes'].keys():
        pid = config['Routes'][route] # "SPEED", "RPM", etc.
        if obd.commands.has_name(pid):
            opc_vars[obd.commands[pid]] = myobj.add_variable(idx, pid, 0)
    #speed = myobj.add_variable(idx, "SPEED", 0)
    #rpm = myobj.add_variable(idx, "RPM", 0)
    #intake_pressure = myobj.add_variable(idx, "INTAKE_PRESSURE", 0)
    #maf = myobj.add_variable(idx, "MAF", 0)
    #cer = myobj.add_variable(idx, "COMMANDED_EQUIV_RATIO", 0)

    # starting!
    server.start()
    obdConn = obd.OBD()

    obdSpeed = 0
    obdRPM = 0
    try:
        while True:
            time.sleep(1)
            if not(obdConn.is_connected()):
                obdConn.close()
                obdConn = obd.OBD()

            #print("==>", obdConn.query(obd.commands.SPEED).value.magnitude)
            if obdConn.is_connected():
                for obd_command in opc_vars:
                    value = obdConn.query(obd_command).value.magnitude
                    opc_vars[obd_command].set_value(value)

    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
        obdConn.close()
