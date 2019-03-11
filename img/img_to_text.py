

import requests
import pytesseract
# pytesseract is installed in the system, brew install for mac, 
# sudo apt-get install for linux
# windows, ... I supose you'll have an executable to install it...

try:
    from PIL import Image
except ImportError:
    import Image


def get_image(url):
    picture_request = requests.get(url)
    if picture_request.status_code == 200:
        with open("./image.jpg", 'wb') as f:
            f.write(picture_request.content)

    print(pytesseract.image_to_string(Image.open('./image.jpg')))

    return pytesseract.image_to_string(Image.open('./image.jpg'))

# my_url = 'http://pbs.twimg.com/media/D1YgbSdV4AECrFT.jpg:orig'

# get_image(my_url)

