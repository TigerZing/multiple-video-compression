This script is used to compress multiple videos at the same time
1. Clone this repository:
```
$ git clone https://github.com/TigerZing/multiple_video_compression.git
$ cd multiple_video_compression
```
2. Prepare some inputs :
- The video must have the format "name__widthxheight__numFrame.yuv"
- the overall template configuration for sequences (e.g: template.cfg))
- the profile configuration for sequences (e.g: encoder_lowdelay_P_vtm.cfg)
- the Encoder file (e.g: EncoderAppStatic)
3. How to run
* Create a new-session in Tmux
```
$ tmux new-session -s <your-session's-name>
```
* Adjust some input parameters: 
```
input_path                      : feed the input_folder path
output_path                     : feed the output_folder path
format                          : '420 | 444'
QP                              : Quantization parameter
encoder_path                    : Encoder file path
configuration_file              : profile config file_path
sequence_config_template_file   : config file_path for sequence
```
* Start to compress videos
```
$ python main.py
```