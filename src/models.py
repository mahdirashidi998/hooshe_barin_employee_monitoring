from typing import Dict,List, Any
import numpy as np
from src.input.config_input import ConfigInput

class ProcessedFrame:
    def  __init__(self, frame: np.ndarray, colored_bbs : List[Dict[str, Any]]):
        self.__frame = frame
        self.__colored_bbs=colored_bbs
    
    def get_frame(self):
        return self.__frame
    
    def get_colored_bounding_boxes(self):
        return self.__colored_bbs
    
class Counter:
    def __init__(self, initiation_value=0):
        self.__value=initiation_value
        self.config=ConfigInput()

    def get_value(self):
        return self.__value

    def count(self,count_value=1):
        self.__value=self.__value+count_value
        return self.__value
    
    def reset(self, initiation_value=0):
        self.__value=initiation_value
        return self.__value
    
    def  count_people(self, not_processed_bbs, processed_bbs):
        if( not_processed_bbs is None or len(not_processed_bbs)<=len(self.config.get_default_bounding_boxes()) or len(processed_bbs)!=len(not_processed_bbs) ):
            return self.get_value()

        not_processed_bbs = not_processed_bbs[0:len(not_processed_bbs)-len(self.config.get_default_bounding_boxes())]
        processed_bbs = processed_bbs[0:len(processed_bbs)-len(self.config.get_default_bounding_boxes())]

        not_processed_bbs = sorted(not_processed_bbs, key=lambda x: x['x'])
        processed_bbs = sorted(processed_bbs, key=lambda x: x['x'])
        for index, bb in enumerate(processed_bbs):
            if (not_processed_bbs[index]['color']== self.config.get_is_inside_bounding_box_color() ):
                pass

            elif (bb['color'] != not_processed_bbs[index]['color'] and 
                bb['color'] == self.config.get_is_inside_bounding_box_color()):
                self.count()
        return self.get_value()


        


    
    