import os
import os.path as osp

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