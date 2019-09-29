import cv2
import os

#image = cv2.imread('flower.jpg', cv2.IMREAD_COLOR)
#b , g , r = cv2.split(image)
#image2 = cv2.merge([r,g,b])

PATH = os.getenv("AI_Gyoo")
PATH += "\\opencv\\"

class Img :
    def __init__(self,name) :                   # ignore __new__ function
        print(PATH + name) 
        image = cv2.imread(PATH + name,cv2.IMREAD_COLOR)
        self.height , self.width, self.channels = image.shape
        self.b, self.g, self.r = cv2.split(image)
    
    def replace_RGB(self) :
        return cv2.merge([self.r,self.g,self.b])

    def get_size(self) :
        return self.height , self.width, self.channels

if __name__ == "__main__" :
    from matplotlib import pyplot as plt

    flower = Img('flower.jpg')
    image2 = flower.replace_RGB() 

    HEIGHT, WIDTH, CH = flower.get_size()

    plt.imshow(image2)
    plt.xticks(range(0,HEIGHT,50))
    plt.yticks(range(0,WIDTH,50))
    plt.show()

