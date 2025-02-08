import numpy as np
import cv2 as cv

def down_sample(img,pix):
    return img[::pix,::pix]     # skipping rows/cols by pix

if __name__ == "__main__":
    orig = cv.imread("test_photo.jpg")
    cv.imshow("Original Image",orig)
    cv.waitKey(0)
    resized = cv.resize(orig,(512,512))    # image,cols,rows
    cv.imshow("Resized Image",resized)
    cv.waitKey(0)

    down_sample = down_sample(resized,3)
    cv.imshow("Down Sampled", down_sample)
    cv.waitKey(0)
    cv.destroyAllWindows()
