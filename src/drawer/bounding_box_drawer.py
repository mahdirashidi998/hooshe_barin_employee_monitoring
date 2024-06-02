from typing import List, Dict, Any
import cv2
import numpy as np
class BoundingBoxDrawer:
    def  __init__(self):
        pass

    def  draw(self, frame, bounding_boxes:List[Dict[str, Any]]) -> np.ndarray:
        for bbx in bounding_boxes:
            cv2.rectangle(frame, (bbx['x'], bbx['y']), (bbx['x'] + bbx['w'], bbx['y'] + bbx['h']), bbx['color'], 1)
        return frame