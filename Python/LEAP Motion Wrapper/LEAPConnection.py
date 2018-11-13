import websocket
import json
import threading
import pprint

pp = pprint.PrettyPrinter(indent=4)

websocket.enableTrace(True)
connection = websocket.WebSocket()
connection.connect("ws://127.0.0.1:6437")

pp.pprint(connection.recv())
pp.pprint(connection.recv())
pp.pprint(connection.recv())
pp.pprint(connection.recv())
pp.pprint(connection.recv())
pp.pprint(connection.recv())
pp.pprint(connection.recv())

{"currentFrameRate":55.578007,
"devices":[],
"hands":[
    {"direction":[0.413047,-0.060077,-0.908726],
    "id":106,
    "palmNormal":[-0.011536,-0.998087,0.060741],
    "palmPosition":[-10.702514,158.328674,43.268402],
    "palmVelocity":[20.016623,12.100307,-28.980669],
    "timeVisible":0.555039}],
"id":173632,
"timestamp":370158218976}
