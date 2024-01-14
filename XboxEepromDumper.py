from machine import Pin, I2C,
import time

EEPROM_ADDRESS = 0x54
EEPROM_SIZE = 256
DUMP = "eeprom.bin"
sda=Pin(0)
scl=Pin(1)
i2c=I2C(0, sda=sda, scl=scl, freq=400000)
devices = i2c.scan()
device_count = len(devices)
EEPROM_FOUND=False

for device in devices:
    print("Device: ", hex(device))
    if device==int(EEPROM_ADDRESS):
        print("Xbox Eeprom Found.....")
        print("Beginning Dump...")
        EEPROM_FOUND=True
        break
    else:
        print("Not Xbox Eeprom")
        pass

if EEPROM_FOUND==True:
    read_buffer=bytearray(EEPROM_SIZE)
    i2c.readfrom_into(EEPROM_ADDRESS, read_buffer)
    print("Creating eeprom.bin")    
    dump=open(DUMP, "w")
    dump.write(read_buffer, EEPROM_SIZE)
    dump.close()
    print("Finished!!!!")
    print("Save the 'eeprom.bin' file to your PC selecting View>>Files in the Thonny menu")
else:
    print("Xbox Eeprom not found!!!")
    