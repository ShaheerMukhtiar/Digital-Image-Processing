import numpy as np
import cv2 as cv



if __name__=="__main__":
    rows = int(input("Enter Number of Rows(height): "))
    cols = int(input("Enter Number of Cols(width): "))

    img =  np.ones((rows,cols,3),dtype=np.uint8) * 255
    img[:rows // 8, :cols // 8] = [0, 0, 0]            # Black Box
    img[:rows // 8, cols-cols // 8:] = [255, 0, 0]     # Blue Box
    img[rows - rows // 8:, :cols // 8] = [0, 255, 0]   # Green Box
    img[rows - rows // 8:, cols - cols // 8:] = [0, 0, 255]   # Red Box

    cv.imshow("Original Image",img)
    cv.waitKey()
