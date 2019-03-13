from twitter import twitter_client
from ocr import ocr_client
from img_downloader import download

PATH = './image.jpg'

img_url = twitter_client.get_image_url()
download.image_to_disk(img_url, PATH)

text_to_tweet = ocr_client.translate_image(PATH)

print(text_to_tweet)
