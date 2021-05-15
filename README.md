## Process Monitor

简介
---

有时候需要在电脑上长时间运行一些程序，程序有自动退出功能，但程序退出时不会自动关机，就使用Python写了这么一个脚本，把目标程序监控起来，等目标程序运行结束退出后关机或者执行其它系统命令。

参数说明
---
python process_monitor.py -p example.exe -i 15 -c "echo test>whatever.txt"

### -p
必填，需要监控的进程名称，需要与进程列表中的名称对应，一般为目标主程序的文件名。

### -i
选填，监控间隔，单位为分钟，默认值是10，脚本会根据这个时间查询进程列表，一旦发现进程列表中不存在目标进程名称则会执行 -c 中的命令。

### -c
必填，如果这个参数不填这个脚本就没有意义了，脚本发现目标程序进程不存在后会执行该命令。

遗留问题
---
目前只在Windows 10 环境下测试过，Linux环境未测试。
