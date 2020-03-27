import os

import cv2

data_root = '/home/zwz/workspace/data'

pic_root = os.path.join(data_root, 'uav0000086_00000_v')

img_path = os.listdir(pic_root)
img_path.sort()

imgs = [os.path.join(pic_root, i) for i in img_path]

for img in imgs:
    frame = cv2.imread(img)
    cv2.imshow('dis', frame)
    k = cv2.waitKey(10)
    if k == 27:
        break
cv2.destroyAllWindows()
