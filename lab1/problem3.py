from html import parser
import numpy as np
import cv2 as cv
import argparse

def bilinear_interpolation(original_image, ratio):
    height, width, channel = original_image.shape

    height *= ratio
    width *= ratio
    magnified_image = np.zeros((height, width, channel), np.uint8)
    for h in range(0, height):
        y = h / ratio
        y1 = h // ratio
        y2 = h // ratio + 1
        if y2 >= (height // ratio):
            y1 = height // ratio - 2
            y2 = height // ratio - 1
        for w in range(0, width):
            x = w / ratio 

            x1 = w // ratio
            x2 = w // ratio + 1
            if x2 >= (width // ratio):
                x1 = width // ratio - 2
                x2 = width // ratio - 1
 
            magnified_image[h][w] = (original_image[y1][x1] * (x2 - x) * (y2 - y) + 
                                    original_image[y1][x2] * (x - x1) * (y2 - y) + 
                                    original_image[y2][x1] * (x2 - x) * (y - y1) + 
                                    original_image[y2][x2] * (x - x1) * (y - y1)
                                    ) / ((x2 - x1) * (y2 - y1))

    return magnified_image

def main():
    # setup argparser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", type=str, help="Image filepath")
    parser.add_argument("-r", "--ratio", type=int, help="Magnification ratio")

    # read args
    args = parser.parse_args()
    PATH = args.image
    RATIO = args.ratio

    # read image
    original_image = cv.imread(PATH)


    # magnify original image by RATIO
    magnified_image = bilinear_interpolation(original_image, RATIO)
    cv.imshow(f"{RATIO}x image (Bilinear)", magnified_image)

    # check result with cv2 resize function
    # correct = cv.resize(
    #     original_image, 
    #     (original_image.shape[1]*RATIO,original_image.shape[0]*RATIO), 
    #     interpolation = cv.INTER_LINEAR
    # )
    # if np.array_equal(correct, magnified_image):
    #     print("same")
    # else: 
    #     diff = correct - magnified_image
    #     print("diff", diff)
    #     cv.imshow("diff", diff)

    # press 's' to save image
    keyboard = cv.waitKey(0)
    if keyboard == ord('s'):
        cv.imwrite("3.png", magnified_image)

    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
