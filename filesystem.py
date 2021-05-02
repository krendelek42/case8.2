import os

from glob import glob
path = 'C:\НГУ'
os.chdir(path)

def acceptCommand(): # эта доделана
    q = False
    while q != True:
        num = input('Выберите пункт меню: ')
        try:
            num = int(num)
            a = True
            if num <= 7 and num >= 1:
                True
            else:
                a = False
            if a == False:
                print('Номер введен ошибочно. Повторите попытку.')
                num = int(input('Выберите пункт меню: '))
        except ValueError:
            print('Введенное "{}" не является числом. Повторите попытку.'.format(num))
        else:
            q = True
    if num == 7:
        return 'QUIK'
    return num



def moveDown(currentDir):  # эта доделана
    a = False
    while a!= True:
        name = input('Введите имя папки, в которую хотите переместиться, или файла, который хотите открыть: ')
        new_path = os.path.join(currentDir, name)
        if os.path.exists(new_path) == True:
            a = True
        else:
            print('Папка\файл не существует. Повторите попытку.')
            a = False
    if os.path.isdir(new_path) == True:
        return os.chdir(new_path)
    if os.path.isfile(new_path) == True:
        return os.startfile(new_path)


def moveUp():  # эта доделана
    path = os.getcwd()
    new_path = os.path.dirname(path)  # parent
    os.chdir(new_path)


def runCommand(command): # нужно доделать 4, 5 и 6 пунк. Они делаются на основе функций

    if command == 1:
        print()
        dir = []
        files = []
        currentDir = os.getcwd()
        for item in os.scandir(currentDir):
            if item.is_dir():
                dir.append(item.name)
            if item.is_file():
                files.append(item.name)
        print('Папки: ', dir)
        print('Файлы: ', files)
        print()


    if command == 2:
        print()
        moveUp()
        print()


    if command == 3:
        print()
        currentDir = os.getcwd()
        moveDown(currentDir)
        print()


    if command == 4: # тут просто костяк написан
        print()
        path = os.getcwd()
        print('Количество файлов:', countFiles(path))
        print()


    if command == 6:
        print()
        path = os.getcwd()

        findFiles(path)


def countFiles(path):
    if os.path.isfile(path):
        return 1

    count = 0
    dir_list = os.listdir(path)
    for d in dir_list:
        new_path = path + '\\' + d
        count += countFiles(new_path)

    return count


def countBytes(path):
    if os.path.isfile(path):
        return os.path.getsize(path)

    count = 0
    dir_list = os.listdir(path)
    for d in dir_list:
        new_path = path + '\\' + d
        count += countBytes(new_path)

    return count

def findFiles(path, target = [] ): #это поя последняя 6, пытаюсь ее доделать
    '''
    # target - имя файла
    # path - каталог
    '''
    for item in os.scandir(path):
        if item.is_file():
            target.append(item.name)
    print(target)






# все что зеленое, это я пыталась написать 4 функцию. Вышла фигня, не обращай внимание

'''
from functools import lru_cache
@lru_cache(maxsize=None)
def countFiles(path):
    for root, dir, files in os.walk(p)
'''



'''
    if len(spisok) == 0 and path != paths:
        name = os.path.basename(paths)
        paths = os.path.dirname(paths)
        spisok = os.listdir(paths)
        f = spisok.index(name)
        return countFiles(path, spisok[f:], paths)
    if len(spisok) == 0 and path == paths:
        return 0
    if os.path.isfile(os.path.join(paths, spisok[0])) != True:
        paths = os.path.join(paths, spisok[0])
        spisok = os.listdir(paths)
        return countFiles(path, spisok, paths)
    return 1 + countFiles(path, spisok[1:], paths)
'''




def main(): # эта функция дописана, ее не надо трогать
    while True:
        print(os.getcwd())
        print('1. Просмотр каталога', '2. На уровень вверх', '3. На уровень аниз', '4. Количесвто файлов и каталогов',
              '5. Размер текущего каталога (в байтах)', '6. Поиск файла', '7. Выход из программы', sep='\n')
        command = acceptCommand()
        if command == 'QUIK':
            print()
            print('Работа программы завершена.')
            break
            print()
        runCommand(command)
main()