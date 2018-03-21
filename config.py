# load config file

import json
import sys

__configFilename = "config.json"
__stateFilename = "state.json"
__configJson = None
__stateJson = None
__stateDefault = { "lastcheck": "1514000000" }

def get():
    try:
        global __configJson
        if __configJson != None:
            return __configJson
        json_data = open(__configFilename)
        __configJson = json.load(json_data)
        #print(__configJson)
        print("Config read from", __configFilename)
        return __configJson
    except:
        print("ERROR: could not load config from", __configFilename, sys.exc_info()[0])
        sys.exit()

def get_state():
    try:
        global __stateJson
        if __stateJson != None:
            return __stateJson
        json_data = open(__stateFilename)
        __stateJson = json.load(json_data)
        #print(__stateJson)
        print("State read from", __stateFilename)
        return __stateJson
    except:
        __stateJson = __stateDefault
        print("State initialized")
        return __stateJson
    
def save_state(newState):
    try:
        __stateJson = newState
        with open(__stateFilename, 'w') as outfile:
            json.dump(__stateJson, outfile)
        print("State written to", __stateFilename)
    except:
        pass
