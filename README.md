# opcua-obd
OPC-UA facade for handling OBD readbacks.
* OPC-UA server and client using [FreeOpcUa/python-opcua](https://github.com/FreeOpcUa/python-opcua).
* HTML server using [Flask](http://flask.pocoo.org/).

## Usage
1. `python3 server-minimal.py &`
2. `FLASK_APP=flask-obd.py flask run`
3. Navigate to http://127.0.0.1:5000/
