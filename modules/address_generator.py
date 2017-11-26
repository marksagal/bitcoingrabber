"""
@author: Mark Sagal <mark@sagal.biz>
@since: 2017-11-26
@license: MIT Licence <http://opensource.org/licenses/MIT>
"""
import libs.addrgen as _addrgen


class AddressGenerator:
    """
    Bitcoin Address Generator
    """
    def __init__(self, *args, **kwargs):
        """
        Bitcoin Address generator
        @param compressed: Set True to compress address (default: False)
        @type compressed: bool
        @param passphrase: eckey's passphrase (default: None)
        @type passphrase: str
        @param secret: eckey's secret (default: None)
        @type secret: str
        @param pkey: address's private key
        @type pkey: str
        @param: version (default: 0)
        @type version: int
        """
        self.__args = args
        self.__kwargs = kwargs

    @property
    def eckey(self):
        """
        Returns _addrgen.KEY instance
        @return: _addrgen.KEY
        """
        return _addrgen.gen_eckey(*self.__args, **self.__kwargs)

    @property
    def version(self):
        """
        ECKey version
        @return: int (default: 0)
        """
        if type(self.__kwargs.get('version')) is int:
            return self.__kwargs.get('version')
        return 0

    @property
    def address(self):
        """
        Returns public / private key in tuple
        @return: {public_key}, {private_key}
        """
        return _addrgen.get_addr(self.eckey, self.version)
