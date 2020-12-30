# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from typing import Any

import requests


class Knackt(object):
    """If you get simplejson.errors.JSONDecodeError it means
    token is invalid, or invalid page in API
    """

    def __init__(self, token: str) -> None:
        """Requires an account token as usage for the API"""

        self.token = token
        self.base = 'https://api.knackt.nu/'
        self.headers = {'cookie': f'token={token}'}

    def categories(self) -> Any:
        """Gets all categories"""

        URL = self.base + 'categories'
        r = requests.get(URL, headers=self.headers)

        if "name" in r.text:
            return r.json()
        elif not r.json()['success']:
            raise KnacktError(r.json()['error'])
        else:
            raise KnacktError('Invalid Key')

    def category_created(self, timestamp: str) -> Any:
        """Gets All Combos in the Category Which was Made at That Time
        Timestamp should be in UNIX, and as a string

        :param timestamp: timestamp in UNIX format as a string
        """

        URL = self.base + 'category/' + timestamp
        r = requests.get(URL, headers=self.headers)

        if "category" in r.text:
            return r.json()
        elif not r.json()['success']:
            raise KnacktError(r.json()['error'])
        else:
            raise KnacktError('Invalid Key')

    def download(self, combo_hash: str, name: str) -> bytes:
        """Downloads the combo according to combo_hash
        :param combo_hash: str, hash of combo
        :param name: name of the file
        """

        URL = self.base + 'download/' + combo_hash + '/' + name
        r = requests.get(URL, headers=self.headers)

        return r.content


class KnacktError(Exception):
    """API Errors, such as wrong token"""
    pass
