import cv2
import numpy as np

height = 300
width = 300

# Get the boundaries of the screen
top = 0
bottom = height
left = 0
right = width

circle_vel = [4, 2]
# Draw a circle
circle_pos = [100, 100]  # x, y coordinates
circle_radius = 50
color = (0, 255, 0)  # green color in BGR format
thickness = 2

for frames in range(0, 601):
    screen = np.zeros((height, width, 3), dtype=np.uint8)

    if circle_pos[1] - circle_radius < top:
        circle_pos[1] = circle_radius
        circle_vel[1] *= -1
    elif circle_pos[1] + circle_radius > bottom:
        circle_pos[1] = bottom - circle_radius
        circle_vel[1] *= -1

    # Check for collision with the left or right side of the screen
    if circle_pos[0] - circle_radius < left:
        circle_pos[0] = circle_radius
        circle_vel[0] *= -1
    elif circle_pos[0] + circle_radius > right:
        circle_pos[0] = right - circle_radius
        circle_vel[0] *= -1
    circle_pos[0] += circle_vel[0]
    circle_pos[1] += circle_vel[1]

    screen = cv2.circle(screen, circle_pos, circle_radius, color, thickness)

    # Display the image
    cv2.imshow('Bola gato', screen)
    cv2.waitKey(10)