# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
from shutil import copyfile

print(sys.path)
sys.path.append(r'C:\Users\Dmitrii\PycharmProjects\Python_lessons_basic')
def makedir(name):
    dir_path = os.path.join(os.getcwd(), name)
    print(dir_path)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')


def remdir(name):
    dir_path = os.path.join(os.getcwd(), name)
    print(dir_path)
    try:
        os.rmdir(dir_path)
    except FileExistsError:
        print('Такая директория уже не существует')


names = ['dir_'+str(i) for i in range(1, 10)]
for name in names:
    makedir(name)
for name in names:
    remdir(name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


l = os.listdir(path='.')
z = [e for e in l if '.' not in e]
print(z)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_this():
        copyfile(sys.argv[0],sys.argv[0][:-3]+'_copy.py')
