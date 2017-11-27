"""
@author: Mark Sagal <mark@sagal.biz>
@since: 2017-11-26
@license: MIT License <http://opensource.org/licenses/MIT>
"""
import os as _os


class GrabList:
    """
    GrabList module
    """
    __EXT = '.txt'  # Grab list file extension

    def __init__(self, __target_path):
        """
        Initialize Grab list
        @param __target_path: Target path
        @type __target_path: str
        """
        self.__path = __target_path

    @staticmethod
    def __open(*args, **kwargs):
        """
        Handles native file opener.
        @return: open | None - Returns None on failure
        """
        try:
            return open(*args, **kwargs)
        except Exception:
            return None

    @staticmethod
    def make_path(__path):
        """
        Makes path
        @param __path: Path to create
        @type __path: str
        @return: bool
        """
        try:
            _os.makedirs(__path)
            return True
        except Exception:
            return False

    @property
    def path(self):
        """
        Get path
        @return: None | str - Returns None if grab list path not exist
        """
        if _os.path.isdir(self.__path) is False:
            return None
        return self.__path

    @property
    def path_files(self):
        """
        Get path files
        @return: None | list - Returns None if no path or no path files
        """
        if self.path is None:
            return None
        ext_len = len(GrabList.__EXT)
        __files = _os.listdir(self.path)
        grab_lists = []
        for __file in __files:
            if __file[-ext_len::] != GrabList.__EXT:
                continue
            grab_lists.append(__file)
        if not grab_lists:
            return None
        return grab_lists

    def list(self, __file_name=None):
        """
        Returns a grab list
        @param __file_name: Optional parameter to pick selected list (default: None)
        @type __file_name: None | str
        @return: None | list - Returns all list in given path if no selected file
        """
        if self.path_files is None:
            return None
        if __file_name is not None and __file_name in self.path_files:
            return self.__get_list(__file_name)
        elif __file_name is None:
            data_list = []
            for __file in self.path_files:
                data_list += self.__get_list(__file)
            return data_list
        else:
            return []

    def __get_list(self, __file_name):
        """
        Parses a valid list as possible
        @param __file_name: List file name
        @type __file_name: str
        @return: list - Returns lines in list
        """
        absolute_path = '{}{}{}'.format(self.path, _os.sep, __file_name)
        try:
            __file = GrabList.__open(absolute_path, 'r')
            data_list = []
            for data in __file.readlines():
                data = data.strip()
                if not data:  # prevents blank lines
                    continue
                data_list.append(data)
            __file.close()
            return data_list
        except Exception:
            return []
