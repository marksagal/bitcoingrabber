"""
@author: Mark Sagal <mark@sagal.biz>
@since: 2017-11-28
@license: MIT License <http://opensource.org/licenses/MIT>
"""
import requests as _req
from requests.exceptions import RequestException as _RequestException
try:  # Python 3
    from urllib.parse import urlencode as _urlencode
except ImportError:  # Python 2
    from urllib import urlencode as _urlencode


class Blockchain:
    """
    Blockchain Library
    """
    API_URL = 'https://blockchain.info'

    def __init__(self, params=None, **kw):
        """
        Initialize Blockchain
        @param params: URI parameter (default: None)
        @type params: dict
        @param address: accepts single address
        @type address: str
        @param addresses: accepts multiple address
        @type addresses: list
        @param key: Blockchain API Key
        @type key: str
        """
        self.__param = params
        self.__address = kw.get('address')
        self.__addresses = kw.get('addresses')
        self.__key = kw.get('key')

    @property
    def __params(self):
        """
        __params Getter
        @return: URI parameters
        @rtype: dict
        """
        params = {}
        if cls.__typeof(self.__param, dict) is True:
            params.update(self.__param)
        if cls.__typeof(self.__key, str):
            params['key'] = self.__key
        return params

    def __set_params(self, **params):
        """
        __params Setter
        @param params: Parameters to set
        """
        if cls.__typeof(self.__param, dict) is False:
            self.__param = {}
        if cls.__typeof(params, dict) is True:
            self.__param.update(params)

    @property
    def info(self):
        """
        Returns request info
        @return: (status_code, server response)
        @rtype: tuple(int, dict)
        """
        if cls.__typeof(self.__addresses, list) is True:  # Multiple address info
            if cls.__typeof(self.__address, str) is True:
                self.__addresses.append(self.__address)
            self.__set_params(active='|'.join(self.__addresses))
            return self.__get_info()
        elif cls.__typeof(self.__address, str) is True:  # Single address info
            return self.__get_info(multiaddr=False)
        else:
            return None

    def __get_info(self, multiaddr=True):
        """
        Decides between multi-address and single-address
        @param multiaddr: Set to false for single address
        @return: (status_code, server response)
        @rtype: tuple(int, dict)
        """
        parse = cls.__parse_response
        if multiaddr is True:
            return parse(cls.__get('{}/multiaddr'.format(cls.API_URL), self.__params))
        return parse(cls.__get('{}/rawaddr/{}'.format(cls.API_URL, self.__address), self.__params))

    @staticmethod
    def __parse_response(response):
        """
        Parses response
        @param response: (Status, Response)
        @type response: tuple(bool, Exception or dict)
        @return: (status_code, server response)
        @rtype: tuple(int, dict)
        """
        parse_error = 'Unable to parse server response with status code {}'
        if response[0] is False:
            return 4, {'error': 'Connection failed'}
        if response[1].status_code == 200:
            try:
                return 200, response[1].json()
            except AttributeError:
                return 200, {'error': parse_error.format(200)}
        return response[1].status_code, {'error': parse_error.format(response[1].status_code)}

    def address(self, address):
        """
        Sets address
        @param address: Single address
        @type address: str
        @raises TypeError: address should be a type of str
        @return: Returns class instance
        @rtype: Blockchain
        """
        if Blockchain.__typeof(address, str) is False:
            raise TypeError('address should be a type of str')
        self.__address = address
        return self

    def addresses(self, addresses):
        """
        Sets addresses
        @param addresses: Multiple addresses
        @type addresses: list
        @raises TypeError: addresses should be a type of list
        @return: Returns class instance
        @rtype: Blockchain
        """
        if Blockchain.__typeof(addresses, list) is False:
            raise TypeError('addresses should be a type of list')
        try:
            self.__addresses += addresses
        except TypeError:
            self.__addresses = addresses
        return self

    @classmethod
    def __get(cls, url, params=None):
        """
        Get request
        @param url: target url
        @param params: url params (get uri)
        @return: (True on success, URL Response)
        @rtype: (bool, Response)
        """
        try:
            if cls.__typeof(params, dict) is True:
                url += '?{}'.format(_urlencode(params))
                print(url)
            return True, _req.get(url)
        except _RequestException as err:
            return False, err

    @staticmethod
    def __typeof(data, valid_type):
        """
        Checks for address type
        @param data: data to check
        @type data: mixed
        @param valid_type: type to check
        @type valid_type: type
        @return: Returns false if not valid
        @rtype: bool
        """
        if type(data) is not valid_type or not data:
            return False
        return True


cls = Blockchain
