from bluepy.btle import Scanner, DefaultDelegate
from helpers import decode, ble_pack
import time
import subprocess, multiprocessing, threading
import json

class ScanDelegate(DefaultDelegate):
    alarm_proc = None
    alarm_timer = None

    def __init__(self):
        DefaultDelegate.__init__(self)
        with open("config.json","r") as cfile:
            self.config = json.load(cfile)

        #self.alarm_proc = multiprocessing.Process(target=self.alarm, args=(,))

    def handleDiscovery(self, dev, isNewDev, isNewData):
        data = dev.getScanData()
        for d in data:
            print(dev.scanData)
            if 255 in dev.scanData and len(dev.scanData[255]) == 29:
                print(len(dev.scanData[255]))
                raw_data = " ".join(["{0:0>2X}".format(ord(b)) for b in dev.scanData[255]])
                d = decode(raw_data)
                if d.search:
                    m = self.config["i"]
                else:
                    m = self.config["a"]

                for i,b in enumerate(d.interests):
                    if b:
                        if i in m:
                            return self.start_alarm(dev.rssi)

    """def alarm(self):
        #time.sleep(50)
        print("foo")
        subprocess.call(["/home/pi/alarm-start.sh"], stdout=subprocess.PIPE)"""

    def stop_alarm():
        print("bla")

        subprocess.call(["python","/home/pi/CoolTourHat/propellor_off.py"], stdout=subprocess.PIPE)

    def start_alarm(self, rssi):
        subprocess.call(["python","/home/pi/CoolTourHat/propellor_on.py"], stdout=subprocess.PIPE)

        with open("/home/pi/state","w") as sfile:
            json.dump(time.time(), sfile)

            self.alarm_timer = threading.Timer(5, self.stop_alarm)




scanner = Scanner().withDelegate(ScanDelegate())
while True:
    devices = scanner.scan(10)
    for dev in devices:
        print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        for (adtype, desc, value) in dev.getScanData():
            print "  %s = %s" % (desc, value)