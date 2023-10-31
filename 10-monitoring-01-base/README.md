# Домашнее задание к занятию 13 «Введение в мониторинг»

## Обязательные задания

1. Вас пригласили настроить мониторинг на проект. На онбординге вам рассказали, что проект представляет из себя платформу для вычислений с выдачей текстовых отчётов, которые сохраняются на диск. Взаимодействие с платформой осуществляется по протоколу http. Также вам отметили, что вычисления загружают ЦПУ. Какой минимальный набор метрик вы выведите в мониторинг и почему?

## Решение 1

Минимальный набор метрик для мониторинга доджен быть такой:
 - необходимо организовать мониторинг загрузки CPU LA, для получения информации о нагрузке на центральный процессор, чтобы понимать хватает ли вычислительной мощности для обработки текущих задач, и есть ли необходимость масштабирования системы или рефакторинга приложения.
 - необходимо организовать мониторинг дисковой системы IOPS (число операций с дисками в секунду), это необходимо для контроля состояния дисковой подсистемы (слишком большие значения данного параметра могут свидетельствовать о проблемах с дисками)
 - необходимо организовать мониториг индексных дескрипторов inodes, для контролирования их переполнение делает невозможным создание новых файлов, очень актуально в нашем случае.
 - необходимо ввести в систему мониторинга метрику FS для контроля наличия свободного места на диске.
 - необходимо также ввести в ситему мониторинга метрику NetTraffic для контроля пропускной способности сетевого трафика, чтобы определить хватает ли для сервиса текушей пропусконой способности.
 - также в систему мониторинга необходимо ввести метрики доступности платформы на основе http кодов ответа, их количества и значения для определения количества неуспешных http-запросов, количества успешных http-запросов и вычисления процента успешных и неуспешных http-запросов.

2. Менеджер продукта, посмотрев на ваши метрики, сказал, что ему непонятно, что такое RAM/inodes/CPUla. Также он сказал, что хочет понимать, насколько мы выполняем свои обязанности перед клиентами и какое качество обслуживания. Что вы можете ему предложить?

## Решение 2

 - если менеджеру проекта интересно я подробно описал необходимые метрики мониторинга и для чего это нужно выше.
 - для получения информации, насколько мы выполняем свои обязанности перед клиентами и какое качество обслуживания, нам необходимо заключить соглашение SLA об уровне обслуживания, целевое качество которого будет описано в SLO, а следить за величиной фактически предоставляемого обслуживания необходимо по SLI.

3. Вашей DevOps-команде в этом году не выделили финансирование на построение системы сбора логов. Разработчики, в свою очередь, хотят видеть все ошибки, которые выдают их приложения. Какое решение вы можете предпринять в этой ситуации, чтобы разработчики получали ошибки приложения?

## Решение 3
 
 - для построения системы сбора логов пердложу организовать сбор логов с помощью Sentry 

4. Вы, как опытный SRE, сделали мониторинг, куда вывели отображения выполнения SLA = 99% по http-кодам ответов. 
Этот параметр вычисляется по формуле: summ_2xx_requests/summ_all_requests. Он не поднимается выше 70%, но при этом в вашей системе нет кодов ответа 5xx и 4xx. Где у вас ошибка?

## Решение 4

 - необходимо скорректировать формулу для учета успешных кодов ответа 3хх, скорректированная формула будет такой: ***(summ_2xx_requests + summ_3xx_requests)/(summ_all_requests)***

## Дополнительное задание* (со звёздочкой) 

Выполнение этого задания необязательно и никак не влияет на получение зачёта по домашней работе.

_____

Вы устроились на работу в стартап. На данный момент у вас нет возможности развернуть полноценную систему 
мониторинга, и вы решили самостоятельно написать простой python3-скрипт для сбора основных метрик сервера. 

Вы, как опытный системный администратор, знаете, что системная информация сервера лежит в директории `/proc`. Также знаете, что в системе Linux есть  планировщик задач cron, который может запускать задачи по расписанию.

Суммировав всё, вы спроектировали приложение, которое:

- является python3-скриптом;
- собирает метрики из папки `/proc`;
- складывает метрики в файл 'YY-MM-DD-awesome-monitoring.log' в директорию /var/log 
(YY — год, MM — месяц, DD — день);
- каждый сбор метрик складывается в виде json-строки, в виде:
  + timestamp — временная метка, int, unixtimestamp;
  + metric_1 — метрика 1;
  + metric_2 — метрика 2;
  
     ...
     
  + metric_N — метрика N.
  
- сбор метрик происходит каждую минуту по cron-расписанию.

Для успешного выполнения задания нужно привести:

* работающий код python3-скрипта;
* конфигурацию cron-расписания;
* пример верно сформированного 'YY-MM-DD-awesome-monitoring.log', имеющий не меньше пяти записей.

Дополнительная информация:

1. Количество собираемых метрик должно быть не меньше четырёх.
2. По желанию можно не ограничивать себя только сбором метрик из `/proc`.


## Решение дополнительное задание* (со звёздочкой) 

