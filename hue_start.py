#!/usr/bin/python
from phue import Bridge
import json

# BRIDGE INFORMATION
b = Bridge('192.168.178.13')
b.connect()

# GET LIST OF ALL ASSOCIATED LAMPS
print(json.dumps(b.get_api(), indent=4))

# TURN LAMPS ON (source: https://github.com/studioimaginaire/phue)
command =  {'transitiontime' : 300, 'on' : True, 'bri' : 170, 'hue' : 8200}
b.set_light("V1 Lightstrip computer Noell", command)
b.set_light("V1 Plug Computer Noell",'on', True)

# EXIT SCRIPT
exit()