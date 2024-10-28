import sys
import numpy as np
import cv2 as cv

from numpy import random

def make_gaussians(cluster_n,img_size):
    points=[]
    ref_distrs=[]
    for i in xrange(cluster_n):
        mean=(0.1+0.8*random.rand(2))*img_size
        a=(random.rand(2,2)-0.5)*img_size*0.1
        cov=np.dot(a.T,a)+img_size*0.05*np.eye(2)
        n=100+random.randint(900)
        pts=random.multivariate_normal(mean,cov,n)
        points.append(pts)
        ref_distrs.append((mean,cov))
    points=np.float32(np.vstack(points))
    return points,ref_distrs



