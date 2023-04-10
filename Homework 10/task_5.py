"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_site(site):
    resolve_dns = subprocess.Popen(site, stdout=subprocess.PIPE)
    for line in resolve_dns.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


site1 = ['ping', 'yandex.ru']
site2 = ['ping', 'yandex.ru']
if __name__ == '__main__':
    ping_site(site1)
    ping_site(site2)
