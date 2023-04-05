'''
Created on 04-Sep-2019

@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from configparser import ConfigParser
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    
    parser = ConfigParser()
    with open("/app/config/propertiesfile.conf") as stream:
        parser.read_string("[default]\n" + stream.read())  # This line does the trick.
    AUDIT_ENABLED_IDMGMT = parser['default']['AUDIT_ENABLED_IDMGMT']
    AUDIT_ENABLED_IDPROVIDER = parser['default']['AUDIT_ENABLED_IDPROVIDER']
    
    return_message = 'Hello, world! \n AUDIT_ENABLED_IDPROVIDER={0}  AUDIT_ENABLED_IDPROVIDER={1}'
    return return_message.format(AUDIT_ENABLED_IDMGMT,AUDIT_ENABLED_IDPROVIDER)
        
if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
