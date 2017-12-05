import speedtest
from datetime import datetime

servers = []

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

download = round(s.download() / 1000000, 2)
upload = round(s.upload() / 1000000, 2)

f = open("speedtests.txt", "a")
f.write("Date: " + str(datetime.now()) + " | Download: " + str(download) + "mbps" + " | Upload: " + str(upload) + "mbps\n")