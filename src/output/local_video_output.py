from src.drawer.bounding_box_drawer import BoundingBoxDrawer
from src.processor.wrapper_processor import WrapperProcessor
from src.input.video_input import VideoInput
from src.input.config_input import ConfigInput
from src.models import Counter

import cv2
class LocalVideoOutput:
    def  __init__(self):
        self.wrapper=WrapperProcessor()
        self.video_input=VideoInput()
        self.config=ConfigInput()
        self.boundingboxDrawerInstance = BoundingBoxDrawer()

    def display(self):
        text_config=self.config.get_counter_text_config()
        people_counter=Counter()
        init_colors = None

        for frame in self.video_input.get_frames():
            processed_frame=self.wrapper.process(frame)
            people_counter.count_people(init_colors, processed_frame.get_colored_bounding_boxes())
            init_colors= processed_frame.get_colored_bounding_boxes()
            self.boundingboxDrawerInstance.draw(frame, processed_frame.get_colored_bounding_boxes())
            cv2.putText(frame, f"People passed: {people_counter.get_value()}", 
                        text_config.position, text_config.font, 
                        text_config.font_scale, text_config.color, 
                        text_config.thickness)


            cv2.imshow("YOLOv8 Tracking", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break



