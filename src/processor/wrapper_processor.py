from src.input.video_input import VideoInput
from src.processor.human_detection_processor import HumanDetectionProcessor
from src.processor.bounding_box_color_processor import BoundingBoxColorProcessor
from src.models import ProcessedFrame

class WrapperProcessor:
    def  __init__(self):
        self.videoInputInstance = VideoInput()
        self.detectionProcessorInstance = HumanDetectionProcessor()
        self.colorProcessorInstance = BoundingBoxColorProcessor()
    

    def  process(self, frame):
        self.detectionProcessorInstance.predict(frame)
        detected_bbs=self.detectionProcessorInstance.get_bounding_boxes()
        colored_bbxes= self.detectionProcessorInstance.remove_duplicates(self.colorProcessorInstance.dye(detected_bbs))
        processedFrameInstance= ProcessedFrame(frame, colored_bbxes)
        return processedFrameInstance
