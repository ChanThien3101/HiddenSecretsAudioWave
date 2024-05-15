
import os
import wave
import argparse

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()

af = args.audiofile

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def help():
    print("\033[92mExtract Your Secret Message and File Name from Audio Wave File.\033[0m")
    print('''usage: ExWave.py [-h] [-f AUDIOFILE]

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
        
        # Find the end of the padding
        pad_index = binary_data.find('0' * 8)
        
        # Extract the hidden message with file name
        hidden_message = binary_data[:pad_index]
        hidden_message = hidden_message[:-(len(hidden_message) % 8)]
        
        # Convert binary data to characters
        hidden_text = ''.join(chr(int(hidden_message[i:i+8], 2)) for i in range(0, len(hidden_message), 8))
        
        # Split hidden message into file name and content
        file_name, file_content = hidden_text.split("\n", 1)
        
        # Remove padding characters
        file_content = file_content.split('#')[0]
        
        # Write content to file with the same name as original file
        output_file = os.path.splitext(af)[0] + "_" + file_name
        with open(output_file, 'w') as file:
            file.write(file_content)
        
        print(f"Extracted file: {output_file}")
        
        # Close audio file
        waveaudio.close()
        
    except Exception as e:
        print(f"Something went wrong: {e}")

cls()
banner()
ex_msg(af)
