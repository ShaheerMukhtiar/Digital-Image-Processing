import numpy as np
import cv2 as cv

def stripe_pattern(rows,cols,width):
    stripe_image = np.zeros((rows,cols),dtype = np.uint8)

    for row_counter in range(rows):
        for col_counter in range(0,cols,width * 2):
            stripe_image[row_counter,col_counter:col_counter+width] = 1

    cv.imshow("Stripe Pattern",stripe_image * 255)
    cv.waitKey(0)

def box_pattern(rows,cols,width):
    box_image =np.zeros((rows,cols),dtype =np.uint8)

    for row_counter in range((rows//2)-width,(rows//2)+width):
        for col_counter in range((cols//2)-width,(cols//2)+width):
            box_image[row_counter,col_counter] = 1
    cv.imshow("Box Pattern",box_image * 255)
    cv.waitKey(0)

def grid_pattern (rows,cols,width):
    grid_image = np.ones((rows,cols),dtype = np.uint8)

    for row_counter in range(rows):
        for col_counter in range(0,cols,width * 3):
            grid_image[row_counter,col_counter:col_counter+width] = 0

    for col_counter in range(cols):
        for row_counter in range(0, rows, width * 3):
            grid_image[row_counter:row_counter + width,col_counter] = 0

    cv.imshow("Grid Pattern",grid_image * 255)
    cv.waitKey(0)

if __name__ == "__main__":
    r = 300
    c = 500
    spacing = 10

    stripe_pattern(r, c, spacing)
    box_pattern(r, c, spacing)
    grid_pattern(r,c,spacing)

    cv.destroyAllWindows()