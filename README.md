# opcua-obd
OPC-UA facade for handling OBD readbacks.
* OPC-UA server and client using [FreeOpcUa/python-opcua](https://github.com/FreeOpcUa/python-opcua).
* HTML server using [Flask](http://flask.pocoo.org/).

## Usage
1. Update the PID list in `pids.conf`
1. Run the OPC-UA server with `python3 opcua-server.py &`
1. Run the HTML server with `FLASK_APP=html-server.py flask run`
1. Navigate to http://127.0.0.1:5000/ for the live dashboard and to http://127.0.0.1:5000/rpm for the RPM, etc.
