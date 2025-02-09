import cv2 as cv
import numpy as np

if __name__ == "__main__":
    iron_man = cv.imread("ironman.png",0)
    cv.imshow("Original Iron Man",iron_man)
    cv.waitKey(0)
    r,c = iron_man.shape
    flipped = np.ones(iron_man.shape, dtype=np.uint8)
    for i in range(r-1,0,-1):
        for j in range (c):
            flipped[i,j]=iron_man[1-i,j]
    flipped[:r // 2, :] = iron_man[:r // 2, :]


    cv.imshow("Flipped iron man",flipped)
    cv.waitKey(0)
