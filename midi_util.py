# encoding: utf-8
"""
@author: Li.Z.F
@time: 2018/11/13 21:02

midi相关
"""
import os
import subprocess

def convertMidiToMp3():
    #将神经网络生成的midi文件转成mp3文件
    input_file  = './file/output.mid'
    output_file = './file/output.mp3'

    assert os.path.exists(input_file)

    print ("Converting %s to MP3" %input_file)

    #用timidty生成mp3
    command = 'timidity {} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {}'.format(input_file,output_file)

    subprocess.call(command,shell=True)
    print ("Converted Generated file id %s" %output_file)

if __name__ == '__main__':
    convertMidiToMp3()

