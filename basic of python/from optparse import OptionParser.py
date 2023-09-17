import optparse 
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

import subprocess
import optparse
parser=optparse.OptionParser()
parser.addoption("-i", "--interface",dest="interface", help="enter the inter the interface")
parser.addoption("-m", "--new_mac",dest="new_mac", help="enter the inter the new_ac")
(options,arguments)=options.parseargs()
interface=options.interface
new_mac=options.new_mac
subprocess.call("ifconfig", interface, "down")
subprocess.call("ifconfig", interface, "hw", "ether", new_mac)
subprocess.call("ifconfig", interface, "up")