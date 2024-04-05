import can
import re

class CAN:
    def __init__(self):
        self.messageFromAcc = [0, 0, 0]
        self.messageFromDXL_Anemo = [0, 0, 0]
        self.messageFromHTP = [0, 0, 0, 0]
        self.messageToLight = 0
        self.messageToDistance = 0
        self.messageToSend = 0
        self.canStateFlag = 0

    def canInit(self):
        # Initialize the CAN interface (choose the appropriate interface)
        self.can_interface = 'can0'  # Change this to 'pcan' or other supported interface if needed
        self.bus = can.interface.Bus(channel=self.can_interface, bustype='socketcan')

    def canShutdown(self):
        self.bus.shutdown()

    def canState(self, canStateFlag):
        self.canStateFlag = canStateFlag
        if(self.canStateFlag):
            self.canInit()
        else:
            self.canShutdown()
            self.messageFromHTP[0] = 0
            self.messageFromDXL_Anemo[2] = 0
            self.messageToLight = 0
            self.messageFromHTP[2] = 0
            self.messageToDistance = 0
            self.messageFromHTP[1]= 0
            self.messageFromDXL_Anemo[0] = 0
            self.messageFromDXL_Anemo[1] = 0

    def recvMessage(self):
        self.message = self.bus.recv()
        if(self.message.arbitration_id == 0x42): #MPU9250
            self.messageFromAcc[0] = (self.message.data[0] << 8) | self.message.data[1]
            self.messageFromAcc[1] = (self.message.data[2] << 8) | self.message.data[3]
            self.messageFromAcc[2] = (self.message.data[4] << 8) | self.message.data[5]
        elif(self.message.arbitration_id == 0x43): #DYN_ANEMO_PRESS
            self.messageFromDXL_Anemo[0] = self.message.data[0]
            self.messageFromDXL_Anemo[1] = self.message.data[1]
            self.messageFromDXL_Anemo[2] = self.message.data[2]
        elif(self.message.arbitration_id == 0x40): #VL6180X
            self.lightDistanceFlag = False
            self.messageToDistance = (self.message.data[0] << 8) | self.message.data[1]
            self.messageFromHTP[0] = (self.message.data[3] << 8) | self.message.data[4]
            self.messageFromHTP[1] = self.message.data[5]
            self.messageFromHTP[2] = self.message.data[6]
            self.messageFromHTP[3] = self.message.data[7]
        elif(self.message.arbitration_id == 0x41): #VL6180X
            self.lightDistanceFlag = True
            self.messageToLight = (self.message.data[0] << 16) | (self.message.data[1] << 8) | self.message.data[2]
            self.messageFromHTP[0] = (self.message.data[3] << 8) | self.message.data[4]
            self.messageFromHTP[1] = self.message.data[5]
            self.messageFromHTP[2] = self.message.data[6]
            self.messageFromHTP[3] = self.message.data[7]

    def sendMessage(self, can_id, can_data):
        self.messageToSend = can.Message(arbitration_id=can_id, data=can_data, is_extended_id=False)
        
        self.bus.send(self.messageToSend)
    

       
     