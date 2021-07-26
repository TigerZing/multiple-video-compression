# Import common packages
import glob
from os import system
import os
import os.path as osp
import tqdm
import cv2
from Sequence import Sequence

# Check if folder exists, if not create it
def checkExist(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
# Extract all information of sequence
def extractInfo(seqPath):
    fullName = osp.basename(seqPath).split(".")[0]
    name_only = fullName.split("__")[0]
    size = fullName.split("__")[1]
    numFrames = fullName.split("__")[2]
    width = size.split('x')[0]
    height = size.split('x')[1]
    return fullName, int(width), int(height), int(numFrames)

# IO sequence
def prepareSeqs(SeqPth, args):
    fullName, width, height, numFrames = extractInfo(SeqPth)
    seq = Sequence(SeqPth, numFrames, args.format, [width,height])
    seq.showInfo()
    return seq
