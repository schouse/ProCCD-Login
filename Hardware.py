import serial
import serial.tools.list_ports
import time
from PySide2.QtCore import QObject

########################################################################################################################
# Protocol
    # 5 bytes are sent from Python program in quick succession
    # Byte00 is 0xCC for command header. Instructs what is coming in the next 4 bytes is a command
    # Byte01 is 0xAA is an identifier.
    # Byte02 is 0xAA is also identifier.
    # Byte03 is pin identifier.
    # Byte04 is the actual command for the above pin.

delayCommand = 0.001  # Delay between commands
pin_OFF = b'\x00'  # Pin Low
pin_ON = b'\x01'  # Pin High

pinMains = b'\x04'  # Mains
pinTUV = b'\x05'  # Trans UV
pinEWL = b'\x06'  # Epi White Light
pinTWL = b'\x07'  # Trans White Light
pinTBL = b'\x17'  # Trans Blue Light
pinEUVA = b'\x19'  # Epi UV A
pinEUVB = b'\x1B'  # Epi UV B
pinSpare = b'\x24'  # Spare pin
allPins = [b'\x04', b'\x05', b'\x06', b'\x07', b'\x17', b'\x19', b'\x1B', b'\x24']

focusFar = b'\x60'  #
focusNear = b'\x61'  #
irisOpen = b'\x62'  #
irisClose = b'\x63'  #
zoomIn = b'\x64'  #
zoomOut = b'\x65'  #
filterLeft = b'\x66'  #
filterRight = b'\x67'  #
spareLeft = b'\x68'  #
spareRight = b'\x69'  #

level3 = b'\x03'
level2 = b'\x02'
level1 = b'\x01'


class HardwareControl(QObject):

    def __init__(self,parent=None):
        self.ardu = None
        self.ports = list(serial.tools.list_ports.comports())  # List all the ports in ports[]

        for p in self.ports:
            if "Arduino" in p.description:  # Identify which port is Arduino and select it
                ArduinoPort = p[0]
                self.ardu = serial.Serial(ArduinoPort, 9600, timeout=0.1)
                # print("Arduino - HardwareDOTpy: ", ArduinoPort)



    def sendCommand(self, val):
        pass

    def relayOperate(self, pinID, ONorOFF):
        if self.ardu is not None:
            self.ardu.write(b'\xCC')         # Command Header
            time.sleep(delayCommand)
            self.ardu.write(b'\xAA')         # 0b10101010
            time.sleep(delayCommand)
            self.ardu.write(b'\xAA')         # 0b10101010
            time.sleep(delayCommand)
            self.ardu.write(pinID)           # Pin ID
            time.sleep(delayCommand)
            self.ardu.write(ONorOFF)
            time.sleep(delayCommand)

    def switchOFF(self):
        if self.ardu is not None:
            # print('Switching OFF')
            for pin in allPins:
                self.relayOperate(pin, pin_OFF)
                time.sleep(0.1)
            self.ardu.close()

    def relayMains(self):
        if self.ardu is not None:
            if self.ui.buttonMains.isChecked():
                self.ardu.relayOperate(pinMains, pin_OFF)
            else:
                self.ardu.relayOperate(pinMains, pin_ON)

    def relayEWL(self):
        if self.ardu is not None:
            if self.ui.buttonEpiWhite.isChecked():
                self.ardu.relayOperate(pinEWL, pin_OFF)
            else:
                self.ardu.relayOperate(pinEWL, pin_ON)

    def relayTUV(self):
        if self.ardu is not None:
            if self.ui.buttonTransUV.isChecked():
                self.ardu.relayOperate(pinTUV, pin_OFF)
            else:
                self.ardu.relayOperate(pinTUV, pin_ON)

    def relayTWL(self):
        if self.ardu is not None:
            if self.ui.buttonTransWhite.isChecked():
                self.ardu.relayOperate(pinTWL, pin_OFF)
            else:
                self.ardu.relayOperate(pinTWL, pin_ON)

    def relayTBL(self):
        if self.ardu is not None:
            if self.ui.buttonTransBlue.isChecked():
                self.ardu.relayOperate(pinTBL, pin_OFF)
            else:
                self.ardu.relayOperate(pinTBL, pin_ON)

    def relayUVA(self):
        if self.ardu is not None:
            if self.ui.buttonEpiUVA.isChecked():
                self.ardu.relayOperate(pinEUVA, pin_OFF)
            else:
                self.ardu.relayOperate(pinEUVA, pin_ON)

    def relayUVB(self):
        if self.ardu is not None:
            if self.ui.buttonEpiUVB.isChecked():
                self.ardu.relayOperate(pinEUVB, pin_OFF)
            else:
                self.ardu.relayOperate(pinEUVB, pin_ON)

