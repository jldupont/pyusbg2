"""
    Quick test
    @author: Jean-Lou Dupont
"""
import os
import sys

### insert our development package
thisdir=os.path.dirname(__file__)
sys.path.insert(0, thisdir)

import usb.core

dev=usb.core.find(idVendor=0x1d6b)  ## Linux Foundation

print "Linux Foundation device: ",dev


dev_phidgets=usb.core.find(idVendor=0x06c2)  ## Linux Foundation
print "Phidgets device: ", dev_phidgets
