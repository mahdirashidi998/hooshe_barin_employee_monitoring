import cv2
from src.input.config_input import ConfigInput

class VideoInput():
    def  __init__(self):
        config=ConfigInput('config.yaml')
        self.__video_path=config.get_video_input()

    def get_frames(self):
        '''returns list of frames as numpy arrays'''

        cap = cv2.VideoCapture(self.__video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            

            yield frame
        cap.release()

    