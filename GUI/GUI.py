import customtkinter as ctk
from model import MODEL_SHOW
from CAN_network import CAN
from motorControl import MOTOR_CONTROL
from VL6180X_control import VL6180X

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

class CAN_PROJECT_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CAN Project")
        self.root.geometry("1500x900")
        
        self.root.columnconfigure(0, weight= 1)
        self.root.columnconfigure(1, weight= 2)
        self.root.columnconfigure(2, weight= 2)
        self.root.columnconfigure(3, weight= 2)
        
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=3)

        self.accID = 0x02
        self.motorID = 0x03
        self.htpID = 0x01
        
        self.accData = [0, 0, 0]

        self.modelShow = MODEL_SHOW()
        self.model_script_path= "model.py"
        self.canData = CAN()
        self.motorIns = MOTOR_CONTROL()
        self.VL6180Xins = VL6180X()

        #leftFrame
        self.leftFrame = ctk.CTkFrame(master=self.root, fg_color="#333333")
        self.leftFrame.grid(row= 0, column=0, rowspan=2, sticky="nsew")
        self.leftFrame.columnconfigure(0, weight=1)
        self.leftFrame.columnconfigure(1, weight=3)
        self.leftFrame.columnconfigure(2, weight=1)
        self.leftFrame.rowconfigure(0, weight=1)
        self.leftFrame.rowconfigure(1, weight=1)
        self.leftFrame.rowconfigure(2, weight=1)
        self.leftFrame.rowconfigure(3, weight=1)
        self.leftFrame.rowconfigure(4, weight=1)
        self.graphics_panel = ctk.CTkButton(master=self.leftFrame, text="3D Model Panel", command=self.graphic_buttonAction)
        self.graphics_panel.grid(row=0, column=1, padx=5, sticky="ew")
        self.light_distance_button = ctk.CTkButton(master=self.leftFrame, text="Light-Distance", command=self.light_distance_buttonAction)
        self.light_distance_button.grid(row=1, column=1, padx=5, sticky="ew")
        self.canStateSwitch = ctk.CTkSwitch(master=self.leftFrame, text="Can State", command=self.canSwitchAction, onvalue="on", offvalue="off")
        self.canStateSwitch.grid(row=2, column=1, padx=5, sticky="ew")
        self.motorStateSwitch = ctk.CTkSwitch(master=self.leftFrame, text="Motor State", command=self.motorSwitchAction, onvalue="on", offvalue="off")
        self.motorStateSwitch.grid(row=3, column=1, padx=5, sticky="ew")
        
        #frame10
        self.frame10 = ctk.CTkFrame(master=self.root)
        self.frame10.grid(row=0, column=1, columnspan=3, padx=(10,10), pady=(10,10), sticky="nwes")
        self.frame10.columnconfigure(0, weight=1)
        self.frame10.columnconfigure(1, weight=1)
        self.frame10.columnconfigure(2, weight=1)
        self.frame10.rowconfigure(0, weight=1)
        self.frame10.rowconfigure(1, weight=1)
        self.frame10.rowconfigure(2, weight=1)
        self.frame10.rowconfigure(3, weight=1)
        
         #label
        self.pressure_label = ctk.CTkLabel(master=self.frame10, text="Pressure")
        self.pressure_label.grid(row=0, column=0, padx=(20,0), sticky="w")
        self.wind_velocity_label = ctk.CTkLabel(master=self.frame10, text="Wind velocity")
        self.wind_velocity_label.grid(row=2, column=0, padx=(20,0), sticky="w")
        self.light_label = ctk.CTkLabel(master=self.frame10, text="Light")
        self.light_label.grid(row=0, column=1, padx=(20,0), sticky="w")
        self.temprature_label = ctk.CTkLabel(master=self.frame10, text="Temprature")
        self.temprature_label.grid(row=2, column=1, padx=(20,0), sticky="w")
        self.distance_label = ctk.CTkLabel(master=self.frame10, text="Distance")
        self.distance_label.grid(row=0, column=2, padx=(20,0), sticky="w")
        self.humidity_label = ctk.CTkLabel(master=self.frame10, text="Humidity")
        self.humidity_label.grid(row=2, column=2, padx=(20,0), sticky="w")
        
        #dataOutput
        self.pressure_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.pressure_output.grid(row=1, column=0, padx=(10,5), sticky="nwe")
        self.wind_velocity_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.wind_velocity_output.grid(row=3, column=0, padx=(10,5), sticky="nwe")
        self.light_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.light_output.grid(row=1, column=1, padx=(5,5),sticky="nwe")
        self.temprature_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.temprature_output.grid(row=3, column=1, padx=(5,5),sticky="nwe")
        self.distance_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.distance_output.grid(row=1, column=2, padx=(5,10),sticky="nwe")
        self.humidity_output = ctk.CTkLabel(master=self.frame10, fg_color="#333333", corner_radius=5, text="0")
        self.humidity_output.grid(row=3, column=2, padx=(5,10),sticky="nwe")
        
        
        #motorControlFrame
        self.frame11 = ctk.CTkFrame(master=self.root)
        self.frame11.grid(row=1, column=1, padx=(10,5), pady=(30,30), sticky="nwes")
        self.frame11.columnconfigure(0, weight=1)
        self.frame11.rowconfigure(0, weight=1)
        self.frame11.rowconfigure(2, weight=1)
        self.frame11.rowconfigure(3, weight=1)
        self.frame12 = ctk.CTkFrame(master=self.root)
        self.frame12.grid(row=1, column=2, padx=(5,5), pady=(30,30), sticky="nwes")
        self.frame12.columnconfigure(0, weight=1)
        self.frame12.rowconfigure(0, weight=1)
        self.frame12.rowconfigure(1, weight=1)
        self.frame12.rowconfigure(2, weight=1)
        self.frame12.rowconfigure(3, weight=1)
        self.frame13 = ctk.CTkFrame(master=self.root)
        self.frame13.grid(row=1, column=3, padx=(5,10), pady=(30,30), sticky="nwes")
        self.frame13.columnconfigure(0, weight=1)
        self.frame13.rowconfigure(0, weight=1)
        self.frame13.rowconfigure(1, weight=1)
        self.frame13.rowconfigure(2, weight=1)
        
        
        #frame11Content
        self.frame11_title = ctk.CTkLabel(master=self.frame11, text="RPM Control", fg_color="#333333", corner_radius=10)
        self.frame11_title.grid(row=0, column=0, padx=5, pady=5, sticky="new")
        self.rpm_slider = ctk.CTkSlider(master=self.frame11, from_=0, to=100, command=self.rpm_sliderAction)
        self.rpm_slider.grid(row=1, column=0, sticky="new")
        self.rpm_slider.set(0)
        self.rpm_entry = ctk.CTkEntry(master=self.frame11, placeholder_text="Set percentage %")
        self.rpm_entry.grid(row=2, column=0, padx=5, sticky="ew")
        self.set_rpm_button = ctk.CTkButton(master=self.frame11, text="Set", command=self.rpm_buttonAction)
        self.set_rpm_button.grid(row=3, column=0, padx=5, sticky="nwe")
        
        #frame12Content
        self.frame11_title = ctk.CTkLabel(master=self.frame12, text="Angle Control", fg_color="#333333", corner_radius=10)
        self.frame11_title.grid(row=0, column=0, padx=5, pady=5, sticky="new")
        self.position_entry = ctk.CTkEntry(master=self.frame12, placeholder_text="Set value (0 , 255)")
        self.position_entry.grid(row=1, column=0, padx=5, sticky="nwe")
        self.set_left = ctk.CTkButton(master=self.frame12, text="<<", command=self.set_left_buttonAction)
        self.set_left.grid(row=2, column=0, padx=5, sticky="we")
        self.set_right = ctk.CTkButton(master=self.frame12, text=">>", command=self.set_right_buttonAction)
        self.set_right.grid(row=3, column=0, padx=5, sticky="nwe")
        
        #frame13Content
        self.frame11_title = ctk.CTkLabel(master=self.frame13, text="Motor Status", fg_color="#333333", corner_radius=10)
        self.frame11_title.grid(row=0, column=0, padx=5, pady=5, sticky="new")
        self.rpm_label = ctk.CTkLabel(master=self.frame13, text="RPM:")
        self.rpm_label.grid(row=1, column=0, padx=5, sticky="nwe")
        self.position_label = ctk.CTkLabel(master=self.frame13, text="Position:")
        self.position_label.grid(row=2, column=0, padx=5, sticky="nwe")

        self.stateFlag = False
      
        self.whileLoop()


    def canSwitchAction(self):
        if(self.canStateSwitch.get() == "on"):
            self.stateFlag = True
        elif(self.canStateSwitch.get() == "off"):
            self.stateFlag = False
        self.canData.canState(canStateFlag=self.stateFlag)
        self.updateConfiguration()

    def rpm_sliderAction(self):
        self.value = int(255 * self.rpm_slider.get()/100)
        self.motorIns.setMotorRpm(can=self.canData,value=self.value)

    def rpm_buttonAction(self):
        self.value = int(255 * int(self.rpm_entry.get())/100)
        self.rpm_slider.set(int(self.rpm_entry.get()))
        self.motorIns.setMotorRpm(can=self.canData,value=self.value)

    def set_left_buttonAction(self):
        self.valueToSet = self.position_entry.get()
        self.motorIns.setLeft(can=self.canData, valueToSet=self.valueToSet)

    def set_right_buttonAction(self):
        self.valueToSet = self.position_entry.get()
        self.motorIns.setRight(can=self.canData, valueToSet=self.valueToSet)

    def motorSwitchAction(self):
        if(self.motorStateSwitch.get() == "on"):
            self.state = True
        elif(self.motorStateSwitch.get() == "off"):
            self.state = False
        self.motorIns.startStopMotor(can=self.canData, state=self.state)

    def light_distance_buttonAction(self):
       self.VL6180Xins.lightDistanceCon(can=self.canData)
    
    def updateConfiguration(self):
        self.pressure_output.configure(text= self.canData.messageFromHTP[0])
        self.wind_velocity_output.configure(text= self.canData.messageFromDXL_Anemo[2])
        self.light_output.configure(text= self.canData.messageToLight)
        self.temprature_output.configure(text= self.canData.messageFromHTP[3])
        self.distance_output.configure(text= self.canData.messageToDistance)
        self.humidity_output.configure(text= self.canData.messageFromHTP[1])
        self.rpm_label.configure(text= f"RPM: {self.canData.messageFromDXL_Anemo[0]}")
        self.position_label.configure(text= f"Position: {self.canData.messageFromDXL_Anemo[1]}")
        self.accData[0] = self.canData.messageFromAcc[0]
        self.accData[1] = self.canData.messageFromAcc[1]
        self.accData[2] = self.canData.messageFromAcc[2]
    
    def graphic_buttonAction(self):
        self.modelShow.setup()
        self.modelShow.running = True

    def whileLoop(self):
        if(self.stateFlag ):
            self.canData.recvMessage()
            self.updateConfiguration()
        if(self.modelShow.running):
            self.modelShow.run(self.accData)
        else:
            self.modelShow.stopRun()
        self.updateConfiguration()

        self.root.after(1, self.whileLoop)
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = CAN_PROJECT_GUI(root)
    root.mainloop()        