# Домашнее задание к занятию 4 «Работа с roles»

## Подготовка к выполнению

1. * Необязательно. Познакомьтесь с [LightHouse](https://youtu.be/ymlrNlaHzIY?t=929).
2. Создайте два пустых публичных репозитория в любом своём проекте: vector-role и lighthouse-role.
3. Добавьте публичную часть своего ключа к своему профилю на GitHub.

## Основная часть

Ваша цель — разбить ваш playbook на отдельные roles. 

Задача — сделать roles для ClickHouse, Vector и LightHouse и написать playbook для использования этих ролей. 

Ожидаемый результат — существуют три ваших репозитория: два с roles и один с playbook.

**Что нужно сделать**

1. Создайте в старой версии playbook файл `requirements.yml` и заполните его содержимым:

   ```yaml
   ---
     - src: git@github.com:AlexeySetevoi/ansible-clickhouse.git
       scm: git
       version: "1.13"
       name: clickhouse 
   ```

2. При помощи `ansible-galaxy` скачайте себе эту роль.
3. Создайте новый каталог с ролью при помощи `ansible-galaxy role init vector-role`.
4. На основе tasks из старого playbook заполните новую role. Разнесите переменные между `vars` и `default`. 
5. Перенести нужные шаблоны конфигов в `templates`.
6. Опишите в `README.md` обе роли и их параметры. Пример качественной документации ansible role [по ссылке](https://github.com/cloudalchemy/ansible-prometheus).
7. Повторите шаги 3–6 для LightHouse. Помните, что одна роль должна настраивать один продукт.
8. Выложите все roles в репозитории. Проставьте теги, используя семантическую нумерацию. Добавьте roles в `requirements.yml` в playbook.
9. Переработайте playbook на использование roles. Не забудьте про зависимости LightHouse и возможности совмещения `roles` с `tasks`.
10. Выложите playbook в репозиторий.
11. В ответе дайте ссылки на оба репозитория с roles и одну ссылку на репозиторий с playbook.

## Решение

1. Создаем в старой версии playbook файл `requirements.yml` и заполняем его содержимым:
```
---
- name: clickhouse
  src: git@github.com:AlexeySetevoi/ansible-clickhouse.git
  scm: git
  version: "1.13"
```

2. При помощи команды ***ansible-galaxy install -r requirements.yml -p roles*** скачиваем эту роль.

3. Создаем новый каталог с ролью при помощи команды ***ansible-galaxy role init vector-role***.

4. На основе tasks из старого playbook заполняем новую role:
 
 - в директории tasks, в файле main.yml прописываем код для установки vector:
 ```
 ---
- block:
    - name: Install Vector
      become: true
      ansible.builtin.yum:
        name: "{{ vector_url }}"
        state: present
    - name: Vector | Template Config
      ansible.builtin.template:
        src: templates/vector.yml.j2
        dest: vector.yml
        mode: "0644"
        owner: "{{ ansible_user_id }}"
        group: "{{ ansible_user_gid }}"
        validate: vector validate --no-environment --config-yaml %s
    - name: Vector | Create systemd unit
      become: true
      ansible.builtin.template:
        src: templates/vector.service.j2
        dest: /etc/systemd/vector.service
        mode: "0755"
        owner: "{{ ansible_user_id }}"
        group: "{{ ansible_user_gid }}"
    - name: Vector | Start Service
      become: true
      ansible.builtin.systemd:
        name: vector
        state: started
        daemon_reload: true
 ``` 

 - в директории defaults, в файле main.yml прописываем переменные, доступные для изменения пользователем:
 ```
 ---
vector_version: "0.22.2"
 ```

 - в директории vars, в файле main.yml прописываем переменные, недоступные для изменения пользователем:
 
 ```
 ---
vector_url: https://packages.timber.io/vector/{{ vector_version }}/vector-{{ vector_version }}-1.x86_64.rpm
vector_config:
  sources:
    our_log:
      type: file
      ignore_older_secs: 600
      include:
        - /home/alex/logs/*.log
      read_from: beginning
  sinks:
    to_clickhouse:
      type: clickhouse
      inputs:
        - our_log
      database: custom
      endpoint: http://158.160.120.205:8123
      table: my_table
      compression: gzip
      healthcheck: false
      skip_unknown_fields: true
 ```

 - в директории meta, в файле main.yml заполняем информацию:
 
 ```
 galaxy_info:
  author: Aleksander Filippov
  description: This role install vector on EL
  company: netology

  # If the issue tracker for your role is not on github, uncomment the
  # next line and provide a value
  # issue_tracker_url: http://example.com/issue/tracker

  # Choose a valid license ID from https://spdx.org - some suggested licenses:
  # - BSD-3-Clause (default)
  # - MIT
  # - GPL-2.0-or-later
  # - GPL-3.0-only
  # - Apache-2.0
  # - CC-BY-4.0
  license: MIT

  min_ansible_version: "2.10"

  # If this a Container Enabled role, provide the minimum Ansible Container version.
  # min_ansible_container_version:

  #
  # Provide a list of supported platforms, and for each platform a list of versions.
  # If you don't wish to enumerate all versions for a particular platform, use 'all'.
  # To view available platforms and versions (or releases), visit:
  # https://galaxy.ansible.com/api/v1/platforms/
  #
  platforms:
    - name: Centos
      versions:
        - 7
        - 8
    - name: RHEL
      versions:
        - 7
        - 8
  # - name: SomePlatform
  #   versions:
  #   - all
  #   - 1.0
  #   - 7
  #   - 99.99

  galaxy_tags:
    []
    # List tags for your role here, one per line. A tag is a keyword that describes
    # and categorizes the role. Users find roles by searching for tags. Be sure to
    # remove the '[]' above, if you add tags to this list.
    #
    # NOTE: A tag is limited to a single word comprised of alphanumeric characters.
    #       Maximum 20 tags per role.

dependencies:
  []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
 ```

 - заполняем файл README.md:

```
Vector
=========

This role can install Vector on EL.

Role Variables
--------------

| vars | description |
|------|-------------|
| vector_version | Version of Vector to install |


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: vector }

License
-------

MIT

Author Information
------------------

Aleksander Filippov.
```

5. Переносим нужные шаблоны конфигов в `templates`:
 - vector.service.j2
```
[Unit]
Description=Vector service
After=network.target
Requires=network-online.target
[Service]
User=root
Group=root
ExecStart=/usr/bin/vector --config-yaml vector.yml --watch-config
Restart=always
[Install]
WantedBy=multi-user.target
```
 - vector.yml.j2
 ```
 {{ vector_config | to_nice_yaml }}
 ```

7. Создаем новый каталог с ролью при помощи команды ***ansible-galaxy role init lighthouse-role***.

 На основе tasks из старого playbook заполняем новую role:

 - в директории tasks, в файле main.yml прописываем код для установки lighthouse:
```
---
- name: Lighthouse | Copy from github
  become: true
  git:
    repo: "{{ lighthouse_vcs }}"
    version: master
    dest: "{{ lighthouse_location_dir }}"
- name: Lighthouse | Create lighthouse vector_config
  become: true
  template:
    src: templates/lighthouse.conf.j2
    dest: /etc/nginx/conf.d/default.conf
    mode: 0644
  notify: reload-nginx 
```

 - в директории handlers, в файле main.yml прописываем код блока lighthouse handlers из playbook:
 
```
---
- name: reload-nginx
  become: true
  command: nginx -s reload
```
 - в директории vars, в файле main.yml прописываем переменные, недоступные для изменения пользователем:
 ```
 ---
lighthouse_vcs: https://github.com/VKCOM/lighthouse.git
lighthouse_location_dir: /home/lighthouse
lighthouse_access_log_name: lighthouse_access
nginx_user_name: root
 ```

 - в директории meta, в файле main.yml заполняем информацию:
 ```
 galaxy_info:
  author: Aleksander Filippov
  description: This role install lighthouse on EL
  company: netology

  # If the issue tracker for your role is not on github, uncomment the
  # next line and provide a value
  # issue_tracker_url: http://example.com/issue/tracker

  # Choose a valid license ID from https://spdx.org - some suggested licenses:
  # - BSD-3-Clause (default)
  # - MIT
  # - GPL-2.0-or-later
  # - GPL-3.0-only
  # - Apache-2.0
  # - CC-BY-4.0
  license: MIT

  min_ansible_version: "2.10"

  # If this a Container Enabled role, provide the minimum Ansible Container version.
  # min_ansible_container_version:

  #
  # Provide a list of supported platforms, and for each platform a list of versions.
  # If you don't wish to enumerate all versions for a particular platform, use 'all'.
  # To view available platforms and versions (or releases), visit:
  # https://galaxy.ansible.com/api/v1/platforms/
  #
  platforms:
    - name: Centos
      versions:
        - 7
        - 8
    - name: RHEL
      versions:
        - 7
        - 8
  # - name: SomePlatform
  #   versions:
  #   - all
  #   - 1.0
  #   - 7
  #   - 99.99

  galaxy_tags:
    []
    # List tags for your role here, one per line. A tag is a keyword that describes
    # and categorizes the role. Users find roles by searching for tags. Be sure to
    # remove the '[]' above, if you add tags to this list.
    #
    # NOTE: A tag is limited to a single word comprised of alphanumeric characters.
    #       Maximum 20 tags per role.

dependencies:
  []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
 ```
 
 - заполняем файл README.md: 
```
Lighthouse
=========

This role can install Lighthouse on EL.


Role Variables
--------------

| vars | description |
|------|-------------|
| lighthouse_version | Version of Lighthouse to install |


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: lighthouse }

License
-------

MIT

Author Information
------------------

Aleksander Filippov
```

 Переносим нужные шаблоны конфигов в `templates`:
 
 - lighthouse.conf.j2 
```
server {
    listen          80;
    server_name     localhost;

    access_log      /var/log/nginx/{{ lighthouse_access_log_name }}.log main;

    location / {
        root    {{ lighthouse_location_dir }};
        index   index.html
    }
}
```

 Создаем новый каталог с ролью при помощи команды ***ansible-galaxy role init nginx-role***.


 На основе tasks из старого playbook заполняем новую role (nginx-role):

 - в директории tasks, в файле main.yml прописываем код для установки nginx:
```
---
- name: NGINX | Install epel-release
  become: true
  ansible.builtin.yum:
    name: epel-release
    state: present
- name: NGINX | Install NGINX
  become: true
  ansible.builtin.yum:
    name: nginx
    state: present
- name: NGINX | Create Config
  become: true
  template:
    src: templates/nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    mode: 0644
  notify: start-nginx
```

 - в директории handlers, в файле main.yml прописываем код блока nginx handlers из playbook:
```
 ---
- name: start-nginx
  become: true
  command: nginx
- name: reload-nginx
  become: true
  command: nginx -s reload
```
 - в директории meta, в файле main.yml заполняем информацию (nginx-role): 
 ```
 galaxy_info:
  author: Aleksander Filippov
  description: his role install nginx on EL
  company: netology

  # If the issue tracker for your role is not on github, uncomment the
  # next line and provide a value
  # issue_tracker_url: http://example.com/issue/tracker

  # Choose a valid license ID from https://spdx.org - some suggested licenses:
  # - BSD-3-Clause (default)
  # - MIT
  # - GPL-2.0-or-later
  # - GPL-3.0-only
  # - Apache-2.0
  # - CC-BY-4.0
  license: MIT

  min_ansible_version: "2.10"

  # If this a Container Enabled role, provide the minimum Ansible Container version.
  # min_ansible_container_version:

  #
  # Provide a list of supported platforms, and for each platform a list of versions.
  # If you don't wish to enumerate all versions for a particular platform, use 'all'.
  # To view available platforms and versions (or releases), visit:
  # https://galaxy.ansible.com/api/v1/platforms/
  #
  platforms:
    - name: Centos
      versions:
        - 7
        - 8
    - name: RHEL
      versions:
        - 7
        - 8
  # - name: SomePlatform
  #   versions:
  #   - all
  #   - 1.0
  #   - 7
  #   - 99.99

  galaxy_tags:
    []
    # List tags for your role here, one per line. A tag is a keyword that describes
    # and categorizes the role. Users find roles by searching for tags. Be sure to
    # remove the '[]' above, if you add tags to this list.
    #
    # NOTE: A tag is limited to a single word comprised of alphanumeric characters.
    #       Maximum 20 tags per role.

dependencies:
  []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
 ```
 
  - заполняем файл README.md:
```
Nginx
=========

This role can install Nginx on EL.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: nginx }

License
-------

MIT

Author Information
------------------

Aleksander Filippov
```

 Переносим нужные шаблоны конфигов в `templates`:
 
 - nginx.conf.j2:
```
user  {{ nginx_user_name }};
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   {{ lighthouse_location_dir }};
            index  index.html;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```

 - Редактируем playbook с учетом созданных ролей, прописываем следующий код:
```
---
- name: Install Nginx
  hosts: lighthouse
  roles:
    - nginx-role
       
- name: Install Lighthouse
  hosts: lighthouse
  roles:
    - lighthouse-role
  pre_tasks:
    - name: Lighthouse | Install Git
      become: true
      ansible.builtin.yum:
        name: git
        state: present

- name: Install Clickhouse
  hosts: clickhouse
  roles:
    - clickhouse

- name: Install Vector
  hosts: vector
  roles:
    - vector-role
```
 - Тестируем работу созданных role и playbook, запускаем в работу с помощью команды ***ansible-playbook -i inventory/prod.yml site.yml***:
 - начало выполнения playbook
<p align="center">
  <img width="1200" height="600" src="./image/task1.png">
</p> 

 - продолжение выполнения playbook
<p align="center">
  <img width="1200" height="600" src="./image/task2.png">
</p> 

 - дальнейшее выполнения playbook
<p align="center">
  <img width="1200" height="600" src="./image/task3.png">
</p> 

 - окончание выполнения playbook
<p align="center">
  <img width="1200" height="600" src="./image/task4.png">
</p>

Проверяем установленные приложения на хостах:
 - vector и clickhouse:
<p align="center">
  <img width="1200" height="600" src="./image/task5.png">
</p> 

 - lighthouse:
 <p align="center">
  <img width="1200" height="600" src="./image/task6.png">
</p> 


8. Создаем два репозитория ('vector-role' и 'lighthouse-role'), выкладываем созданные roles в соответствующих репозиториях.
```
aleksander@aleksander-MS-7641:~/lighthouse-role$ git tag -a 1.0.0 -m "v.1.0.0"
aleksander@aleksander-MS-7641:~/lighthouse-role$ git push --set-upstream origin master 1.0.0
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 4 потоков
Сжатие объектов: 100% (3/3), готово.
Запись объектов: 100% (3/3), 308 байтов | 102.00 КиБ/с, готово.
Всего 3 (изменений 2), повторно использовано 0 (изменений 0), повторно использовано пакетов 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/anfilippov7/lighthouse-role.git
   203b489..2eedbdb  master -> master
    * [new tag]         1.0.0 -> 1.0.0

```

```
aleksander@aleksander-MS-7641:~/vector-role$ git tag -a 1.0.0 -m "v.1.0.0"
aleksander@aleksander-MS-7641:~/vector-role$ git push --set-upstream origin master 1.0.0
Перечисление объектов: 19, готово.
Подсчет объектов: 100% (19/19), готово.
При сжатии изменений используется до 4 потоков
Сжатие объектов: 100% (10/10), готово.
Запись объектов: 100% (19/19), 2.84 КиБ | 364.00 КиБ/с, готово.
Всего 19 (изменений 0), повторно использовано 0 (изменений 0), повторно использовано пакетов 0
To https://github.com/anfilippov7/vector-role.git
 * [new branch]      master -> master
 * [new tag]         1.0.0 -> 1.0.0
Ветка «master» отслеживает внешнюю ветку «master» из «origin».

```
Добавляем roles в `requirements.yml` в playbook:
```
---
- name: clickhouse
  src: git@github.com:AlexeySetevoi/ansible-clickhouse.git
  scm: git
  version: "1.13"

- name: vector
  src: git@github.com/anfilippov7/vector-role.git
  scm: git
  version: "1.0.0"

- name: lighthouse
  src: git@github.com/anfilippov7/lighthouse-role.git
  scm: git
  version: "1.0.0"
```





---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
