"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def tuple_filepath(file_path):
    """
    Возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    """
    path = os.path.dirname(file_path)
    f_name = os.path.basename(file_path)
    name, extnsn = os.path.splitext(f_name)
    return path, name, extnsn


if __name__ == "__main__":
    result = tuple_filepath(input(
        'Введите абсолютный путь до файла, аналогично "/home/user/documents/file.txt": '))
    print('путь, имя файла, расширение: ', result)

# def tuple_path(file_path):
#     """
#     """
#     if '/' in file_path:
#         path, f_name = file_path.rsplit('/', 1)
#     elif '\\' in file_path:
#         path, f_name = file_path.rsplit('\\', 1)
#     else:
#         path = ''
#         f_name = file_path

#     name, extnsn = f_name.rsplit('.', 1) if '.' in f_name else (f_name, '')
#     return path, name, f".{extnsn}" if extnsn else ''


# if __name__ == "__main__":
#     file_path = "/home/user/documents/file.txt"
#     result = tuple_path(file_path)
#     print(result)
