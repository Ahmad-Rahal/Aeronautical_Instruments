import can



class CAN:
    def __init__(self):
        # Initialize the CAN interface (choose the appropriate interface)
        self.can_interface = 'can0'  # Change this to 'pcan' or other supported interface if needed
        self.bus = can.interface.Bus(channel=self.can_interface, bustype='socketcan')
        self.message = self.bus.recv()

    def run(self):
        while True:
            self.message = self.bus.recv()
            # Process the received message (example: print the message)
            print(f"Received CAN message: ID={self.message.arbitration_id}, Data={self.message.data}")
       

if __name__== '__main__':
    can_work = CAN()
    can_work.run()