
# Hide your secret text and file name in wave audio file.

import os
import wave
import argparse

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message or file txt', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
args = parser.parse_args()

af = args.audiofile
secret_msg = args.secretmsg
output = args.outputfile

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def help():
    print("\033[92mHide Your Secret Message and File Name in Audio Wave File.\033[0m")
    print('''usage: HiddenWave.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message or file txt
  -o OUTPUTFILE Your output file path and name''')

def banner():
    print('''
                         \033[1;91mHide secrets in audio\033[0m
                         \033[92mDinh Huu Duc 20NS\033[0m
                         \033[93mNguyen Viet Tan 20NS\033[0m''')

def get_secret_message(input_str):
    # Check if input_str is a file path
    if os.path.isfile(input_str):
        with open(input_str, 'r') as file:
            # Return file name + file content
            return os.path.basename(input_str) + "\n" + file.read()
    else:
        return input_str

def em_audio(af, secret_msg, output):
    if not (af and secret_msg and output):
        help()
        return
    
    try:
        print("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        
        # Get secret message with file name
        secret_msg = get_secret_message(secret_msg)
        
        # Add padding to secret message
        secret_msg = secret_msg + int((len(frame_bytes) - (len(secret_msg) * 8 * 8)) / 8) * '#'
        
        # Convert secret message to binary
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in secret_msg])))
        
        # Embed secret message into audio frames
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        
        # Write modified frames to output file
        frame_modified = bytes(frame_bytes)
        with wave.open(output, 'wb') as fd:
            fd.setparams(waveaudio.getparams())
            fd.writeframes(frame_modified)
        
        # Close audio file
        waveaudio.close()
        
        print("Done...")
        
    except Exception as e:
        print(f"Something went wrong: {e}")

cls()
banner()
em_audio(af, secret_msg, output)
