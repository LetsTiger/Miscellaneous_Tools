from .base import BaseShortener

class ShorteningErrorException(Exception):
    def __init__(self, message=None):
        super().__init__(f'There was an error on trying to short the url: '
                         f'{message}')

class Shortener(BaseShortener):

    api_url = "http://tinyurl.com/api-create.php"

    def short_url(self, url):
        
        url = self.clean_url(url)
        api_response = self._get(self.api_url, params=dict(url=url))

        if api_response.ok:
            return api_response.text.strip()
        raise ShorteningErrorException(api_response.content)