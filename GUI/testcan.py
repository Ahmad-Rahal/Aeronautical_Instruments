import can

# Initialize the CAN interface (choose the appropriate interface)
can_interface = 'socketcan'  # Change this to 'pcan' or other supported interface if needed
bus = can.interface.Bus(channel=can_interface, bustype='socketcan')

# Main loop to receive and process CAN messages
while True:
    message = bus.recv()
    
    # Process the received message (example: print the message)
    print(f"Received CAN message: ID={message.arbitration_id}, Data={message.data}")