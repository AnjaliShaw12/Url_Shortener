import string
import random

class URLShortener:
    def __init__(self):
        self.short_to_long={}
        self.long_to_short={}
        self.allowed_chars=string.ascii_letters+string.digits
        self.base_url="https://sample_urlShortener.com/"

    def shorten_url(self,long_url):
        if long_url in self.long_to_short:
            return self.base_url+self.long_to_short[long_url]
        short_code=self.generate_short_code()
        short_url=self.base_url+short_code

        self.short_to_long[short_code]=long_url
        self.long_to_short[long_url]=short_code

        return short_url

    def generate_short_code(self):
        while True:
            short_code=''.join(random.choices(self.allowed_chars,k=6))
            if short_code not in self.short_to_long:
                return short_code

url_shortener=URLShortener()
while True:
    long_url=input("Enter a url:")
    if long_url=='N':
        break
    short_url=url_shortener.shorten_url(long_url)
    print("Shortened URL :",short_url)