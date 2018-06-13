from project import app
import cv2
import os
from matplotlib import pyplot as plt



def get_image_difference(image_1, image_2):
    first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match





    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


def calculate_Similarity(inputImage, compareImage):

    input = cv2.imread(inputImage)
    compare = cv2.imread(compareImage)
    commutative_image_diff = get_image_difference(input, compare)

    #print(commutative_image_diff)

    return commutative_image_diff




def SIFT_detector(inputImage, compareImage, tempPath):
    print("make Iamge")
    print( tempPath)
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
    #inputImage = "/Users/Choichanghyun/Documents/Hardware_Experience/"+ inputImage

    input = cv2.imread( inputImage)
    compare = cv2.imread( compareImage)

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(input, None)
    kp2, des2 = sift.detectAndCompute(compare, None)
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)


    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    diffImage = cv2.drawMatchesKnn(input, kp1, compare, kp2, good, None, flags=2)
    #path = os.path.join(app.config['UPLOAD_FOLDER'], "images/1.bmp")

    cv2.imwrite("project/static/diff_images/diff_" + tempPath , diffImage)






