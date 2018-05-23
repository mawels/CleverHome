import subprocess, json
from pathlib import Path

class command:
    @staticmethod
    def send_once(remote, key):
        run = subprocess.Popen("", stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            return True
        else:
            return False

    @staticmethod
    def send_start(remote, key):
        run = subprocess.Popen("", stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            return True
        else:
            return False

    @staticmethod        
    def send_stop(remote, key):
        run = subprocess.Popen("", stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            return True
        else:
            return False
    
    @staticmethod
    def get_remotes():
        run = subprocess.Popen("irsend list '' '' | grep -v '^$'", stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            (stdout, stderr) = run.communicate()
            remotes = stdout.splitlines()
            return remotes
    
    @staticmethod
    def get_remote_codes(self, remote):
        run = subprocess.Popen("irsend list " + remote + " \ ", stdout=subprocess.PIPE, shell=True)
        (stdout, stderr) = run.communicate()
        codes = []
        for line in stdout.splitlines():
            code = line.split(" ")
            if len(code) == 2:
                code_label = {}
                code_label['code']=code[1]
                code_label['label']=code[1]
                codes.append(code_label)
        return codes

class commandRemotesManager:
    config_file = 'command.remotes.json'
    remote_definitions = {}

    def load_remotes(self):
        try:    
            file = open(self.config_file,'r')
            json_remote_definitions = file.read()
            self.remote_definitions = json.loads(json_remote_definitions)
        except IOError:
            if(not Path(self.config_file).is_file()):
                file = open(self.config_file, 'w')
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
    
    def add_remote(self, remote):
        self.remote_definitions.extend(remote)
        self.save_remotes()
    
    def list_remotes(self):
        remotes = []
        for (name, codes) in self.remote_definitions.items():
            remotes.append(name)

    def __init__(self):
        self.load_remotes()
