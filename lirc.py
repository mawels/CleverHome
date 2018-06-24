import subprocess

class Lirc:
    @staticmethod
    def send_once(remote_name, key):
        run = subprocess.Popen("irsend SEND_ONCE " + remote_name + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (stdout, stderr) = run.communicate()
        return True

    @staticmethod
    def send_start(remote_name, key):
        run = subprocess.Popen("irsend SEND_START " + remote_name + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (stdout, stderr) = run.communicate()
        return True

    @staticmethod
    def send_stop(remote_name, key):
        run = subprocess.Popen("irsend SEND_STOP " + remote_name + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (stdout, stderr) = run.communicate()
        return True
    
    @staticmethod
    def get_remotes():
        run = subprocess.Popen("irsend list '' '' | grep -v '^$'", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (stdout, stderr) = run.communicate()
        remote_names = stdout.splitlines()
        return remote_names
    
    @staticmethod
    def get_remote_codes(remote_name):
        run = subprocess.Popen("irsend list " + remote_name + r" \ ", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
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