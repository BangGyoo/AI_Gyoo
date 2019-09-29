import cv2

class Cam :
    def __init__(self,cam_index,width,height) :
         self.capture = cv2.VideoCapture(cam_index)        # Default index of notebook web cam is 0
         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

         self.waitTime = 1                   # must define integer number

    def display(self) :
        while True :
            ret, frame = self.capture.read()
            cv2.imshow("Notebook Cam",frame)
            if cv2.waitKey(self.waitTime) == 27 : break # 27 is esc key 

        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__" :
    cam = Cam(0,600,600)
    cam.display()
   
