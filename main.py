print("Python environment working") #test

import sys
import warnings
import socket
import time
import json
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"

print("Hello welcome to DSYSender, mainly built for Linux Users who want to use The Resident Evil Requiem Dualsense mod (though hopefully it could help with other games too!) Im MDTH and hopefully soon I'll have a github distro for this setup. Please use Control + C to close this script whenever you feel like it")

if not CONFIG_PATH.is_file():
    print("WARNING: Config file is missing, please make sure the included config is also in this folder.")
    input("DSYSender will now exit. Press Enter to close: ")
    sys.exit(1)
else:
    print("Config file found successfully.")

with open(CONFIG_PATH) as f:
    config = json.load(f)

host = config["host"] # i doubt anyone will need to change this ever i dont think
port = config["port"] # port to send to : normally 6969 for dualsenseY
rate = config["rate"] # how many times per second it updates i didnt end up setting this up maybe will though eventually
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



#function to send payload to dsy
def send_payload(data : bytes):
    dsySocket.sendto(data, (host, port))


class PayloadWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(PAYLOAD_PATH.name):
            data = PAYLOAD_PATH.read_bytes()
            send_payload(data)
            # Payload sent
            # print("yes we sent the updated data lolololol")


observer = Observer()
observer.schedule(PayloadWatcher(), str(PAYLOAD_PATH.parent), recursive=False)
observer.start()

print("Watching payload for changes...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()