# Steganography
This is just basic encryption for hiding text messages inside simple images but obviously, this algorithm has its own limitations. 

## Limitations
* As of now this algorithm can only take 250 words or less than that
* It can't encrypt very large word in the encrypted image
* The ascii code for the letter should be from 0 to 255
* The program is not actually changing the image's metadata so if someone wish to send the encrypted image then send it as a document file, so that the file can retain its encrypted bits

## How to get started
* Clone the repo with `git clone` in git bash
```gitbash
git clone https://github.com/Shadow129-sys/Steganography.git
```
* move to "steganography" folder
```gitbash
cd Steganography
```
* install all the required lib using `pip` from `requirements.txt`
```gitbash
pip install -r requirements.txt
```
run `main.py` then enter the mode encrypt or decrypt, in `encrypt mode` we need to enter the coverfile name with extension but that file should be in the same directory, the program will take the message from `input.txt` and creates a encrypted file `encrypted.png` now just to test the program we can delete the cover file and input.txt and then run the `decrypt mode` in this mode we need to enter the encrypted filename with extension `encrypted.png` it will generate an output file `output.txt` with the decrypted text.
```terminal
$ python -u main.py
e - encryption
d - decryption
Choice : e
processing started.....
coverfile : photo.jpg
Encrypted file created...
process ended...
```
this will be printed if the program can encrypt the file or else it will show an error, in decrypt mode an `output.txt` file will be created with the decrypted text.
```terminal
$ python -u main.py
e - encryption
d - decryption
Choice : d
processing started.....
encrypted file : encrypted.png
Decrypted Text : bla bla bla
```
