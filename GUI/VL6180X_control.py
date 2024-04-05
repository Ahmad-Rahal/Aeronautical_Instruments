

class VL6180X:
    def __init__(self):
        self.dataToSend = [0]
        self.htpID = 0x01

    def lightDistanceCon(self, can):
       can.lightDistanceFlag = not can.lightDistanceFlag
       if(can.lightDistanceFlag):
           can.messageToDistance = 0
           self.dataToSend[0] = 0x02
           can.sendMessage(self.htpID, self.dataToSend)
       else:
           can.messageToLight = 0
           self.dataToSend[0] = 0x01
           can.sendMessage(self.htpID, self.dataToSend)