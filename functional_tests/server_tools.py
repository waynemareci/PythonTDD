import os.path
import time


from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host,email):
    session_key = subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER,
    ).decode().strip()


    while not os.path.exists(THIS_FOLDER + './session_key_file'):
        time.sleep(1)
    time.sleep(1)        
    f1=open(THIS_FOLDER + './session_key_file', 'r')
    session_key = f1.readlines()

    return session_key

def reset_database(host):
    subprocess.check_call(['fab','reset_database','--host={}'.format(host)],cwd=THIS_FOLDER)
