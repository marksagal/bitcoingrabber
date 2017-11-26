# from modules.address_generator import AddressGenerator
#
# address = AddressGenerator()
# adresses = [address.address[0] for _ in range(3)]
# print(adresses)
# print('*' * 3)
# addresses = [
#     '1cMh228HTCiwS8ZsaakH8A8wze1JR5ZsP',
#     '1NZUP3JAc9JkmbvmoTv7nVgZGtyJjirKV1',
#     '1CUNEBjYrCn2y1SdiUMohaKUi4wpP326Lb'
# ]
# import requests
# string_addresses = '|'.join(addresses)
# # print(string_addresses)
# req = requests.get('https://blockchain.info/multiaddr?active={}'.format(string_addresses))
# resp = req.json()
#
# for key in resp:
#     print(key)
# print('*' * 8)
# print(len(resp['txs']))

from modules import grabber as gb, grab_list as gl, address_generator as ag
import os as _os


class Main:
    ACTIONS = {
        '1': 'blockchain_conf.json',
        '2': 'target_conf.json'
    }

    def __init__(self, __action):
        self.__action = __action

    @classmethod
    def check_config(cls, __answer):
        __conf_file = cls.ACTIONS.get(__answer)
        print(__conf_file)


if __name__ == '__main__':
    print('1 - Grab from BlockChain | 2 - Grab from Target list')
    action = raw_input('Answer: ')
    main = Main.check_config(action)

