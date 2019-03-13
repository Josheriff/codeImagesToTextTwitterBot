import requests

def image_to_disk(url, path):
    picture_request = requests.get(url)
    if picture_request.status_code == 200:
        with open(path, 'wb') as f:
            f.write(picture_request.content)