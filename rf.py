import json
from pathlib import Path
from rpi_rf import RFDevice

class Rf:    
    @staticmethod
    def send_once(remote_name, key):
        remoteManager = RfRemoteManager()
        remoteManager.send_key(remote_name, key)

    @staticmethod
    def send_start(remote_name, key):
        return 
        
    @staticmethod        
    def send_stop(remote_name, key):
        return
        
    
    @staticmethod
    def get_remotes():
        remoteManager = RfRemoteManager()
        return remoteManager.get_remote_names()
    
    @staticmethod
    def get_remote_codes(remote_name):
        remoteManager = RfRemoteManager()
        codes = []
        remote = remoteManager.get_remote(remote_name)
        print(remote)
        for key, command in remote.items():
            code = {}
            code["code"]=key
            code["label"]=key
            codes.append(code)
        return codes

class RfRemoteManager:
    config_file = 'rf.remotes.json'
    remote_definitions = {}

    gpio = 24
    pulselength = 350
    protocol = 1


    def __init__(self):
        self.load_remotes()

    def load_remotes(self):
        try:    
            file = open(self.config_file,'r')
            json_remote_definitions = file.read()
            self.remote_definitions = json.loads(json_remote_definitions)
        except IOError:
            if(not Path(self.config_file).is_file()):
                self.save_remotes()
                file.close()
    
    def save_remotes(self):
        try:
            file = open(self.config_file, 'w')
            json_remote_definitions = json.dumps(self.remote_definitions)
            file.write(json_remote_definitions)
            return True
        except IOError:
            print("Error guardando configuracion: " + IOError.strerror)
            return False
    
    def add_remote(self, remote_name):
        self.remote_definitions.extend(remote_name)
        self.save_remotes()
    
    def get_remote_names(self):
        remotes = []
        for name, codes in self.remote_definitions.items():
            remotes.append(name)
        return remotes

    def get_remote(self, name):
        return self.remote_definitions[name]
    
    def send_key(self, remote_name, key):
        rfdevice = RFDevice(self.gpio)
        rfdevice.enable_tx()
        code = self.remote_definitions[remote_name][key]
        rfdevice.tx_code(int(code), self.protocol, self.pulselength)
        rfdevice.cleanup()
        return
