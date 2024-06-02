class TextConfig:
    def __init__(self, position=(0, 0, 0), font=0, font_scale=1, color=(0, 0, 255), thickness=2):
        self.position : tuple = position
        self.font : int = font
        self.font_scale : int = font_scale
        self.color : tuple = color # color in BGR
        self.thickness : int = thickness