import cv2 as cv
import numpy as np

if __name__ == '__main__':
    filename = 'out_test.jpg'
    img = cv.imread(filename)

    pts_src = [[1209, 381], [3133, 673], [3113, 1729], [1193, 1745]]
    pts_src = np.array(pts_src)
    pts_dst = [[0, 0], [223, 0], [223, 223], [0, 223]]
    pts_dst = np.array(pts_dst)
    h, status = cv.findHomography(pts_src, pts_dst)
    print(h)

    im_dst = cv.warpPerspective(img, h, (224, 224))

    cv.imshow('', im_dst)
    cv.waitKey(0)
