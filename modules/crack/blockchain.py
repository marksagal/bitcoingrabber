from libs.addrgen import get_addr, gen_eckey
from concurrent.futures import ThreadPoolExecutor
from libs.blockchain import Blockchain as libBlockchain
import json


class Blockchain:
    def __init__(self, **kw):
        self.__chunks = kw.get('chunks')
        self.__threads = kw.get('threads')
        self.__passphrases = kw.get('passphrases')

    def run(self):
        pool = ThreadPoolExecutor(max_workers=self.threads)
        for passphrase in self.__gen_passphrases:
            pool.submit(self.__get_infos, self.__get_address(passphrase))
            # self.__get_infos(self.__get_address(passphrase))

    def __log(self, data, balance, fname):
        with open(fname, 'a') as f:
            f.write('{}::{}\n'.format(balance, json.dumps(data)))

    def __get_infos(self, addresses):
        # 1483228800
        address_list = [addr for addr in addresses]
        # address_list = ['1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v']
        bl = libBlockchain(params={'n': 1}, addresses=address_list, key='7318b580-aa3b-4c4b-9de7-42b9339fc1df')
        status_code, response = bl.info
        if status_code == 200:
            try:
                wallet = response.get('wallet')
                txs = response.get('txs')
                final_balance = wallet.get('final_balance')
                n_tx = wallet.get('n_tx')
                # print(wallet)
                if final_balance != 0:
                    print(final_balance)
                    self.__log(addresses, final_balance, 'withbalance.txt')
                    import winsound
                    winsound.Beep(2500, 1000)
                if len(txs) >= 1:
                    ftrans = txs[0]
                    ftime = ftrans['time']
                    if ftime >= 1483228800:
                        logid = '{}::{}'.format(ftime, n_tx)
                        print(logid)
                        self.__log(addresses, logid, '2017.txt')
                        import winsound
                        winsound.Beep(2500, 1000)
            except Exception:
                pass


        # for address in addresses:
        #     print(address)

    def __get_address(self, passphrases):
        # addresses = []
        # for passphrase in passphrases:
        #     public, private = get_addr(gen_eckey(passphrase=passphrase))
        #     addr = passphrase, public, private
        #     addresses.append(addr)
        # return addresses

        addresses = {}
        for passphrase in passphrases:
            public, private = get_addr(gen_eckey(passphrase=passphrase))
            addr = passphrase, private
            addresses.update({public: addr})
        return addresses

    @property
    def threads(self):
        if cls.__typeof(self.__threads, int) is False:
            return 1
        return self.__threads

    @threads.setter
    def threads(self, threads):
        if cls.__typeof(self.__threads, int) is False:
            raise TypeError('threads should be a type of int')
        self.__threads = threads

    @property
    def passphrases(self):
        if cls.__typeof(self.__passphrases, list) is False:
            return []
        return self.__passphrases

    @passphrases.setter
    def passphrases(self, passphrases):
        if cls.__typeof(passphrases, list) is True:
            self.__passphrases = passphrases
        self.__passphrases = []

    @property
    def __gen_passphrases(self):
        passphrases = self.passphrases[:]
        if cls.__typeof(self.__chunks, int) is True:
            chunks = self.__chunks
        else:
            chunks = len(passphrases)
        while len(passphrases) >= 1:
            yield passphrases[:chunks]
            del passphrases[:chunks]

    @staticmethod
    def __typeof(data, valid_type):
        """
        Checks for data type
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
