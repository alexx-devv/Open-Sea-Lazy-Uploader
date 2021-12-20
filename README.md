# The OpenSea Lazy Uploader

Upload NFTs automatically to OpenSea using their lazy mint function.

![LOU](https://user-images.githubusercontent.com/88213417/146703524-908f635c-0e20-4720-aede-f36827420c38.png)

## Quick note
* This program works only with FireFox at this moment. Don't try using any chrome based browser or anything else, it won't work.
* You need an empty OpenSea collection already created.
* I included the most recent MetaMask extension inside the 'metamask' directory, feel free to delete it and [download](https://addons.mozilla.org/en-US/firefox/addon/ether-metamask/) it again. You will need to open the link using FireFox, right click the download button and click "save as..".

## Installation

You will need [python3](https://www.python.org) installed.

Open a terminal inside the folder and run this command to install the needed package.
​
```bash
pip install -r requirements.txt
```
## Image and metadata files requirements
The name of the image and its metadata file MUST be the same, otherwise it won't work.

**Example**: 1.png AND 1.json

## Usage

1. Open **login-info.json** and write your MetaMask secret phrase and password.
2. Create a folder called "images" and one called "metadata" and paste your files there.
3. On your terminal type:

```bash
python main.py
```
4. Insert your collection link in the terminal and press 'Enter'
5. When MetaMask's pop up appears, select the address you want to use and press 'Enter'.

## Known issues
* Be aware that this is a workaround for uploading NFTs to OpenSea, the script can crash or get stuck at any given time because it depends on the availability/speed of their website and your internet connection, just close the browser and run the script again if you encounter any error.

* The script moves the uploaded images and metadata files to *uploaded/images* and *uploaded/metadata* so you can restart the script without modifying any file.

* The script only works with text properties. Numeric traits, ranks and dates are not supported yet. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Donations
Did you find this script useful? Did your project went to the moon? Buy me a pizza! 

ETH: 0x5a7d97C88e9dbBE1748Fb24D5fb7875745d7A152

## License
[MIT](https://choosealicense.com/licenses/mit/)
