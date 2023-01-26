import matplotlib.pyplot as plt
from image import imageProcessing



def main():

    #设置图片路径
    image_path = 'sakura.jpg'
    #读取图片
    origin_image = plt.imread(image_path)
    print("original image size: ", origin_image.shape)

    inst_img_list = []
    list_th = []
    list_ziprate = []
    for i in range(1,7):
        inst_img = imageProcessing(origin_image, 0.03*i)
        inst_img.zip_image_by_svd()

        inst_img_list.append(inst_img)

    plt.figure(figsize= (6, 8))
    plt.title("按照奇异值个数选取k值")
    #sp = plt.subplot(3,3,1)
    #sp.axis('off')
    #plt.title("Origin Image")
    #plt.imshow(origin_image)

    for i in range(len(inst_img_list)):
        sp = plt.subplot(3,2,i+1)
        sp.axis('off')
        plt.title("th = {}    zip rate = {}".format(round(inst_img_list[i].reserve_rate, 2) , round(inst_img_list[i].zip_rate, 2)))
        #plt.title("Reserve Rate : {}".format(inst_img_list[i].reserve_rate, '.2f'))
        plt.imshow(inst_img_list[i].result)
        list_th.append(round(inst_img_list[i].reserve_rate, 2))
        list_ziprate.append(round(inst_img_list[i].zip_rate, 2))
    plt.figure()
    plt.plot(list_th,list_ziprate)
    #plt.title("zip rate VS th")
    plt.ylabel("zip rate")
    plt.xlabel("th")


    plt.show()
if __name__ == "__main__":
    main()
