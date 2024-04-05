

class MOTOR_CONTROL:

    def __init__(self):
        self.motorID = 0x03
        self.motorStateFlag = 0
        self.dataToSend = [0, 0]

    def startStopMotor(self, can, state):
        self.motorStateFlag = state
        if(self.motorStateFlag):
            self.dataToSend[0] = 0x02
            self.dataToSend[1] = 0x00
            can.sendMessage(self.motorID, self.dataToSend)
        else:
            self.dataToSend[0] = 0x01
            self.dataToSend[1] = 0x00
            can.sendMessage(self.motorID, self.dataToSend)

    def setRight(self, can, valueToSet):
        self.dataToSend[0] = 0x03
        self.dataToSend[1] = -valueToSet
        can.sendMessage(self.motorID, self.dataToSend)

    def setLeft(self, can, valueToSet):
        self.dataToSend[0] = 0x03
        self.dataToSend[1] = valueToSet
        can.sendMessage(self.motorID, self.dataToSend)

    def setMotorRpm(self, can, value):
        if(self.motorStateFlag):
            self.dataToSend[0] = 0x04
            self.dataToSend[1] = value
            can.sendMessage(self.motorID, self.dataToSend)
