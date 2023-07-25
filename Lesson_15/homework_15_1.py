# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
from collections import namedtuple
import os
import logging

FORMAT = '{levelname}  {msg} '

logging.basicConfig(format=FORMAT, style="{", filename="log5.txt", filemode='w', encoding="Utf-8", level=logging.INFO)
logger = logging.getLogger(__name__)

FileOrDir = namedtuple('FileOrDir', ['name', 'ext', "dir", "parent_dir"],
                       defaults=['', '', False, ''])

parser = argparse.ArgumentParser(description="homework_15_1")
parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
args = parser.parse_args()
def dir_info(input_path):
    result = []
    if not input_path:
        input_path = os.getcwd()
        logger.info(f'Путь установлен по умолчанию {input_path}')
    input_path = os.path.abspath(input_path)
    parent = input_path.rstrip('/').rsplit('/', 1)[0]
    for item in os.listdir(input_path):
        obj_name, obj_ext, obj_isdir = None, None, False
        item = item.rsplit('/', 1)[0]
        if os.path.isdir(os.path.join(parent, item)):
            obj_name = item
            obj_isdir = True
            dir_info(os.path.join(parent, obj_name))
        else:
            if item.rfind('.') != -1 and not item.startswith('.'):
                obj_name, obj_ext = item.rsplit('.', 1)
            else:
                obj_name = item
        logger.info(
            f'Имя:{obj_name}, Расширение: {obj_ext}, Родительская директория {parent}, Это директория: {obj_isdir}')
        result.append(FileOrDir(name=obj_name, ext=obj_ext, parent_dir=parent, dir=obj_isdir))

    return result


parser = argparse.ArgumentParser(description="homework_15_1")
parser.add_argument('-p', metavar='path', type=str, help='введите путь к директорию')
args = parser.parse_args().p


if __name__ == "__main__":
   dir_info('C:\MyGames')