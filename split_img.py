from icecream import ic 
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to input directory of images to stitch")
ap.add_argument("--subWidth", type=int, required=True, help="width of sub image")
ap.add_argument("--subHeight", type=int, required=True, help="height of sub image")
args = vars(ap.parse_args())

full_img = cv2.imread(args["image"])

cv2.imshow("eh", full_img)
cv2.waitKey(0)

h = args["subHeight"]
w = args["subWidth"]
ic(full_img.shape)
full_h, full_w, _ = full_img.shape
ic(full_h, full_w)

im1 = full_img[:h, :w]
im2 = full_img[:h, full_w - w:]
im3 = full_img[full_h - h:, :w]
im4 = full_img[full_h - h:, full_w - w:]

cv2.imshow("im1", im1)
cv2.imshow("im2", im2)
cv2.imshow("im3", im3)
cv2.imshow("im4", im4)

cv2.imwrite("images/eg1/im1.png", im1)
cv2.imwrite("images/eg1/im2.png", im2)
cv2.imwrite("images/eg1/im3.png", im3)
cv2.imwrite("images/eg1/im4.png", im4)

cv2.waitKey(0)