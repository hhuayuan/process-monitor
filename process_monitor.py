# coding = utf-8

import psutil
import time
import os
# import argparse

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Process monitor and do something when target down.')
    # parser.add_argument('-p', type=str, help='process full name,like:python.exe')
    # parser.add_argument('-t', type=int, help='Monitoring interval(seconds)')
    # parser.add_argument('-c', type=str, help='Execute command when target down, like:shutdown 0')
    # args = parser.parse_args()
    # print(args)
    # print('ok')
    # exit()
    while True:
        print('sleeping...')
        time.sleep(60*10)
        scrapy_count = 0
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                if pinfo['name'] == 'scrapy.exe':
                    scrapy_count += 1

            except psutil.NoSuchProcess:
                pass
            # else:
            #     print(pinfo)
        if scrapy_count > 0:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'spider still running...')
        else:
            s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '    spider down'
            f = open('spider.log', 'a', encoding='utf-8')
            f.write(s)
            f.close()
            print(s)
            time.sleep(10)
            os.system('shutdown /s /t 0')