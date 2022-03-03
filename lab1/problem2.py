import numpy as np
import cv2 as cv

def nearest_interpolation(original_image, ratio):
    height, width, channel = original_image.shape

    height *= ratio
    width *= ratio
    magnified_image = np.zeros((height, width, channel), np.uint8)
    for h in range(0, height):
        for w in range(0, width):
            magnified_image[h][w] = original_image[h // ratio][w // ratio]

    return magnified_image

def main():
    # read image
    original_image = cv.imread("lisa.jpeg")

    # magnify original image by 3
    magnified_image = nearest_interpolation(original_image, 3)
    print(original_image.shape, magnified_image.shape)
    cv.imshow("3x image (Nearest)", magnified_image)

    # check result with cv2 resize function
    # correct = cv.resize(original_image, (2022,1365), interpolation = cv.INTER_NEAREST)
    # if np.array_equal(correct, magnified_image):
    #     print("same")
    # else: 
    #     diff = correct - magnified_image
    #     print("diff", diff)
    #     cv.imshow("diff", diff)

    # press 's' to save image
    keyboard = cv.waitKey(0)
    if keyboard == ord('s'):
        cv.imwrite("2.png", magnified_image)

    cv.destroyAllWindows()

if __name__ == '__main__':
    main()