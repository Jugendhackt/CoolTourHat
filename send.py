from helpers import ble_pack, start_broadcast
import json
import time

with open("config.json","r") as cfile:
    config = json.load(cfile)

search = True

while True:
    time.sleep(2)
    if search:
        m = config["i"]
    else:
        m = config["a"]

    m_l = []
    for i in range(max(m)):
        if i in m:
            m_l.append(True)
        else:
            m_l.append(False)

    print(m_l)

    search = not search

    data = ble_pack(search, 1, m_l)
    d = start_broadcast(data)