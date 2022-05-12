import os


def get_latest_file(path=str):
    '''
    :param path: str
    :return: the last added file (filepath) of that folder
    '''
    files = os.listdir(path)
    file_paths = [os.path.join(path, filename) for filename in files]
    return max(file_paths, key=os.path.getctime)


def sort_list(list_):
    '''
    :param list_: list
    :return: the sorted list in reverse order based on element lengths
    '''
    list_.sort(key=len, reverse=True)
    return list_