1. Для сбора основных метрик сервера пишем python3-скрипт следующего содержания:
```
rom __future__ import print_function
import os
from collections import OrderedDict
from datetime import datetime
import json


def uptime():
    ''' Return the information about up system in /proc/uptime
    as a dictionary '''
    up_time = OrderedDict()
    with open('/proc/uptime') as f:
        for line in f:
            up_time = line
    return up_time


def load_stat():
    ''' Return the information about load system in /proc/loadavg
    as a dictionary '''
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    return loadavg


def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    mem_info = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            mem_info[line.split(':')[0]] = line.split(':')[1].strip()
    return mem_info


def version():
    ''' Return the information in /proc/version
    as a dictionary '''
    ver = OrderedDict()

    with open('/proc/version') as f:
        for line in f:
            ver = line
    return ver


current_DateTime = datetime.now()
data = {'log_system': []}
data['log_system'].append({
    'timestamp': int(datetime.timestamp(current_DateTime)),
    'uptime': uptime(),
    'loadavg': load_stat(),
    'version_OS': version(),
    'Total_memory': meminfo()['MemTotal'],
    'Free_memory': meminfo()['MemFree']
})

log_file_name = f'{datetime.today().strftime("%Y-%m-%d")}' + '-awesome-monitoring.log'
base_path = '/var/log'
full_path = os.path.join(base_path, log_file_name)

if os.path.isdir(base_path):
    with open(full_path, 'a+', encoding='utf-8') as file:
        json.dump(data, file)
        file.write('\n')
else:
    print('No directory or permission denied for this directory')
```

2. Для настройки планировщика задач открываем редактор планировщика задач cron и записываем следующий код

```
  GNU nano 6.2                                                             /tmp/crontab.UgCurz/crontab                                                                       
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

* * * * * cd /home/aleksander/mnt-homeworks/10-monitoring-01-base && /home/aleksander/pythonProject1/venv/bin/python main.py
```

3. По умолчанию директория /var/log защищена от записи новых файлов, натраиваем доступ для записи в данную директорию под моим пользователем:
 - Cоздаем группу LOG и добавим в нее пользователя aleksander:
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/10-monitoring-01-base$ sudo groupadd LOG
aleksander@aleksander-MS-7641:~/mnt-homeworks/10-monitoring-01-base$ sudo usermod -aG LOG aleksander
aleksander@aleksander-MS-7641:~/mnt-homeworks/10-monitoring-01-base$ groups aleksander
aleksander : aleksander adm cdrom sudo dip plugdev lpadmin lxd sambashare docker LOG
```
 - перелогиниваемся чтобы система увидела это изменение
 - меняем группу папки /var/log на LOG
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/10-monitoring-01-base$ sudo chgrp LOG /var/log
```
 -  Создаем разрешение на чтение и запись для группы LOG:
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/10-monitoring-01-base$ sudo chmod g+rw /var/log
```

После выполнения перечисленных дествий в директории /var/log в начале следующей минуты выполняемтся написанный скрипт создается файл 'YY-MM-DD-awesome-monitoring.log' и выполняются записи следующего содержания
```
{"log_system": [{"timestamp": 1698735650, "uptime": "70288.66 267063.55\n", "loadavg": {"lavg_1": "1.01", "lavg_5": "0.79", "lavg_15": "0.74", "nr": "4/1422", "last_pid": "35236"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "416772 kB"}]}
{"log_system": [{"timestamp": 1698735661, "uptime": "70298.99 267096.45\n", "loadavg": {"lavg_1": "1.01", "lavg_5": "0.80", "lavg_15": "0.75", "nr": "1/1427", "last_pid": "35244"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "396624 kB"}]}
{"log_system": [{"timestamp": 1698735721, "uptime": "70359.03 267309.33\n", "loadavg": {"lavg_1": "0.46", "lavg_5": "0.68", "lavg_15": "0.71", "nr": "1/1428", "last_pid": "35280"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "360556 kB"}]}
{"log_system": [{"timestamp": 1698735781, "uptime": "70419.06 267515.45\n", "loadavg": {"lavg_1": "0.41", "lavg_5": "0.62", "lavg_15": "0.68", "nr": "4/1420", "last_pid": "35309"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "327912 kB"}]}
{"log_system": [{"timestamp": 1698735841, "uptime": "70479.09 267703.99\n", "loadavg": {"lavg_1": "0.78", "lavg_5": "0.66", "lavg_15": "0.69", "nr": "3/1417", "last_pid": "35344"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "180464 kB"}]}
{"log_system": [{"timestamp": 1698735901, "uptime": "70539.13 267901.40\n", "loadavg": {"lavg_1": "0.54", "lavg_5": "0.64", "lavg_15": "0.68", "nr": "1/1433", "last_pid": "35414"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "130620 kB"}]}
{"log_system": [{"timestamp": 1698735961, "uptime": "70599.21 268097.75\n", "loadavg": {"lavg_1": "0.44", "lavg_5": "0.60", "lavg_15": "0.67", "nr": "1/1436", "last_pid": "35458"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "171936 kB"}]}
{"log_system": [{"timestamp": 1698736021, "uptime": "70659.27 268317.76\n", "loadavg": {"lavg_1": "0.25", "lavg_5": "0.52", "lavg_15": "0.63", "nr": "1/1422", "last_pid": "35479"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "260664 kB"}]}
{"log_system": [{"timestamp": 1698736081, "uptime": "70719.34 268550.24\n", "loadavg": {"lavg_1": "0.15", "lavg_5": "0.43", "lavg_15": "0.60", "nr": "1/1419", "last_pid": "35497"}, "version_OS": "Linux version 6.2.0-33-generic (buildd@lcy02-amd64-073) (x86_64-linux-gnu-gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #33~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 10:33:52 UTC 2\n", "Total_memory": "8080700 kB", "Free_memory": "229672 kB"}]}
```

Пример файла логирования 'YY-MM-DD-awesome-monitoring.log' добавил в директорию с домашним заданием


---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.


---
