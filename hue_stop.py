#!/usr/bin/python
from phue import Bridge

# BRIDGE INFORMATION
b = Bridge('192.168.178.13')
b.connect()

# TURN LAMPS OFF
b.set_light("V1 Lightstrip computer Noell", 'on', False)
b.set_light("V1 Plug Computer Noell", 'on', False)

# EXIT SCRIPT
exit()