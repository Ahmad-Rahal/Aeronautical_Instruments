import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
display = (2000, 1500)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up the perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50)
glTranslatef(0.0, 0.0, -10)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glRotatef(9, 3, 9, 1)  # Optional: Rotate the model
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Load and display the .obj model
    # Replace 'your_model.obj' with the path to your .obj model file
    with open('uploads_files_4656550_AK47Subdiv.obj', 'r') as f:
        obj_lines = f.readlines()
        glBegin(GL_TRIANGLES)
        for line in obj_lines:
            if line.startswith('v '):
                vertex = line.split()[1:]
                glVertex3fv([float(vertex[0]), float(vertex[1]), float(vertex[2])])
        glEnd()

    pygame.display.flip()
    pygame.time.wait(10)  # Adjust for the desired frame rate

pygame.quit()
