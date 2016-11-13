#!/usr/bin/env python3
from collections import namedtuple
import subprocess
def chunks(iterable, chunk_size):
    for i in range(0, len(iterable), chunk_size):
    	yield iterable[i:i + chunk_size]


# Types
ble_pack = namedtuple('CTBPacket', ["search","page","interests"])
def encode(data):
	bin = '{:1b}{:07b}'.format(data.search, data.page) # search bin and page number
	bin += "".join(map(lambda x: str(int(x)), data.interests)) # interests
	bin = bin.ljust(28*8, "0") # pad to 28 bytes
	s = list(chunks(bin, 8)) # split into bytes
	bts = ["{0:0>2X}".format(int(x, 2)) for x in s]
	bts = " ".join(bts)
	return bts

def decode(input):
	bts = ""
	for byte in input.split():
		bts += "{:08b}".format(int(byte, 16))

	print(bts[0])

	search = bool(int(bts[0]))

	page = int(bts[1:8])
	print(page)
	print(search)
	intrbits = bts[8:]
	interests = [bool(int(x)) for x in intrbits]
	print(interests)
	decoded = ble_pack(search, page, interests)

	return decoded

"""
hciconfig hci0 down
hciconfig hci0 up
hciconfig hci0 noleadv
hcitool -i hci0 cmd 0x08 0x0009 0c 0c 09 63 6f 6f 6c 74 6f 75 72 62 61 6e 64
#hcitool -i hci0 cmd 0x08 0x0008 10 02 01 1a 0c ff 18 01 48 45 4c 4c 4f 57 4f 52 4c 44
# 0x0008 -> LE Set Advertising Data
# 01 -> significant octets 1
# 18 -> 1st octet length
# ff -> manufactorer data
# 17 bytes data
#hcitool -i hci0 cmd 0x08 0x0008 0e 02 01 05 02 ff 18 74 65 73 74 74 65 73 74 74 65 73 74 68 61 6c 6c 6f 64 61 76 69 64
#01 18 ff 74 65 73 74 74 65 73 74 74 65 73 74 68 61 6c 6c 6f 64 61 76 69 64
hcitool -i hci0 cmd 0x08 0x0008  1f  1e ff  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 07 08 09 10 11 12
hciconfig hci0 leadv 3"""

def start_broadcast(data):
	data = encode(data)
	print(data)
	subprocess.call(["hciconfig","hci0","down"], stdout=subprocess.PIPE)
	subprocess.call(["hciconfig","hci0","up"], stdout=subprocess.PIPE)
	subprocess.call(["hciconfig","hci0","noleadv"], stdout=subprocess.PIPE)
	name_cmd = "hcitool -i hci0 cmd 0x08 0x0009 0c 0c 09 63 6f 6f 6c 74 6f 75 72 62 61 6e 64"
	subprocess.call(name_cmd.split(), stdout=subprocess.PIPE)
	data_cmd = "hcitool -i hci0 cmd 0x08 0x0008 1f 1e ff " +  data #01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 07 08 09 10 11 12"
	subprocess.call(data_cmd.split(), stdout=subprocess.PIPE)
	subprocess.call(["hciconfig","hci0","leadv","3"], stdout=subprocess.PIPE)

#start_broadcast(None)