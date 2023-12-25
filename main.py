from speedtest import Speedtest
wifi = Speedtest()

print("Getting Download Speed...")
download = wifi.download()
#bit / 1024 ->Kbps /1024 ->Mbps
print(f'Download: {download / 1024 / 1024:.2f} mbps')
print("Getting Upload Speed...")
upload = wifi.upload()
print(f'Upload: {upload / 1024 / 1024:.2f} mbps')
print("Getting Ping Speed...")
ping = wifi.results.ping
print(f"Ping: {ping:.2f} ms")
