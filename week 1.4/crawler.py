import urllib.request
import ssl
import re
from bs4 import BeautifulSoup


class WebCrawler:
    def __init__(self):
        self.url = "https://sport050.nl/sportaanbieders/alle-aanbieders/"
        self.pointer = 0
        self.sub_urls = []

    # Good observeration that this method could be made static
    @staticmethod
    def hack_ssl():
        """Ignores the certificate errors"""
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def open_url(self, url):
        """Reads URL file as a big string and cleans the HTML file to make it more readable.
        Input: URL
        Output: BeautifulSoup object
        """
        ctx = self.hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    # Good observation that all these methods could be made static. 
    # It would even be better is you hade refactored them into their own scope.
    @staticmethod
    def read_hrefs(soup):
        """Get a list of anchor tags from the BeautifulSoup object, get the href keys, and print them.
        Input: BeautifulSoup object
        Output: List of anchor tags
        """
        reflist = []
        tags = soup('a')
        for tag in tags:
            reflist.append(tag)
        return reflist

    @staticmethod
    def read_li(soup):
        lilist = []
        tags = soup('li')
        for tag in tags:
            lilist.append(tag)
        return lilist

    @staticmethod
    def get_phone(info):
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [s for s in filter(lambda x: 'Telefoon' in str(x), info)]
        try:
            phone = str(phone[0])
        except:
            phone = [s for s in filter(lambda x: re.findall(reg, str(x)), info)]
            try:
                phone = str(phone[0])
            except:
                phone = ""
        return phone.replace('Facebook', '').replace('Telefoon:', '')

    @staticmethod
    def get_email(soup):
        try:
            email = [s for s in filter(lambda x: '@' in str(x), soup)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email = bs.find('a').attrs['href'].replace('mailto:', '')
        except:
            email = ""
        return email

    @staticmethod
    def remove_html_tags(text):
        """Remove HTML tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def fetch_sidebar(self, soup):
        """Read HTML file as a big string and cleans the HTML file to make it more readable.
        Input: HTML
        Output: Tables
        """
        sidebar = soup.findAll(attrs={'class': 'sidebar'})
        return sidebar[0]

    @staticmethod
    def extract(url):
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text

    def crawl_site(self):
        print('Fetching URLs')
        s = self.open_url(self.url)
        reflist = self.read_hrefs(s)

        print('Getting sub-URLs')
        self.sub_urls = [s for s in filter(lambda x: '<a href="/sportaanbieders' in str(x), reflist)]
        self.sub_urls = self.sub_urls[3:]

    #Good
    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer < len(self.sub_urls):
            sub = self.extract(self.sub_urls[self.pointer])
            site = self.url[:-16] + sub
            soup = self.open_url(site)
            info = self.fetch_sidebar(soup)
            info = self.read_li(info)
            phone = self.get_phone(info)
            phone = self.remove_html_tags(phone).strip()
            email = self.get_email(info)
            email = self.remove_html_tags(email).replace("/", "")
            self.pointer += 1
            # Should this not be `yield` instead of `return`?
            # Now you delegate the administration of the state of the 
            # iterator to the using client.
            return f'{site} ; {phone} ; {email}'
        else:
            raise StopIteration


