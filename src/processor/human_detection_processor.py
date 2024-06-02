from ultralytics import YOLO
from ultralytics.engine.results import Results
import numpy as np
from typing import List, Dict
from src.input.config_input import ConfigInput



class HumanDetectionProcessor():
    '''detects humans on an image or frame'''
    def  __init__(self):
        config=ConfigInput('config.yaml')
        self.__yolo_model=YOLO(config.get_yolo_model())

    @staticmethod
    def remove_duplicates(dicts):
        seen = set()
        unique_dicts = []
        for d in dicts:
            # Convert dictionary to a tuple of sorted key-value pairs
            tuple_repr = tuple(sorted(d.items()))
            if tuple_repr not in seen:
                seen.add(tuple_repr)
                unique_dicts.append(d)
        return unique_dicts
    
    def  predict(self, frame) ->List[Results]:
        self.__results = self.__yolo_model.predict(frame, classes=[0], device='gpu')

        bounding_boxes=[]
        boxes=self.__results[0].boxes

        for box in boxes:
        # Extracting coordinates
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            coordinates=dict()
            coordinates['x']=int(x1)
            coordinates['y']=int(y1)
            coordinates['w']=int(x2)-int(x1)
            coordinates['h']=int(y2)-int(y1)
            bounding_boxes.append(coordinates)
        
        self.__bounding_boxes=bounding_boxes

        return self.__results
    
    def  get_bounding_boxes(self) -> List[Dict[str, int]]:
        '''returns list of detected human bounding boxes'''
        try:
            if self.__bounding_boxes is None:
                raise NameError('"HumanDetectionProcessor.predict" method should run before accessing to bounding boxes')
        except NameError as e:
            print(e)

        return self.__bounding_boxes


