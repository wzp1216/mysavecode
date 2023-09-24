from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

morph_size = 0
max_operator = 4
max_elem = 2
max_kernel_size = 21
title_trackbar_operator_type="operator 0:opening 1:close 2:gradient  3:top hat 4:blak hat"
title_trackbar_element_type="element: 0:Rect  1:cross  2:Ellipse"
title_trackbar_kernel_size = "kernel size: 2n+1"
title_window="morphology demo"
morph_op_dic={0:cv.MORPH_OPEN,1:cv.MORPH_CLOSE,2:cv.MORPH_GRADIENT,3:cv.MORPH_TOPHAT,4:cv.MORPH_BLACKHAT}


def morphology_operations(val):
    morph_oerator=cv.getTrackbarPos(title_trackbar_element_type,title_window)
    morph_size=cv.getTrackbarPos(title_trackbar_kernel_size, title_window)
    morph_elem = 0
    val_type=cv.getTrackbarPos(title_trackbar_element_type, title_window)
    if val_type == 0:
        morph_elem = cv.MORPH_RECT
    elif val_type == 1:
        morph_elem = cv.MORPH_CROSS
    elif val_type == 2:
        morph_elem = cv.MORPH_ELLIPSE
    
    element = cv.getStructuringElement(morph_elem, (2*morph_size + 1, 2*morph_size+1), (morph_size, morph_size))
    operation = morph_op_dic[morph_operator]
    
    
    dst = cv.morphologyEx(src, operation, element)
    cv.imshow(title_window, dst)
    


parser=argparse.ArgumentParser(description='Code for mor morphology transformations...')
parser.add_argument('--input',help='path to input image',default='LinuxLogo.jpg')
args=parser.parse_args()

src=cv.imread(cv.samples.findFile(args.input))
if src is None:
    print("clould not open or find imge",args.input)
    exit(0)
cv.namedWindow(title_window,1)
cv.createTrackbar(title_trackbar_operator_type, title_window, 0, max_operator,morphology_operations)
cv.createTrackbar(title_trackbar_element_type, title_window, 0, max_elem,morphology_operations)
cv.createTrackbar(title_trackbar_kernel_size, title_window, 0, max_kernel_size,morphology_operations)

morphology_operations(0)
cv.waitKey()
cv.destroyAllWindows()

    
