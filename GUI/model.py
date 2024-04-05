import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from CAN_network import CAN


class MODEL_SHOW:
    def __init__(self):
        self.display = (2000, 1500)
        self.previous_roll = 0.0
        self.previous_pitch = 0.0
        self.previous_yaw = 0.0
        self.current_roll = 0.0
        self.current_pitch = 0.0
        self.current_yaw = 0.0
        self.can_data = [0.0, 0.0, 0.0]
        self.roll_step = 0.0
        self.pitch_step = 0.0
        self.yaw_step = 0.0 
        self.data = CAN()
        self.running = False



    def setup(self):
        # Initialize Pygame
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        glShadeModel(GL_SMOOTH)
        # Set up the perspective
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50)
        glTranslatef(0.0, 0.0, -30)

    def updateState(self, data):
        # Update the model position based on the CAN data
        self.can_data[0] = data[0]
        self.can_data[1] = data[1]
        self.can_data[2] = data[2]
        self.previous_roll = self.current_roll
        self.previous_pitch = self.current_pitch
        self.previous_yaw = self.current_yaw
        self.current_roll = self.can_data[0]
        self.current_pitch = self.can_data[1]
        self.current_yaw = self.can_data[2]
        self.yaw_step = self.current_yaw - self.previous_yaw
        self.pitch_step = self.current_pitch - self.previous_pitch
        self.roll_step = self.current_roll - self.previous_roll
        glRotatef(math.degrees(self.yaw_step), 0, 1, 0)  # Yaw
        glRotatef(math.degrees(self.pitch_step), 1, 0, 0)  # Pitch
        glRotatef(math.degrees(self.roll_step), 0, 0, 1)  # Roll
    
    def renderModel(self):
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Load and display the .obj model
    # Replace 'model.obj' with the path to your .obj model file
       with open('Yak-130.obj', 'r') as f:
        obj_lines = f.readlines()
        glBegin(GL_TRIANGLES)
        for line in obj_lines:
            if line.startswith('v '):
                vertex = line.split()[1:]
                glVertex3fv([float(vertex[0]), float(vertex[1]), float(vertex[2])])
        glEnd()

       pygame.display.flip()
         # Adjust for the desired frame rate

    

    def run(self, data):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             self.running = False

        self.updateState(data)
        self.renderModel()
    
    def stopRun(self):
       pygame.quit()


# if __name__ == '__main__':
#     viewer = MODEL_SHOW()
#     viewer.setup()
#     viewer.run() 


 
    
    

    

