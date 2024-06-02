import sys
import os
import torch
from src.output.local_video_output import LocalVideoOutput

torch.cuda.set_device(0) # Set to your desired GPU number
# Add the root project directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

displayer=LocalVideoOutput()

displayer.display()




