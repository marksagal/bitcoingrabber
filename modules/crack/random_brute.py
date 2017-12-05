from ..grab_list import GrabList
# from concurrent.futures import ThreadPoolExecutor
import os


class RandomBrute:
    def __init__(self, **kw):
        self.__config = {}
        self.__config.update(kw)

    def console(self):
        while True:
            if self.__is_configured:
                print('running the pool')
                break
            if self.__has_config('workers') is None:
                workers = raw_input('Number of workers (threads): ')
                if self.__set_config('workers', workers) is False:
                    print('Workers should be a Number')
                    continue
            if self.__has_config('target_path') is None:
                target_path = raw_input('Target path: ')
                if self.__set_config('target_path', target_path) is False:
                    print('Target path not found !!!')
                    continue
            if self.__has_config('target_list') is None:
                if self.__set_config('target_list', self.__target_list) is False:
                    raw_input('Your target is empty. Hit [enter] to retry.')
                    continue
        print(self.__config, self.__target_list)

    @property
    def __target_list(self):
        gl = GrabList(self.__config.get('target_path'))
        return gl.list()

    @property
    def __is_configured(self):
        configs = ['workers', 'target_path', 'target_list']
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
