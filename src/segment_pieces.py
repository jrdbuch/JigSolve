import cv2 
import numpy as np
import matplotlib.pyplot as plt


def preprocess_pieces_img(path_to_img):

    img = cv2.imread(path_to_img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_edges = cv2.Canny(gray,150,200)
    gray = cv2.medianBlur(gray, ksize=5)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.blur(thresh, ksize=(3, 3))
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_on_img = cv2.drawContours(np.zeros(img.shape), contours, -1, (0,255,0), 3)
    plt.imshow(contour_on_img)
    plt.show()

if __name__ == '__main__':
    preprocess_pieces_img('/home/jaredbuchanan/jig_solve/data/ocean_puzzle_pieces.png')

