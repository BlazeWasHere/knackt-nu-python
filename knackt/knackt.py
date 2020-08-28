import requests

class Knackt:
    """If you get simplejson.errors.JSONDecodeError it means
    token is invalid, or invalid page in API
    """
    def __init__(self, token=None):
        """Requires an account token as usage for the API"""
        if token is None:
            raise KnacktError('Enter Your Account Token!')
        self.token = token
        self.base = 'https://api.knackt.nu/'
        self.headers = {
            'cookie': f'token={token}' 
        } 

    def categories(self):
        """Gets all categories"""
        URL = self.base + 'categories'
        r = requests.get(URL, headers=self.headers)
        if "name" in r.text:
            return r.json()
        elif not r.json()['success']:
            raise KnacktError(r.json()['error'])
        else:
            raise KnacktError('Invalid Key')

    def category_created(self, timestamp=None):
        """Gets All Combos in the Category Which was Made at That Time
        Timestamp should be in UNIX, and as a string
        """
        if timestamp is None:
            raise KnacktError('Enter a Timestamp!')
        URL = self.base + 'category/' + timestamp
        r = requests.get(URL, headers=self.headers)
        if "category" in r.text:
            return r.json()
        elif not r.json()['success']:
            raise KnacktError(r.json()['error'])
        else:
            raise KnacktError('Invalid Key')

    def download(self, combo_hash=None):
        """Downloads the combo according to combo_hash
        Currently Not Working
        """
        if combo_hash is None:
            raise KnacktError('Enter a Hash!')
        URL = self.base + 'download/' + combo_hash
        r = requests.get(URL, headers=self.headers)
        print(r.text)
        print(URL)
        if not r.json()['success']:
            raise KnacktError(r.json()['error'])
        else:
            raise KnacktError('Invalid Key')

class KnacktError(Exception):
    """API Errors, such as wrong token"""
    pass
