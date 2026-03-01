DEBUG_MODE : int = 0 #0 = No Debug ,1 = Unused as of now ,2 = Update Rate,3 = , 4 = Payload Change Debug


import sys
import warnings
import socket
import time
import json
from pathlib import Path



# check if in a kind of terminal
if not (sys.stdin.isatty() and sys.stdout.isatty()):
    print("DSYSender must be run from bundled dsySenderRun.sh.")
    sys.exit(1)

# Preventing multiple instances multiple instances
_singleton = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    _singleton.bind(("127.0.0.1", 51987))  # im using this port to check for instances of my own script, in the event it's already in use fuck me i guess, i thought id add this comment for clarity
except OSError:
    print("DSYSender is already running.")
    sys.exit(1)

BASE_DIR = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent

CONFIG_PATH = BASE_DIR / "config.json"

print("Hello welcome to DSYSender, please remember to read ReadMe before trying to use. The readme bundled with the file is always the most updated way to get instructions. Please use Control + C to close this script whenever you feel like it")
print("Github Link: https://github.com/MDTH0/DSYSender")

if not CONFIG_PATH.is_file():
    print("WARNING: Config file is missing, please make sure the included config is also in this folder.")
    # warn the usert the config file is missing
    input("DSYSender will now exit. Press Enter to close: ")
    sys.exit(1)
else:
    print("Config file found successfully.")

with open(CONFIG_PATH) as f:
    config = json.load(f)

host = config["host"] # i doubt anyone will need to change this ever i dont think
port = config["port"] # port to send to : normally 6969 for dualsenseY
rate = config["rate"] # default 20, might not be needed, might be, probably, maybe set it to more if you have good pc if want, probably use numbers 1 can be divided by cleanly ex. 1/20 = 0.05, 1/50 = .02, 1/40 = 0.025 but 1/60 = .0166666666 (goes on forever basically, do not use this, same with 1/30)
sleepTime = 1/rate
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





# create socket
dsySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

lastPayload = None

lastPayloadTime = time.time()

def debugPrint(string : str, debugKey: int):
    if debugKey == DEBUG_MODE:
        print("DEBUG: ", string)
    

def should_send_payload(data : bytes, lastPayloadCompare : bytes, lastPayloadTime : float):
    if lastPayloadCompare == None:
        debugPrint("It is the first payload" , 4)
        return True
    elif time.time() - lastPayloadTime > 1:
        debugPrint("Forcing Data Send to Keep connection with DSY", 4)
        return True
    elif data == lastPayloadCompare:
        debugPrint("Data unchanged from last payload", 4)
        return False
    else:
        debugPrint("Valid data and different from last payload", 4)
        return True
        

# function to send payload to dsy
def send_payload(dataSend : bytes):
    global lastPayload
    global lastPayloadTime
    should = should_send_payload(dataSend, lastPayload, lastPayloadTime)
    if should:
        debugPrint("Should send Payload", 4)
        dsySocket.sendto(dataSend, (host, port))
        lastPayload = dataSend
        lastPayloadTime = time.time()

try:
    print("DSYSender Loaded, Please press Left Control + C to Exit")
    while True:
        time.sleep(sleepTime)
        data = PAYLOAD_PATH.read_bytes()
        send_payload(data)
except KeyboardInterrupt:
    print("You have pressed CTRL + C and DSYSender will now exit.")