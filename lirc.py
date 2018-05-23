import subprocess

class lirc:
    @staticmethod
    def send_once(remote, key):
        run = subprocess.Popen("irsend SEND_ONCE " + remote + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        return True

    @staticmethod
    def send_start(remote, key):
        run = subprocess.Popen("irsend SEND_START " + remote + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        return True

    @staticmethod
    def send_stop(remote, key):
        run = subprocess.Popen("irsend SEND_STOP " + remote + " " + key, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        return True
    
    @staticmethod
    def get_remotes():
        run = subprocess.Popen("irsend list '' '' | grep -v '^$'", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        (stdout, stderr) = run.communicate()
        remotes = stdout.splitlines()
        return remotes
    
    @staticmethod
    def get_remote_codes(remote):
        print(remote)
        run = subprocess.Popen("irsend list " + remote + r" \ ", stdout=subprocess.PIPE, shell=True, universal_newlines=True)
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