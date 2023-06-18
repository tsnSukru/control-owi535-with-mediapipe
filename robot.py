import time
import usb.core
import usb.util

# USB cihazı için filtreleme yapın
dev = usb.core.find(idVendor=0x1267, idProduct=0x0000)
if dev is None:
    raise ValueError('OWI 535 bulunamadı')

# USB cihazını ayarlayın
dev.set_configuration()


def gripperOpen(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [2, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)


def gripperClose(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [1, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)


def gripperStop(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)


def elbowUp(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [16, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)


def elbowDown(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [32, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)


def elbowStop(duration=0.01):
    dev.ctrl_transfer(64, 6, 0x100, 0, [0, 0, 0], 3)
    time.sleep(duration)
    usb.util.dispose_resources(dev)
