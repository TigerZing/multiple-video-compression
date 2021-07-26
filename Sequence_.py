import os
import os.path as osp
from imageio import imread
from imageio import imsave
import getopt
import math
import numpy
import os
import PIL
import PIL.Image as Image
import random
import shutil
import sys
import tempfile
import time
import os.path as osp
import numpy as np
from numpy import zeros, newaxis
from tqdm import tqdm
import sys
import time
import io
import time
import cv2

class Sequence:
    "Description of uncompressed sequence"
    def __init__(self, path, totalFrames, formatVideo, res):
        super().__init__()
        self.path = str(path)
        self.name = str(osp.basename(osp.splitext(path)[0]))
        self.totalFrames = int(totalFrames)
        self.formatVideo = str(formatVideo)
        self.width = int(res[0])
        self.height = int(res[1])
        
    def showInfo(self):
        print("# Name  {}".format(self.name))
        print("  Path   {}".format(self.path))
        print("  Total  {} frames".format(self.totalFrames))
        print("  Format {}".format(self.formatVideo))
        print("  Size   {}x{}".format(self.width,self.height))