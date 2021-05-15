# coding = utf-8

import psutil
import time
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process monitor and do something when target down.')
    parser.add_argument('-p', '--process_name', type=str, required=True, help='Process full name,eg:python.exe')
    parser.add_argument('-i', '--interval', type=int, default=10,
                        help='Monitoring interval(minutes),default 10 minutes')
    parser.add_argument('-c', '--command', type=str, help='Execute command when target down, eg:"shutdown 0"')
    args = parser.parse_args()
    process_name = args.process_name
    interval = args.interval
    command = args.command

    while True:
        print('sleeping...')
        time.sleep(60 * interval)
        scrapy_count = 0
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                if pinfo['name'] == process_name:
                    scrapy_count += 1
            except psutil.NoSuchProcess:
                pass

        if scrapy_count > 0:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'process still running...')
        else:
            s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '    process down'
            f = open('process_monitor.log', 'a', encoding='utf-8')
            f.write(s)
            f.close()
            print(s)
            time.sleep(10)
            os.system(command)
            exit()
