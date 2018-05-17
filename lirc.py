import subprocess

class lirc:
    @staticmethod
    def send_once(remote, key):
        run = subprocess.Popen("irsend SEND_ONCE " + remote + " " + key, stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            return True
        else:
            return False

    @staticmethod
    def send_start(remote, key):
        run = subprocess.Popen("irsend SEND_START " + remote + " " + key, stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            return True
        else:
            return False

    @staticmethod
    def send_stop(remote, key):
        run = subprocess.Popen("irsend SEND_STOP " + remote + " " + key, stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            run = subprocess.Popen('killall -s9 irsend > /dev/null 2>&1', stdout=subprocess.PIPE, shell=True)
            return True
        else:
            run = subprocess.Popen('killall -s9 irsend > /dev/null 2>&1', stdout=subprocess.PIPE, shell=True)
            return False
    
    @staticmethod
    def get_remotes():
        run = subprocess.Popen("irsend list '' '' | grep -v '^$'", stdout=subprocess.PIPE, shell=True)
        if(run.returncode == 0):
            (stdout, stderr) = run.communicate()
            remotes = stdout.splitlines()
            return remotes
    
    @staticmethod
    def get_remote_codes(remote):
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