#=======================================================================================================================
    # Protocol
    # 5 bytes are sent from Python program in quick succession
    # Byte00 is 0xCC for command header. Instructs what is coming in the next 4 bytes is a command
    # Byte01 is 0xAA is an identifier.
    # Byte02 is 0xAA is also identifier.
    # Byte03 is pin identifier.
    # Byte04 is the actual command for the above pin.

    def hbridgeOperate(self, idFZI, howMuchToMove):
        if self.ardu is not None:
            self.ardu.write(b'\xCC')         # Command Header
            time.sleep(delayCommand)
            self.ardu.write(b'\xAA')         # 0b10101010
            time.sleep(delayCommand)
            self.ardu.write(b'\xAA')         # 0b10101010
            time.sleep(delayCommand)
            self.ardu.write(idFZI)           # Pin ID
            time.sleep(delayCommand)
            self.ardu.write(howMuchToMove)
            time.sleep(delayCommand)

    # -------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------
    def hbridgeFocusFar3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusFar, level3)

    def hbridgeFocusFar2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusFar, level2)

    def hbridgeFocusFar1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusFar, level1)

    def hbridgeFocusNear3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusNear, level3)

    def hbridgeFocusNear2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusNear, level2)

    def hbridgeFocusNear1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(focusNear, level1)
    #-------------------------------------------------------------------------------------------------------------------

    def hbridgeIrisOpen3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisOpen, level3)

    def hbridgeIrisOpen2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisOpen, level2)

    def hbridgeIrisOpen1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisOpen, level1)

    def hbridgeIrisClose3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisClose, level3)

    def hbridgeIrisClose2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisClose, level2)

    def hbridgeIrisClose1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(irisClose, level1)
    #-------------------------------------------------------------------------------------------------------------------

    def hbridgeZoomIn3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomIn, level3)

    def hbridgeZoomIn2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomIn, level2)

    def hbridgeZoomIn1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomIn, level1)

    def hbridgeZoomOut3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomOut, level3)

    def hbridgeZoomOut2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomOut, level2)

    def hbridgeZoomOut1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(zoomOut, level1)
    #-------------------------------------------------------------------------------------------------------------------

    def hbridgeSpareL3(self): # 2nd H-bridge of the 2nd L298
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareLeft, level3)

    def hbridgeSpareL2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareLeft, level2)

    def hbridgeSpareL1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareLeft, level1)

    def hbridgeSpareR3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareRight, level3)

    def hbridgeSpareR2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareRight, level2)

    def hbridgeSpareR1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(spareRight, level1)
    #-------------------------------------------------------------------------------------------------------------------

    def hbridgeFilterL3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterLeft, level3)

    def hbridgeFilterL2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterLeft, level2)

    def hbridgeFilterL1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterLeft, level1)

    def hbridgeFilterR3(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterRight, level3)

    def hbridgeFilterR2(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterRight, level2)

    def hbridgeFilterR1(self):
        if self.ardu is not None:
            self.ardu.hbridgeOperate(filterRight, level1)
    #-------------------------------------------------------------------------------------------------------------------


    # ########################################################################################################################

if __name__ == "__main__":
    app = HardwareControl()
    while(1):
        app.relayOperate(pinMains, pin_ON)
        app.hbridgeOperate(irisOpen, level3)
        print('ON')
        time.sleep(1)
        app.relayOperate(pinMains, pin_OFF)
        app.hbridgeOperate(irisClose, level3)
        print('OFF')
        time.sleep(1)
