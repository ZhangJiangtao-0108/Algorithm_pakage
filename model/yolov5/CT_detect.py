## 文件test
import os
import time
from detect2 import detect
images_path = r'/home/pi/camera/'
server_args_path = r"/home/pi/work_space/yolov5_material/yolov5-master/sever.json"
while True:
    images = os.listdir(images_path)
    print(images)
    if len(images)!= 0:
        source = images_path
        detect(source= source, server_args_path = server_args_path) 
        del images


