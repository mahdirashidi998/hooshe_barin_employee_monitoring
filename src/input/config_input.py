import yaml
from typing import Dict, Any
from src.text_config import TextConfig

class ConfigInput:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self.__config = yaml.safe_load(file)
    
    def get_video_input(self):
        return self.__config['video_input']
    
    def get_yolo_model(self):
        return self.__config['yolo_model_path']
    
    def get_default_bounding_boxes(self):
        bbs= self.__config['default_bounding_boxes']
        for bb in bbs:
            bb['color']=tuple(bb['color'])

        return tuple(self.__config['default_bounding_boxes'])
    
    def get_face_emotion_model_path(self):
        return self.__config['face_emotion_model_path']
    
    def get_image_path(self):
        return self.__config['image_path']
    
    def get_counter_text_config(self)->TextConfig:
        text_config= TextConfig()
        config= self.__config['counter_text']

        text_config.position=config['position']
        text_config.font=config['font']
        text_config.font_scale=config['font_scale']
        text_config.color=config['color']
        text_config.thickness=config['thickness']

        return text_config

    def get_is_inside_bounding_box_color(self):
        return tuple(self.__config['is_inside_bounding_box_color'])
    
    def get_not_inside_bounding_box_color(self):
        return tuple(self.__config['not_inside_bounding_box_color'])

    def get_stream_input_link(self):
        return self.__config['stream_input_link']
    


