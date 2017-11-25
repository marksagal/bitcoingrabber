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

    def __init__(self, list_path):
        """
        Initialize Grab list
        @param list_path:
        """
        self.__path = list_path

    @staticmethod
    def __open(*args, **kwargs):
        """
        Handles native file opener.
        @param args: Arguments
        @param kwargs: Named Arguments
        @return: Returns None on failure
        """
        try:
            return open(*args, **kwargs)
        except Exception:
            return None

    @staticmethod
    def make_path(path):
        try:
            _os.makedirs(path)
            return True
        except Exception:
            return False

    @property
    def path(self):
        """
        Get path
        @return: Returns None if grab list path not exist
        """
        if _os.path.isdir(self.__path) is False:
            return None
        return self.__path

    @property
    def path_files(self):
        """
        Get path files
        @return: Returns None if no path or no path files
        """
        if self.path is None:
            return None
        ext_len = len(GrabList.__EXT)
        files = _os.listdir(self.path)
        grab_lists = []
        for file in files:
            if file[-ext_len::] != GrabList.__EXT:
                continue
            grab_lists.append(file)
        if not grab_lists:
            return None
        return grab_lists

    def list(self, file_name=None):
        """
        Returns a grab list
        @param file_name: Optional parameter to pick selected list (default: None)
        @return: Returns all list in given path if no selected file
        """
        if self.path_files is None:
            return None
        if file_name is not None and file_name in self.path_files:
            return self.__get_list(file_name)
        elif file_name is None:
            data_list = []
            for file in self.path_files:
                data_list += self.__get_list(file)
            return data_list
        else:
            return []

    def __get_list(self, file_name):
        """
        Parses a valid list as possible
        @param file_name: List file name
        @return: Returns lines in list
        """
        absolute_path = '{}{}{}'.format(self.path, _os.sep, file_name)
        try:
            file = GrabList.__open(absolute_path, 'r')
            data_list = []
            for data in file.readlines():
                data = data.strip()
                if not data:  # prevents blank lines
                    continue
                data_list.append(data)
            file.close()
            return data_list
        except Exception:
            return []
