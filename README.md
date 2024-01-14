# Pico-ogxbox-eepromdumper by JustinCase 01/12/2024


 A simple program to dump the EEPROM of an Original Xbox
 Nothing is written to the Eeprom!! This is only for dumping your eeprom.
    
This program is design to be used with Thonny IDE, which you can download here: https://thonny.org/
If you don't have micropython installed to your microcontroller you can do so by installing Thonny and downloading the latest version of Micropython to your board. Micropython has to be installed on your microcontroller for this program to work. Generally pressing the download button on the board and copying the precompiled uf2 file to the board, which you can find here: https://micropython.org/download/



Only a Raspberry Pico has been tested so far but any microcontroller that can run micropython and has I2C capabilities should work.
Start by wiring up your board to the motherboard of your xbox, see included picture for reference.
The easiest way to setup is by removing your DVD drive and HDD completely from the motherboard. Then power on the Xbox and wait 10 seconds after the Xbox turns on. The LED on your Xbox will most likely flash green or orange, due to the motherboard detecting that components are missing, this is normal and will not hurt your xbox. You need to wait 10 seconds after the Xbox turns on because the xbox is accessing the eeprom at this time and will cause an error if you try to read at the same time. Start Thonny on your PC or Mac and, with Thonny, open 'XboxEepromDumper.py' located in this repository. If you need to change the Pins being used you can do so on lines 7 & 8 but you may need to change the ID of the I2C port on line 9 as well.


Make sure your microcontroller is plugged into your PC and detected by Thonny. Press the green 'Play' button. If everything is wired up correctly you will see the program check each address on the I2C bus and see if it's the Xbox Eeprom. If it finds the Eeprom it will Dump the contents to 'eeprom.bin' and save it to the microcontroller's internal storage. Everything should take less than 20 seconds.
To save the 'eeprom.bin' to your Computer, in Thonny on the Top Menu bar click; View>>Files, you should now be able to download the 'eeprom.bin' to your computer. To read the dump you can use the Xbox Eeprom Editor: https://github.com/Ernegien/XboxEepromEditor
