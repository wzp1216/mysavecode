import numpy as np
import cv2 as cv


def main():
    cluster_n=5
    img_size=512
    colors=np.zeros((1,cluster_n,3),np.uint8)
    colors[0,:]=255
    colors[0,:,0]=np.arange(0,180,180.0/cluster_n)
    colors=cv.cvtColor(colors,cv.COLOR_HSV2BGR)[0]

cv.imshow(colors)









if __name__=='__main__':
    main()
    cv.destroyAllWindows()
    
