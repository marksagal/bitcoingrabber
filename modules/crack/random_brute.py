from ..grab_list import GrabList
import libs.addrgen as addrgen
from concurrent.futures import ThreadPoolExecutor
import os


class RandomBrute:
    def __init__(self, **kw):
        self.__config = {}
        self.__config.update(kw)

    def console(self):
        while True:
            if self.__is_configured:
                self.__run_pool()
                print('running')
                break
            if self.__has_config('workers') is None:
                workers = raw_input('Number of workers (threads): ')
                if self.__set_config('workers', workers) is False:
                    print('Workers should be a Number')
                    continue
            if self.__has_config('target_path') is None:
                target_path = raw_input('Target path: ')
                if self.__set_config('target_path', target_path) is False:
                    print('Target path "{}" not found !!!'.format(os.path.abspath(target_path)))
                    continue
            if self.__has_config('target_list') is None:
                if self.__set_config('target_list', self.__target_list) is False:
                    print('Target Path: {}'.format(os.path.abspath(self.__has_config('target_path'))))
                    raw_input('Your target is empty. Hit [enter] to retry.')
                    continue
            if self.__has_config('beep') is None:
                beep = raw_input('Enable beep sound on success (Y/n): ')
                self.__set_config('beep', beep)

    def __run_pool(self):
        config = self.__config
        workers = config['workers']
        pool = ThreadPoolExecutor(max_workers=workers)
        for _ in range(workers):
            pool.submit(self.__run_brute)

    def __run_brute(self):
        public, private = cls.__random_address()
        config = self.__config
        if public in config['target_list']:
            self.__log(public, private)

    def __log(self, public, private):
        if self.__config['beep'] is True:
            try:
                import winsound
                winsound.Beep(2500, 500)
            except ImportError:  # Non-windows
                pass
        with open('addr.log', 'a') as fp:
            fp.write('{}::{}\n'.format(public, private))

    @staticmethod
    def __random_address():
        eckey = addrgen.gen_eckey(version=addrgen.get_version())
        version = addrgen.get_version()
        return addrgen.get_addr(eckey, version=version)

    @property
    def __target_list(self):
        gl = GrabList(self.__config.get('target_path'))
        return gl.list()

    @property
    def __is_configured(self):
        configs = ['workers', 'target_path', 'target_list', 'beep']
        return not (False in [config in self.__config for config in configs])

    def __has_config(self, key):
        return self.__config.get(key)

    def __set_config(self, key, value):
        if key == 'workers':
            try:
                self.__config.update(workers=int(value))
                return True
            except ValueError:
                return False
        if key == 'target_path':
            if not os.path.isdir(value):
                return False
            self.__config.update(target_path=value)
            return True
        if key == 'target_list':
            if not value:
                return False
            self.__config.update(target_list=value)
            return True
        if key == 'beep':
            if value.upper() == 'Y':
                self.__config.update(beep=True)
                return True
            self.__config.update(beep=False)
            return True


cls = RandomBrute
