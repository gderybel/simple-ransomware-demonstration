# Simple ransomware demonstration

This tool shows you how a simple ransomware could affect your workstations.

## Install requirements
`pip install -r requirements.txt`

## Usage
```
usage: main.py [-h] -f FOLDER [-r] [-k KEY] [-y]

This tool encrypt or decrypt files.

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        which folder should be encrypted/decrypted (default: None)
  -r, --recursive       tells if the folder selected should be encrypted recursively (default: False)
  -k KEY, --key KEY     specified decryption key, if given, decryption mode is activated, other wise it will be encryption (default: None)
  -y, --consent         if selected, user won't be prompted for consent before encryption (default: False)
```
