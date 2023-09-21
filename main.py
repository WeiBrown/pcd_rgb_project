import numpy as np
import cv2
from constants import rgb_camera_params as prgb
def project(point3d,tr_matrix):
    camera_coords_pt3d = np.dot(tr_matrix,point3d.T).T
    camera_coords_pt2d = np.dot(prgb.camera_matrix,camera_coords_pt3d[:-1])
    camera_coords_pt2d /= camera_coords_pt2d[2]
    x,y = camera_coords_pt2d[0], camera_coords_pt2d[1]
    return int(x),int(y)

def cal_rot():
    pass 
def cal_trans():
    pass

def get_trMatrix(calib_file):
    with open(calib_file, 'r') as file:
        lines = file.readlines()
    temp_mat = np.array([float(value) for value in lines[5][:-1].split(': ')[1].split(' ')]).reshape(3, 4)
    tr_mat = np.vstack((temp_mat,np.array([0,0,0,1])))
    return tr_mat

def main(pointcloud_file,rgb_image,calib_file):
    img = cv2.imread(rgb_image)
    points3d_ = np.delete(np.loadtxt(pointcloud_file,skiprows=11),3,axis=1)
    points3d = np.hstack((points3d_,np.ones((points3d_.shape[0],1))))
    tr_mat = get_trMatrix(calib_file)
    # points3d = np.fromfile(pointcloud_file,dtype=np.float32).reshape(-1,4)
    hashmap = []
    for i,point3d in enumerate(points3d):
        x,y = project(point3d,tr_mat)
        if x>0 and x<prgb.width and y>0 and y<prgb.height:
            img[y,x] = (255,255,255)
            hashmap.append([i,(x,y)])
    import ipdb;ipdb.set_trace()
    cv2.imwrite('res/0.png',img)

    

if __name__ == '__main__':
    pointcloud_file = 'data/0.pcd'
    rgb_image = 'data/0.png'
    calib_file = 'data/0.txt'
    main(pointcloud_file,rgb_image,calib_file)