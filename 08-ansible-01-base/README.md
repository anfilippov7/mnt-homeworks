# Домашнее задание к занятию 1 «Введение в Ansible»

## Подготовка к выполнению

1. Установите Ansible версии 2.10 или выше.
2. Создайте свой публичный репозиторий на GitHub с произвольным именем.
3. Скачайте [Playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.

## Основная часть

1. Попробуйте запустить playbook на окружении из `test.yml`, зафиксируйте значение, которое имеет факт `some_fact` для указанного хоста при выполнении playbook.
2. Найдите файл с переменными (group_vars), в котором задаётся найденное в первом пункте значение, и поменяйте его на `all default fact`.
3. Воспользуйтесь подготовленным (используется `docker`) или создайте собственное окружение для проведения дальнейших испытаний.
4. Проведите запуск playbook на окружении из `prod.yml`. Зафиксируйте полученные значения `some_fact` для каждого из `managed host`.
5. Добавьте факты в `group_vars` каждой из групп хостов так, чтобы для `some_fact` получились значения: для `deb` — `deb default fact`, для `el` — `el default fact`.
6. Повторите запуск playbook на окружении `prod.yml`. Убедитесь, что выдаются корректные значения для всех хостов.
7. При помощи `ansible-vault` зашифруйте факты в `group_vars/deb` и `group_vars/el` с паролем `netology`.
8. Запустите playbook на окружении `prod.yml`. При запуске `ansible` должен запросить у вас пароль. Убедитесь в работоспособности.
9. Посмотрите при помощи `ansible-doc` список плагинов для подключения. Выберите подходящий для работы на `control node`.
10. В `prod.yml` добавьте новую группу хостов с именем  `local`, в ней разместите localhost с необходимым типом подключения.
11. Запустите playbook на окружении `prod.yml`. При запуске `ansible` должен запросить у вас пароль. Убедитесь, что факты `some_fact` для каждого из хостов определены из верных `group_vars`.
12. Заполните `README.md` ответами на вопросы. Сделайте `git push` в ветку `master`. В ответе отправьте ссылку на ваш открытый репозиторий с изменённым `playbook` и заполненным `README.md`.


## Необязательная часть

1. При помощи `ansible-vault` расшифруйте все зашифрованные файлы с переменными.
2. Зашифруйте отдельное значение `PaSSw0rd` для переменной `some_fact` паролем `netology`. Добавьте полученное значение в `group_vars/all/exmp.yml`.
3. Запустите `playbook`, убедитесь, что для нужных хостов применился новый `fact`.
4. Добавьте новую группу хостов `fedora`, самостоятельно придумайте для неё переменную. В качестве образа можно использовать [этот вариант](https://hub.docker.com/r/pycontribs/fedora).
5. Напишите скрипт на bash: автоматизируйте поднятие необходимых контейнеров, запуск ansible-playbook и остановку контейнеров.
6. Все изменения должны быть зафиксированы и отправлены в ваш личный репозиторий.

---

## Решение

1. Запускаем playbook на окружении из `test.yml` командой ***ansible-playbook -i inventory/test.yml site.yml***, фиксируем значение факта `some_fact` для указанного хоста при выполнении playbook - 12 (***"msg": 12**)
<p align="center">
  <img width="1200" height="600" src="./image/task1.png">
</p>

2. Меняем значение `some_fact` в файле с переменными (group_vars) на `all default fact`, проверяем внесенные изменения:
<p align="center">
  <img width="1200" height="600" src="./image/task2.png">
</p>

3. Для проведения дальнейших испытаний создаем окружение `docker`, выполняем команды:
   ***docker run --name centos7 -d pycontribs/centos:7***
   ***docker run --name ubuntu -d pycontribs/ubuntu***

4. Запускаем playbook на окружении из `prod.yml` командой ***ansible-playbook -i inventory/prod.yml site.yml***, фиксируем значение факта `some_fact` для каждого из `managed host` при выполнении playbook:
```
TASK [Print fact] ********************************************************************************
ok: [centos7] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}
```
<p align="center">
  <img width="1200" height="600" src="./image/task4.png">
</p>

5. Добавляем факты в `group_vars` каждой из групп хостов: для `deb` — `deb default fact`, для `el` — `el default fact`. 
 - el.yml:
 ```
 ---
some_fact: "el default fact"
 ```
 - deb.yml: 
  ```
---
some_fact: "deb default fact"
 ``` 

6. Запускаем playbook на окружении `prod.yml`, фиксируем результат:
<p align="center">
  <img width="1200" height="600" src="./image/task6.png">
</p>

7. При помощи `ansible-vault` шифруем факты в `group_vars/deb` и `group_vars/el` с паролем `netology`:
<p align="center">
  <img width="1200" height="600" src="./image/task7.png">
</p>

8. Запускаем playbook при помощи команды ***ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass*** и вводим пароль `netology`, получаем результат:
<p align="center">
  <img width="1200" height="600" src="./image/task8.png">
</p>

9. Запускаем команду ***ansible-doc -t connection -l***, получаем список плагинов для подключения, подходящий для работы на `control node` - ansible.builtin.local
<p align="center">
  <img width="1200" height="600" src="./image/task9.png">
</p>

10. В файле `prod.yml` добавляем новую группу хостов с именем  `local`, в ней размещаем localhost с типом подключения local:
```
local:
  hosts:
    localhost:
      ansible_connection: local
```

11. Запускаем playbook на окружении `prod.yml` с помощью команды ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass, фиксируем результат:
<p align="center">
  <img width="1200" height="600" src="./image/task11.png">
</p>


## Решение необязательная часть

1. При помощи `ansible-vault` расшифруйте зашифрованные файлы с переменными (group_vars/deb/examp.yml и group_vars/el/examp.yml).

 - вводим две команды с паролем netology:
	***ansible-vault decrypt group_vars/deb/examp.yml***
	***ansible-vault decrypt group_vars/el/examp.yml***

Фиксируем успешное выполнение команд выше:
<p align="center">
  <img width="1200" height="600" src="./image/task1_1.png">
</p>

2. Шифруем значение `PaSSw0rd` для переменной `some_fact` паролем `netology` и добавляем полученное значение в `group_vars/all/exmp.yml`.
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/08-ansible-01-base/playbook$ ansible-vault encrypt_string
New Vault password: 
Confirm New Vault password: 
Reading plaintext input from stdin. (ctrl-d to end input, twice if your content does not already have a newline)
PaSSw0rd
Encryption successful
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          38613562633836333635383038363862383034356363333136333637333332633438666131343531
          3065353163363431336263626664653539623361623763660a623963336339623337626137303462
          65366364383530353333663132636230623738383764663132363865646432363838643430626262
          6234346533323164360a333833323738313563633465326366376432646534646661346337383239
          6563

```

```
---
some_fact: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  38613562633836333635383038363862383034356363333136333637333332633438666131343531
  3065353163363431336263626664653539623361623763660a623963336339623337626137303462
  65366364383530353333663132636230623738383764663132363865646432363838643430626262
  6234346533323164360a333833323738313563633465326366376432646534646661346337383239
  6563
```

3. Запускаем `playbook` с помощью команды ***ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass*** и вводим пароль netology, фиксируем новый `fact` для localhost:
<p align="center">
  <img width="1200" height="600" src="./image/task1_3.png">
</p>

4. Запускаем `docker` образ fedora, выполняем команду:
   ***docker run --name fedora -d pycontribs/fedora***

 - в файл prod.yml добавляем перепенную db и записываем в нее группу хостов `fedora`
```
---
el:
  hosts:
    centos7:
      ansible_connection: docker
deb:
  hosts:
    ubuntu:
      ansible_connection: docker
local:
  hosts:
    localhost:
      ansible_connection: local
db:
  hosts:
    fedora:
      ansible_connection: docker
```

 - запускаем `playbook` с помощью команды ***ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass*** и вводим пароль netology, фиксируем новую группу fedora:
<p align="center">
  <img width="1200" height="600" src="./image/task1_4.png">
</p> 
 
5. Создаем скрипт на bash: автоматизируем поднятие необходимых контейнеров, запуск ansible-playbook и остановку контейнеров:
```
#!/usr/bin/env bash

ansible_playbook_home="../playbook"
ansible_password_file="./password"


declare -A image

image["ubuntu"]="pycontribs/ubuntu"
image["centos7"]="pycontribs/centos:7"
image["fedora"]="pycontribs/fedora"


#**********************************************************#

function start_containers() {

  for container in ${!image[@]}
    do
      echo -e "--- Launching a docker container \"${container}\" from image \"${image[${container}]}\": ---"
      if docker run -d -t --rm --name ${container} ${image[${container}]} > /dev/null
        then
          echo -e "--- Done. ---\n"
        else
          echo -e "--- Error while starting docker container... Exit. ---\n"
          exit 1
      fi
    done
}


function stop_containers() {

    for container in ${!image[@]}
      do
        echo -e "--- Stoping a docker container \"${container}\" from image \"${image[${container}]}\": ---"
        if docker container stop ${container} > /dev/null
          then
            echo -e "--- Done. ---\n"
          else
            echo -e "--- Error while stoping docker container... Exit. ---\n"
            exit 1
        fi

      done
}


function play_ansible() {

    if cd ${ansible_playbook_home}
      then
        echo -e "\n--- Running ansible playbook: ---\n"
        ansible-playbook site.yml -i inventory/prod.yml --vault-password-file ${ansible_password_file}
      else
        echo -e "\n--- Error when changing directory... Exit. ---\n"
        stop_containers
        exit 1
    fi
}


#**********************************************************#

echo -e "\n--- Launching docker containers... : ---\n"
start_containers


echo -e "\n--- The following docker containers are running: ---\n"
docker ps


echo -e "\n--- Changing the directory with ansible playbook \"${ansible_playbook_home}\": ---\n"
play_ansible


echo -e "\n--- Stopping docker containers... : ---"
stop_containers
```

 - выполняем запуск скрипта командой ***bash auto_example.sh***, получаем результат: 

```
aleksander@aleksander-MS-7641:~/mnt-homeworks/08-ansible-01-base/bash$ bash auto_example.sh 

--- Launching docker containers... : ---

--- Launching a docker container "centos7" from image "pycontribs/centos:7": ---
--- Done. ---

--- Launching a docker container "fedora" from image "pycontribs/fedora": ---
--- Done. ---

--- Launching a docker container "ubuntu" from image "pycontribs/ubuntu": ---
--- Done. ---


--- The following docker containers are running: ---

CONTAINER ID   IMAGE                 COMMAND       CREATED                  STATUS                  PORTS     NAMES
946534c8ed24   pycontribs/ubuntu     "/bin/bash"   Less than a second ago   Up Less than a second             ubuntu
701d4dbe1338   pycontribs/fedora     "/bin/bash"   1 second ago             Up Less than a second             fedora
426b3e96523f   pycontribs/centos:7   "/bin/bash"   1 second ago             Up Less than a second             centos7

--- Changing the directory with ansible playbook "../playbook": ---


--- Running ansible playbook: ---


PLAY [Print os facts] ***********************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [localhost]
ok: [fedora]
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] *****************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [localhost] => {
    "msg": "Ubuntu"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}
ok: [fedora] => {
    "msg": "Fedora"
}

TASK [Print fact] ***************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
ok: [localhost] => {
    "msg": "PaSSw0rd"
}
ok: [fedora] => {
    "msg": "db default fact"
}

PLAY RECAP **********************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
fedora                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


--- Stopping docker containers... : ---
--- Stoping a docker container "centos7" from image "pycontribs/centos:7": ---
--- Done. ---

--- Stoping a docker container "fedora" from image "pycontribs/fedora": ---
--- Done. ---

--- Stoping a docker container "ubuntu" from image "pycontribs/ubuntu": ---
--- Done. ---

```



6. Все изменения должны быть зафиксированы и отправлены в ваш личный репозиторий.

## Необязательная часть


### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
