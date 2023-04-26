import requests

from logging import getLogger

_logger = getLogger(__name__)

def get_artwork_by_title_artist(artist, title):
    _logger.info(f"Fetching artwork for {artist} - {title}")

    url = f"https://api.deezer.com/search?q=artist:'{artist}' track:'{title}'"

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        if data['total'] > 0:
            img_url = data['data'][0]['album']['cover_medium']
        else:
            return False

        if img_url:
            image_request = requests.get(img_url)

            with open('/tmp/radioimg.jpg', 'wb') as f:
                f.write(image_request.content)

            return True
        else:
            _logger.info("Could not fetch artwork")
    else:
        _logger.info(f"Error connecting to Deezer API, status code: {r.status_code}")

        return False