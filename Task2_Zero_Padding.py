import cv2
import numpy

if __name__ == "__main__":
    c= 500
    r = 500
    pad = 100
    mat_ones= numpy.ones((500,500),dtype = numpy.uint8)
    print(mat_ones)
    padded_mat = numpy.zeros((r+pad,c+pad),dtype = numpy.uint8)
    print("\nPadded Matrix")
    print(padded_mat)
    cv2.imshow("Initially padded Matrix",padded_mat*255)
    cv2.waitKey()


    # using this: x = y [row_start: row_ end, col_start: col_end]
    padded_mat[pad//2:r + pad//2, pad//2:c + pad//2] = mat_ones
    print("\nPadded Matrix Updated")
    print(padded_mat)
    cv2.imshow("Final padded Matrix",padded_mat*255)
    cv2.waitKey()
