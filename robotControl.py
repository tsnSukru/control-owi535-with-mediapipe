import time

import usb.core
import usb.util

# USB cihazı için filtreleme yapın
dev = usb.core.find(idVendor=0x1267, idProduct=0x0000)
if dev is None:
    raise ValueError('OWI 535 bulunamadı')

# USB cihazını ayarlayın
dev.set_configuration()

#First byte
    #Gripper close == 0x01 = 1
    #Gripper open == 0x02 = 1
    #Wrist Up == 0x04 = 4
    #Wrist Down == 0x08 = 8
    #Elbow up == 0x10 = 16
    #Elbow down == 0x20 = 32
    #Shoulder up == 0x40 = 64
    #Shoulder down == 0x80 = 128

    #Second byte
    #Base rotate right == 0x01 = 1
    #Base rotate left == 0x02 = 2

    #Third byte
    #Light on == 0x01 = 1

def baseRotationLeft(duration = 0.1):
    dev.ctrl_transfer(64,6,0x100,0,[0,2,0],3)
    time.sleep(duration)
    dev.ctrl_transfer(64,6,0x100,0,[0, 0, 0],3)
    usb.util.dispose_resources(dev)

def baseRotationRight(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 1, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def shoulderUp(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [64, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def shoulderDown(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [128, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def elbowUp(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [16, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def elbowDown(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [32, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def gripperOpen(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [2, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def gripperClose(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [1, 0, 0], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def lightOn(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 1], 3)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)

def lightOff(duration = 0.1):
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    time.sleep(duration)
    time.sleep(duration)
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    usb.util.dispose_resources(dev)