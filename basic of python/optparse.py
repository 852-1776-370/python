import subprocess
import optparse
parser=optparse.OptionParser()
parser.addoption("-i", "--interface",dest="interface", help="enter the inter the interface")
parser.addoption("-m", "--new_mac",dest="new_mac", help="enter the inter the new_ac")
(options,arguments)=parse.parseargs()
interface=options.interface
new_mac=options.new_mac
subprocess.call("ifconfig", interface, "down")
subprocess.call("ifconfig", interface, "hw", "ether", new_mac)
subprocess.call("ifconfig", interface, "up")
