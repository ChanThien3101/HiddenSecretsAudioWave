

import os
import wave
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile

def cls():
    os.system("clear")

def help():
    print("\033[92mExtract Your Secret Message from Audio Wave File.\033[0m")
    print ('''usage: ExWave.py [-h] [-f AUDIOFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File''')

def banner():
    print('''
                         \033[1;91mHide secrets in audio\033[0m
                         \033[92mDinh Huu Duc 20NS\033[0m
                         \033[93mNguyen Viet Tan 20NS\033[0m''')

def ex_msg(af):
    if not af:
        help()
        return
    
    try:
        print("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        
        # Extract hidden message
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        binary_data = "".join(map(str, extracted))
        
       
        
        # Convert binary data to characters
        hidden_text = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        
        # Split hidden message into file name and content
        split_index = hidden_text.find("\n")
        file_name = os.path.splitext(af)[0] + "_" + hidden_text[:split_index]
        message_content = hidden_text[split_index + 1:].split("###")[0]
        
        # Write content to file with the same name as original file
        with open(file_name, 'w') as file:
            file.write(message_content)
        
        print(f"Extracted file: {file_name}")
        print(f"Extracted message: {message_content}")
        
        # Close audio file
        waveaudio.close()
        
    except Exception as e:
        print(f"Something went wrong: {e}")

cls()
banner()
ex_msg(af)
