import numpy as np
class rgb_camera_params():
    width = 1224
    height = 370
    fx = 500
    fy = 500
    cx = 320
    cy = 240
    camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
    