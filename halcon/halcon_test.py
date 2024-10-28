import halcon as ha
"""
HTuple=ha.core.HTuple
HObject=ha.core.HObject
HWindow=ha.core.HWindow
HSystem=ha.core.HSystem
"""


"""
if __name__=='__main__':
    img=ha.read_image('test1.jpg')
    width,heigh=ha.get_image_size_s(img)
    region=ha.threshold(img,0,122)
    num_regions=ha.count_obj(ha.connection(region))
    print(f'Number of Regions" {num_regions}')
"""
if __name__=='__main__':
    img=ha.read_image('test.jpg')
    width,height=ha.get_image_size(img)
    winhandle=ha.open_window(0,0,width[0]/2,height[0]/2,father_window=0,
                             mode='visible',machine='')
    gray=ha.rgb1_to_gray(img)
    thres=ha.threshold(gray,100,200)

    ha.disp_obj(img,winhandle)
    ha.wait_seconds(5)
    ha.clear_window(winhandle)
    ha.disp_obj(thres,winhandle)
    ha.wait_seconds(5)





