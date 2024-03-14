import glob
import os
import cv2

# for i, img_path in enumerate(glob.glob("images_2/*.JPG")):
# for i, img_path in enumerate(glob.glob("/223010087/SimonWorkspace/3dgs/data/gui/images/*.jpg")):
for i, img_path in enumerate(glob.glob("/223010087/SimonWorkspace/3dgs/data/lab/images/*.jpg")):
    img = cv2.imread(img_path)
    w, h = img.shape[1], img.shape[0]
    img = cv2.resize(img, (w//2, h//2))
    # cv2.imwrite("/223010087/SimonWorkspace/3dgs/data/gui/images_4/{}".format(os.path.basename(img_path)), img)
    cv2.imwrite("/223010087/SimonWorkspace/3dgs/data/lab/images_4/{}".format(os.path.basename(img_path)), img)
    print(i)
