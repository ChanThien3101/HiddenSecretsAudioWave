# HiddenWave
Embedding secret messages in wave audio file

# What is HiddenWave
Hiddenwave is a python based program for simple audio steganography. You can hide your secret text messages in wave audio file. you can play this audio in any media player and secretly share your private message with any one.

# Requirements
<p>This tool require python3</p>

## Installation

```
https://github.com/ChanThien3101/HiddenSecretsAudioWave.git
cd HiddenSecretsAudioWave
```
## Usage
<p>Hiddenwave have two python scripts. </p>
<ul>
<li><b>HiddenWave.py :</b> for hide secret information.</li>
<li><b>ExWave.py :</b> for extract secret information for wave audio file.</li>
</ul>

### Hide Secret Information in Audio file

```
python HiddenWave.py -f ThangNamKhongQuenRemix.wav -m "Secret Msg" -o Output.wav
python HiddenWave.py -f ThangNamKhongQuenRemix.wav -m TestFile -o Output.wav
```
### Extract Secret Information from Audio file

```
python ExWave.py -f Output.wav
```


