import subprocess
interface="eth0"
new_mac="11:23:34:56:78:89:"
print(interface,new_mac)
subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)
