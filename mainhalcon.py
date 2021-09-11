import halcon as ha




if __name__=='__main__':
    img=ha.read_image('pcb.png')
    region=ha.threshold(img,0,122)
    num=ha.count_obj(ha.connection(region))
    print(f'Number of regions: {num}')

