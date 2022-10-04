#!/usr/bin/env python

'''
1.show test img;
2.gass filter
3.find IO,and draw
4.scrach test 
'''

import numpy as np
import cv2 as cv
import os
import sys

def aplitfn(fn):
    path,fn=os.path.split(fn)
    name,ext=os.path.splitext(fn)
    return path,name,ext

def processImage(fn):
    print('processing %s... ' % fn)
    img = cv.imread(fn, 0)
    if img is None:
        print("Failed to load", fn)
        return None

    assert w == img.shape[1] and h == img.shape[0], ("size: %d x %d ... " % (img.shape[1], img.shape[0]))
    found, corners = cv.findChessboardCorners(img, pattern_size)
    if found:
        term = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 30, 0.1)
        cv.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

    if debug_dir:
        vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        cv.drawChessboardCorners(vis, pattern_size, corners, found)
        _path, name, _ext = splitfn(fn)
        outfile = os.path.join(debug_dir, name + '_chess.png')
        cv.imwrite(outfile, vis)

    if not found:
        print('chessboard not found')
        return None

    print('           %s... OK' % fn)
    return (corners.reshape(-1, 2), pattern_points)




def main():
    import getopt
    from glob import glob

    debug_dir='./output/'
    set_threads=4
    square_size = 1.0
    img_mask = './test_img/side/Image_??.jpg'  # default
    img_names = glob(img_mask)

    if debug_dir and not os.path.isdir(debug_dir):
        os.mkdir(debug_dir)
    h, w = cv.imread(img_names[0], cv.IMREAD_GRAYSCALE).shape[:2]  # TODO: use imquery call to retrieve results









'''    
    obj_points = []
    img_points = []

    threads_num = int(args.get('--threads'))
    if threads_num <= 1:
        chessboards = [processImage(fn) for fn in img_names]
    else:
        print("Run with %d threads..." % threads_num)
        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(threads_num)
        chessboards = pool.map(processImage, img_names)

    chessboards = [x for x in chessboards if x is not None]
    for (corners, pattern_points) in chessboards:
        img_points.append(corners)
        obj_points.append(pattern_points)

    # calculate camera distortion
    rms, camera_matrix, dist_coefs, _rvecs, _tvecs = cv.calibrateCamera(obj_points, img_points, (w, h), None, None)

    print("\nRMS:", rms)
    print("camera matrix:\n", camera_matrix)
    print("distortion coefficients: ", dist_coefs.ravel())

    # undistort the image with the calibration
    print('')
    for fn in img_names if debug_dir else []:
        _path, name, _ext = splitfn(fn)
        img_found = os.path.join(debug_dir, name + '_chess.png')
        outfile = os.path.join(debug_dir, name + '_undistorted.png')

        img = cv.imread(img_found)
        if img is None:
            continue

        h, w = img.shape[:2]
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

        dst = cv.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

        # crop and save the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]

        print('Undistorted image written to: %s' % outfile)
        cv.imwrite(outfile, dst)
        cv.imshow('dst',dst)
        cv.waitKey(0)

    print('Done')
'''    
    


if __name__ == '__main__':
    print(__doc__)
    main()
    #cv.DestroyAllWindows()
