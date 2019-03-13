import requests
import pytesseract
# pytesseract is installed in the system, brew install for mac, 
# sudo apt-get install for linux
# windows, ... I supose you'll have an executable to install it...
try:
    from PIL import Image
except ImportError:
    import Image

def translate_image(path):    
    return pytesseract.image_to_string(Image.open(path))


