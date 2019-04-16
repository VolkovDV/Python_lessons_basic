#!C:\Users\Dmitrii\PycharmProjects\Python_lessons_basic\lesson05\examples\5_with_args.py
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
from shutil import copyfile
import lesson05.home_work.hw05_easy as easy
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file(filename):
    if not filename:
        print("Необходимо указать имя файла")
        return
    try:
        copyfile(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), filename)[:-3] + '_copy.py'
             + os.path.join(os.getcwd(), filename)[-3:])
    except:
        print('Error')

def remove_file(filename):
    if not filename:
        print("Необходимо указать имя файла")
        return
    try:
        print('Are you sure? Y -yes, N - No')
        agree = int(input())
        if agree == 'Y':
            easy.remdir(filename)
        else:
            print('Отменено')
    except:
        print('Error')

def ls():
    print(os.listdir(path='.'))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
