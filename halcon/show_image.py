import halcon as ha
img=ha.read_image('./pcb.png')
wid,hei=ha.get_image_size(img)
print(wid[0],hei[0])

winhandle=ha.open_window(0,0,wid[0],hei[0],father_window=0,mode='visible',machine='')
ha.disp_obj(img,winhandle)
ha.wait_seconds(20)