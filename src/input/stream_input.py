import cv2
from src.input.config_input import ConfigInput

class StreamInput():
    def  __init__(self):
        config=ConfigInput('config.yaml')
        self.__stream_link=config.get_stream_input_link()

    def get_frames(self):
        '''returns list of frames as numpy arrays'''

        cap = cv2.VideoCapture(self.__stream_link)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            

            yield frame
        cap.release()