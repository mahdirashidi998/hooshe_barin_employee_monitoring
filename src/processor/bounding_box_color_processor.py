from typing import List, Dict, Any
from src.input.config_input import ConfigInput




class BoundingBoxColorProcessor:
    def  __init__(self):
        self.config=ConfigInput('config.yaml')
        self.default_bbs=self.config.get_default_bounding_boxes()


    @staticmethod
    def  is_inside(bb1:Dict[str, int], bb2:Dict[str, int]) -> bool:
        x_left = max(bb1['x'], bb2['x'])
        y_top = max(bb1['y'], bb2['y'])
        x_right = min(bb1['x']+bb1['w'], bb2['x']+bb2['w'])
        y_bottom = min(bb1['y']+bb1['h'], bb2['y']+bb2['h'])

        if x_right < x_left or y_bottom < y_top:
            return 0.0

        # The intersection of two axis-aligned bounding boxes is always an
        # axis-aligned bounding box
        intersection_area = (x_right - x_left) * (y_bottom - y_top)

        # compute the area of both AABBs
        bb1_area = (bb1['w']) * (bb1['h'])
        bb2_area = (bb2['w']) * (bb2['h'])
        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area

        # iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
        iou = intersection_area / min(bb1_area, bb2_area)
        return iou > 0.5
    
    def  dye(self, detected_BBs: List[Dict[str, int]]) -> List[Dict[str, Any]]:
        bbx_with_colors=[]
        for detected_bb in detected_BBs:
            for default_bb in self.default_bbs:

                if self.is_inside(detected_bb, default_bb):
                    detected_bb['color']=self.config.get_is_inside_bounding_box_color()
                    bbx_with_colors.append(detected_bb)
                    break
                else:
                    detected_bb['color']=(0, 255, 255)
                    bbx_with_colors.append(detected_bb)
        for default_bb in self.default_bbs:
            bbx_with_colors.append(default_bb)
        return bbx_with_colors