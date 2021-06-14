# steganography
This is just basic encryption for hiding text messages inside simple images but obviously, this algorithm has its own limitations. 

## Limitations
* As of now this algorithm can only take 250 words or less than that
* It can't encrypt very large word in the encrypted image
* The program is not actually changing the image's metadata so if someone wish to send the encrypted image then send it as a document file, so that the file can retain its encrypted bits

## How to get started
* Clone the repo with git clone in git bash
* move to "stegnography" folder
* install all the required lib using pip from requirements.txt
```gitbash
git clone https://github.com/Shadow129-sys/steganography.git
cd steganography
pip install -r requirements.txt
```
