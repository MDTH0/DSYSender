print("Python environment working") #test

DEBUG_MODE : int = 4 #0 = No Debug ,1 = ,2 = ,3 = , 4 = Payload Change Debug


import sys
import warnings
import socket
import time
import json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# check if in a kind of terminal
if not (sys.stdin.isatty() and sys.stdout.isatty()):
    print("DSYSender must be run from bundled dsySenderRun.sh.")
    sys.exit(1)

# Preventing multiple instances multiple instances
_singleton = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    _singleton.bind(("127.0.0.1", 51987))
except OSError:
    print("DSYSender is already running.")
    sys.exit(1)

BASE_DIR = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent

CONFIG_PATH = BASE_DIR / "config.json"

print("Hello welcome to DSYSender, mainly built for Linux Users who want to use The Resident Evil Requiem Dualsense mod (though hopefully it could help with other games too!) Im MDTH and hopefully soon I'll have a github distro for this setup. Please use Control + C to close this script whenever you feel like it")

if not CONFIG_PATH.is_file():
    print("WARNING: Config file is missing, please make sure the included config is also in this folder.")
    #warn the usert the config file is missing
    input("DSYSender will now exit. Press Enter to close: ")
    sys.exit(1)
else:
    print("Config file found successfully.")

with open(CONFIG_PATH) as f:
    config = json.load(f)

host = config["host"] # i doubt anyone will need to change this ever i dont think
port = config["port"] # port to send to : normally 6969 for dualsenseY
rate = config["rate"] # i changed my mind not using observer im going to use fixed updates a second
PAYLOAD_PATH = (BASE_DIR / config["payload_name"]) # path to the payload



if not PAYLOAD_PATH.is_file():
    print("WARNING: No payload file, please make sure the mod you are using supports this. it should be a json file and should be in the same folder as this python executable and the config file.")
    input("DSYSender will now exit. Press Enter to close: ")
    sys.exit(1)
else:
    print("Payload found")


# loaded config

print("Loaded Host: ", host)
print("Loaded Port: ", port)
print("Loaded Rate: ", rate)
print("Loaded Payload ", PAYLOAD_PATH)





#create socket
dsySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


lastPayload : bytes

firstPayload = True

def debugPrint(string : str, debugKey: int):
    if debugKey == DEBUG_MODE:
        print("DEBUG: ", string)
    

def should_send_payload(data : bytes):
    if FirstPayload == True:
        debugPrint("It is the first payload" , 4)
        return True
    elif data == lastPayload:
        debugPrint("Data unchanged from last payload", 4)
        return False
    else:
        debugPrint("Valid data and different from last payload", 4)
        return True
        

#function to send payload to dsy
def send_payload(dataSend : bytes):
    should = should_send_payload(dataSend)
    if should:
        debugPrint("Should send Payload", 4)
        dsySocket.sendto(dataSend, (host, port))
        lastPayload = dataSend
        if firstPayload == True:
            firstPayload = False

try:
    while True:
        time.sleep(0.02)
        data = PAYLOAD_PATH.read_bytes()
        send_payload(data)
        
except KeyboardInterrupt:
    print("You have pressed Ctrl + C and DSYSender will now exit.")
    input("Press enter to Exit: ")
    sys.exit(1)