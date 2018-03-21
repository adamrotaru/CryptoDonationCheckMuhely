# load config file

import json
import sys

__config_filename = "config.json"
__state_filename = "state.json"
__configJson = None

def get():
    try:
        global __configJson
        if __configJson != None:
            return __configJson
        json_data = open(__config_filename)
        __configJson = json.load(json_data)
        #print(__configJson)
        print("Config read from", __config_filename)
        return __configJson
    except:
        print("ERROR: could not load config from", __config_filename, sys.exc_info()[0])
        sys.exit()