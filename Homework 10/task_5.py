"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def Ping(site):
    PING_SITE = subprocess.Popen(site, stdout=subprocess.PIPE)
    for line in PING_SITE.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


ARGS1 = ['ping', 'yandex.ru']
ARGS2 = ['ping', 'yandex.ru']
if __name__ == '__main__':
    Ping(ARGS1)
    Ping(ARGS2)
