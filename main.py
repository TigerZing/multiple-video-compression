# common packages
import numpy as np 
import os
import os.path as osp
from os import system
import sys
import shutil
import glob
import argparse
from Sequence_ import Sequence

#[Notice ! sequence has format "name__widthxheight__numFrame.yuv"]

# Read configuration file
def read_config(parser):
    parser.add_argument('--input_path', type=str, default="/mnt/exhdd1/exhdd1_hont/DATASET/Original/Train/720p",help='feed the input_folder path')
    parser.add_argument('--output_path', type=str,default="/mnt/exhdd1/exhdd1_hont/DATASET/Multiple_video_compression/1080p",  help='feed the output_folder path' )
    parser.add_argument('--format', type=str, default="420", help='420 | 444')
    parser.add_argument('--QP', type=str, default=42, help='Quantization parameter')
    parser.add_argument('--encoder_path', type=str,default="/mnt/exhdd1/exhdd1_hont/DATASET/Multiple_video_compression/EncoderAppStatic",  help='Encoder path' )
    parser.add_argument('--configuration_file', type=str,default="/mnt/exhdd1/exhdd1_hont/DATASET/Multiple_video_compression/encoder_lowdelay_P_vtm.cfg",  help='config profile path' )
    parser.add_argument('--sequence_config_template_file', type=str,default="template.cfg",  help='config files path' )
    return parser.parse_args()

# Extract all information of sequence
def extract_info(seqPath):
    fullName = osp.basename(seqPath).split(".")[0]
    name_only = fullName.split("__")[0]
    size = fullName.split("__")[1]
    numFrames = fullName.split("__")[2]
    width = size.split('x')[0]
    height = size.split('x')[1]
    return fullName, int(width), int(height), int(numFrames)


def tmux(command):
    system('tmux %s' % command)
    
def tmux_shell(command):
    tmux('send-keys "%s" "C-m"' % command)
    
def create_panel( seq, SeqPth, args):
    # create n_window
    cmd = "{} -i {} -c {} -c {} -q {}".format(args.encoder_path, SeqPth, args.configuration_file, osp.join(osp.join(args.output_path,"config"),seq.name+".cfg"), args.QP)
    tmux_shell(cmd)
    
def compress_sequence(sequence, args, idx):
    tmux('new-window')
    tmux('select-window -t '+str(idx+1))
    create_panel( sequence, sequence.path, args)

# Generate Cfg file
def generateCfg(seq, args):
    templateFile = open(args.sequence_config_template_file,"r")
    templateContent = templateFile.read()
    templateFile.close()
    newContent = templateContent.replace("namestreamfile",osp.join(osp.join(args.output_path, "video"),seq.name))
    newContent = newContent.replace("outputfile",osp.join(osp.join(args.output_path,"video"),seq.name))
    newContent = newContent.replace("inputfile.yuv",seq.path)
    newContent = newContent.replace("widthfile",str(seq.width))
    newContent = newContent.replace("heightfile",str(seq.height))
    newContent = newContent.replace("nframefile",str(seq.totalFrames))
    newContent = newContent.replace("SummaryOutpath",osp.join(osp.join(args.output_path, "info"),"SummaryOut_"+seq.name))
    newContent = newContent.replace("SummaryPicpath",osp.join(osp.join(args.output_path, "info"),"SummaryPic_"+seq.name))
    newContent = newContent.replace("fileInfo",osp.join(args.output_path+"info",seq.name))
    newFile = open(osp.join(osp.join(args.output_path,"config"),seq.name+".cfg"),"w")
    newFile.write(newContent)
    newFile.close()
    
def main():
    # read configurations
    parser = argparse.ArgumentParser()
    read_config(parser)
    args = parser.parse_args()
    
    # IO sequences
    list_seqs_path = glob.glob(osp.join(args.input_path,"*.yuv"))
    
    # Create folders
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)

    else:
        shutil.rmtree(osp.join(args.output_path,"video"), ignore_errors=True)
        shutil.rmtree(osp.join(args.output_path,"config"), ignore_errors=True)
        shutil.rmtree(osp.join(args.output_path,"info"), ignore_errors=True)
    os.makedirs(osp.join(args.output_path,"video"))
    os.makedirs(osp.join(args.output_path,"config"))
    os.makedirs(osp.join(args.output_path,"info"))

    # {generate cfg} & {compress sequence}
    for idx, seq_path in enumerate(list_seqs_path):
        fullName, width, height, numFrames = extract_info(seq_path)
        seq = Sequence(seq_path, numFrames, args.format, [width,height])
        #seq.showInfo()
        generateCfg(seq, args)
        compress_sequence(seq, args, idx)
        
if __name__=="__main__":
    main()