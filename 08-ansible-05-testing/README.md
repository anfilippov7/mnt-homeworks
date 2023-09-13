# Домашнее задание к занятию 5 «Тестирование roles»

## Подготовка к выполнению

1. Установите molecule: `pip3 install "molecule==3.5.2"` и драйвера `pip3 install molecule_docker molecule_podman`.
2. Выполните `docker pull aragast/netology:latest` —  это образ с podman, tox и несколькими пайтонами (3.7 и 3.9) внутри.

## Основная часть

Ваша цель — настроить тестирование ваших ролей. 

Задача — сделать сценарии тестирования для vector. 

Ожидаемый результат — все сценарии успешно проходят тестирование ролей.

### Molecule

1. Запустите  `molecule test -s centos_7` внутри корневой директории clickhouse-role, посмотрите на вывод команды. Данная команда может отработать с ошибками, это нормально. Наша цель - посмотреть как другие в реальном мире используют молекулу.
2. Перейдите в каталог с ролью vector-role и создайте сценарий тестирования по умолчанию при помощи `molecule init scenario --driver-name docker`.
3. Добавьте несколько разных дистрибутивов (centos:8, ubuntu:latest) для инстансов и протестируйте роль, исправьте найденные ошибки, если они есть.
4. Добавьте несколько assert в verify.yml-файл для  проверки работоспособности vector-role (проверка, что конфиг валидный, проверка успешности запуска и др.). 
5. Запустите тестирование роли повторно и проверьте, что оно прошло успешно.
6. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

### Tox

1. Добавьте в директорию с vector-role файлы из [директории](./example).
2. Запустите `docker run --privileged=True -v <path_to_repo>:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash`, где path_to_repo — путь до корня репозитория с vector-role на вашей файловой системе.
3. Внутри контейнера выполните команду `tox`, посмотрите на вывод.
5. Создайте облегчённый сценарий для `molecule` с драйвером `molecule_podman`. Проверьте его на исполнимость.
6. Пропишите правильную команду в `tox.ini`, чтобы запускался облегчённый сценарий.
8. Запустите команду `tox`. Убедитесь, что всё отработало успешно.
9. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

После выполнения у вас должно получится два сценария molecule и один tox.ini файл в репозитории. Не забудьте указать в ответе теги решений Tox и Molecule заданий. В качестве решения пришлите ссылку на  ваш репозиторий и скриншоты этапов выполнения задания. 

## Необязательная часть

1. Проделайте схожие манипуляции для создания роли LightHouse.
2. Создайте сценарий внутри любой из своих ролей, который умеет поднимать весь стек при помощи всех ролей.
3. Убедитесь в работоспособности своего стека. Создайте отдельный verify.yml, который будет проверять работоспособность интеграции всех инструментов между ними.
4. Выложите свои roles в репозитории.

В качестве решения пришлите ссылки и скриншоты этапов выполнения задания.


### Решение Molecule

1. Берем за основу ДЗ "Работа с roles", переходим в директорию с role clickhouse и запускаем команду ***`molecule test -s centos_7`***, выполнение падает с ошибкой:
```
INFO     Running from /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse : ansible-galaxy collection install -vvv community.docker:>=1.9.1
CRITICAL Collection 'community.docker' not found in '['/home/aleksander/.cache/ansible-compat/7e099f/collections', '/home/aleksander/.cache/ansible-compat/7e099f/collections', '/home/aleksander/.ansible/collections', '/usr/share/ansible/collections']'
```

 - Устанавливаем  community.docker с помощью команды ***ansible-galaxy collection install community.docker:1.9.1***, затем повторно ***`molecule test -s centos_7`***, получаем результат:
 
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse$ molecule test -s centos_7
INFO     centos_7 scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Set ANSIBLE_LIBRARY=/home/aleksander/.cache/ansible-compat/7e099f/modules:/home/aleksander/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/aleksander/.cache/ansible-compat/7e099f/collections:/home/aleksander/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/aleksander/.cache/ansible-compat/7e099f/roles:/home/aleksander/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > lint
COMMAND: yamllint .
ansible-lint
flake8

WARNING: PATH altered to include /usr/bin
WARNING  Loading custom .yamllint config file, this extends our internal yamllint config.
an AnsibleCollectionFinder has not been installed in this process
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos_7)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > syntax

playbook: /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/resources/playbooks/converge.yml
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > create

PLAY [Create] ******************************************************************

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Create Dockerfiles from image names] *************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'diff': {'before': {'path': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7'}, 'after': {'path': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7'}}, 'path': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7', 'changed': False, 'uid': 1000, 'gid': 1000, 'owner': 'aleksander', 'group': 'aleksander', 'mode': '0600', 'state': 'file', 'size': 2199, 'invocation': {'module_args': {'mode': '0600', 'dest': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7', '_original_basename': 'Dockerfile.j2', 'recurse': False, 'state': 'file', 'path': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7', 'force': False, 'follow': True, 'modification_time_format': '%Y%m%d%H%M.%S', 'access_time_format': '%Y%m%d%H%M.%S', 'unsafe_writes': False, '_diff_peek': None, 'src': None, 'modification_time': None, 'access_time': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None}}, 'checksum': '4b70768619482424811f2977aa277a5acf2b13a1', 'dest': '/home/aleksander/.cache/molecule/clickhouse/centos_7/Dockerfile_centos_7', 'failed': False, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
changed: [localhost] => (item=molecule_local/centos:7)

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j189040347768.57054', 'results_file': '/home/aleksander/.ansible_async/j189040347768.57054', 'changed': True, 'item': {'capabilities': ['SYS_ADMIN'], 'command': '/usr/sbin/init', 'dockerfile': '../resources/Dockerfile.j2', 'env': {'ANSIBLE_USER': 'ansible', 'DEPLOY_GROUP': 'deployer', 'SUDO_GROUP': 'wheel', 'container': 'docker'}, 'image': 'centos:7', 'name': 'centos_7', 'privileged': True, 'tmpfs': ['/run', '/tmp'], 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup']}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=7    changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
[WARNING]: The "community.docker.docker" connection plugin has an improperly
configured remote target value, forcing "inventory_hostname" templated value
instead of the string
ok: [centos_7]

TASK [Apply Clickhouse Role] ***************************************************
ERROR! the role 'ansible-clickhouse' was not found in /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/resources/playbooks/roles:/home/aleksander/.cache/molecule/clickhouse/centos_7/roles:/home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles:/home/aleksander/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse:/home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/resources/playbooks

The error appears to be in '/home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/resources/playbooks/converge.yml': line 7, column 15, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

      include_role:
        name: ansible-clickhouse
              ^ here

PLAY RECAP *********************************************************************
centos_7                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '-D', '--inventory', '/home/aleksander/.cache/molecule/clickhouse/centos_7/inventory', '--skip-tags', 'molecule-notest,notest', '/home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/resources/playbooks/converge.yml']
WARNING  An error occurred during the test sequence action: 'converge'. Cleaning up.
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/hosts.yml linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/hosts
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/group_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/group_vars
INFO     Inventory /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/clickhouse/molecule/centos_7/../resources/inventory/host_vars/ linked to /home/aleksander/.cache/molecule/clickhouse/centos_7/inventory/host_vars
INFO     Running centos_7 > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos_7)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=centos_7)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory 
```

2. Переходим в каталог с ролью vector-role и создаем сценарий тестирования при помощи команды ***`molecule init scenario --driver-name docker`***:
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role$ molecule init scenario --driver-name docker
INFO     Initializing new scenario default...
INFO     Initialized scenario in /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role/molecule/default successfully.
```
3. Добавляем дистрибутивы centos:8 и ubuntu:latest для инстансов и тестируем роль, исправляем найденные ошибки.

 - обновляем community.docker с помощью команды ***ansible-galaxy collection install community.docker:2.7.6***
```
aleksander@aleksander-MS-7641:~/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role$ ansible-galaxy collection install community.docker:2.7.6
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/download/community-docker-2.7.6.tar.gz to /home/aleksander/.ansible/tmp/ansible-local-9742112esowaz/tmpkwqjzjw1/community-docker-2.7.6-pzvlwakc
Installing 'community.docker:2.7.6' to '/home/aleksander/.ansible/collections/ansible_collections/community/docker'
community.docker:2.7.6 was installed successfully
```
 - в файле molecule.yml прописываем код для создания инстансов:
```
 ---
dependency:
  name: galaxy
driver:
  name: docker
lint: |
  ansible-lint .
  yamllint .
platforms:
  - name: centos8
    image: quay.io/centos/centos:stream8
    pre_build_image: true
  - name: ubuntu
    image: docker.io/pycontribs/ubuntu:latest
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
```

 - в папке tasks создаем файлы ubuntu.yml, centos8.yml, main.yml и прописываем следующий код для установки инстансов, соответственно:
```
 ---
- block:
    - name: Install Vector
      ansible.builtin.dnf:
        disable_gpg_check: true
        name: "{{ vector_url }}"
        state: present
    - name: Vector | Template Config
      ansible.builtin.template:
        src: templates/vector.yml.j2
        dest: /etc/vector/vector.yaml
        mode: "0644"
        owner: "{{ ansible_user_id }}"
        group: "{{ ansible_user_gid }}"
        validate: vector validate --no-environment --config-yaml %s
    - name: Vector | Create systemd unit
      ansible.builtin.template:
        src: templates/vector.service.j2
        dest: /etc/systemd/vector.service
        mode: "0755"
        owner: "{{ ansible_user_id }}"
        group: "{{ ansible_user_gid }}"
```

```
---
- block:
  - name: Install vector deb
    become: true
    ansible.builtin.apt:
      deb:  https://packages.timber.io/vector/{{ vector_version }}/vector_{{ vector_version }}-1_amd64.deb
      update_cache: yes
      state: present
  - name: Vector | Template Config
    ansible.builtin.template:
      src: templates/vector.yml.j2
      dest: /etc/vector/vector.yaml
      mode: "0644"
      owner: "{{ ansible_user_id }}"
      group: "{{ ansible_user_gid }}"
      validate: vector validate --no-environment --config-yaml %s
  - name: Vector | Create systemd unit
    ansible.builtin.template:
      src: templates/vector.service.j2
      dest: /etc/systemd/vector.service
      mode: "0755"
      owner: "{{ ansible_user_id }}"
      group: "{{ ansible_user_gid }}"
```

```
---
- name: Install vector for centos8
  import_tasks: centos8.yml
  when: ansible_facts['os_family'] == "RedHat"

- name: Install vector for ubuntu
  import_tasks: ubuntu.yml
  when: ansible_facts['os_family'] == "Debian"
```

 - выполняем команду ***molecule test***, тест прошел успешно:
```
aleksander@aleksander-System-Product-Name:~/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role$ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Set ANSIBLE_LIBRARY=/home/aleksander/.cache/ansible-compat/f5bcd7/modules:/home/aleksander/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/aleksander/.cache/ansible-compat/f5bcd7/collections:/home/aleksander/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/aleksander/.cache/ansible-compat/f5bcd7/roles:/home/aleksander/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
COMMAND: ansible-lint .
yamllint .

ERROR    Computed fully qualified role name of vector-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

Computed fully qualified role name of vector-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos8)
ok: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Synchronization the context] *********************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/quay.io/centos/centos:stream8) 
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/ubuntu:latest) 
skipping: [localhost]

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) creation to complete] *******************************
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j871342857499.28696', 'results_file': '/home/aleksander/.ansible_async/j871342857499.28696', 'changed': True, 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j84753133139.28741', 'results_file': '/home/aleksander/.ansible_async/j84753133139.28741', 'changed': True, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos8]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install Vector] ********************************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Install vector deb] ****************************************
skipping: [centos8]
changed: [ubuntu]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [centos8]
changed: [ubuntu]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [centos8]
changed: [ubuntu]

PLAY RECAP *********************************************************************
centos8                    : ok=4    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
ubuntu                     : ok=4    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos8]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install Vector] ********************************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Install vector deb] ****************************************
skipping: [centos8]
ok: [ubuntu]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [centos8]
ok: [ubuntu]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [centos8]
ok: [ubuntu]

PLAY RECAP *********************************************************************
centos8                    : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
ubuntu                     : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] ******************************************************************

TASK [Example assertion] *******************************************************
ok: [centos8] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
centos8                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item=centos8)
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
```
4. Добавляем в файл verify.yml проверку работоспособности vector-role (проверку версии и проверку что конфиг валидный)
```
- name: Verify
  hosts: all
  gather_facts: false
  vars:
    vector_config_path: /etc/vector/vector.yaml
  tasks:
    - name: Get Vector version
      ansible.builtin.command: "vector --version"
      changed_when: false
      register: vector_version
    - name: Assert Vector instalation
      assert:
        that: "'{{ vector_version.rc }}' == '0'"

    - name: Validation Vector configuration
      ansible.builtin.command: "vector validate --no-environment --config-yaml {{ vector_config_path }}"
      changed_when: false
      register: vector_validate
    - name: Assert Vector validate config
      assert:
        that: "'{{ vector_validate.rc }}' == '0'"
```

 - выполняем команду ***molecule test***, тест прошел успешно:
```
aleksander@aleksander-System-Product-Name:~/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role$ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Set ANSIBLE_LIBRARY=/home/aleksander/.cache/ansible-compat/f5bcd7/modules:/home/aleksander/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/home/aleksander/.cache/ansible-compat/f5bcd7/collections:/home/aleksander/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/home/aleksander/.cache/ansible-compat/f5bcd7/roles:/home/aleksander/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
COMMAND: ansible-lint .
yamllint .

ERROR    Computed fully qualified role name of vector-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

Computed fully qualified role name of vector-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos8)
ok: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /home/aleksander/mnt-homeworks/08-ansible-05-testing/playbooks/roles/vector-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Synchronization the context] *********************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'false_condition': 'not item.pre_build_image | default(false)', 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/quay.io/centos/centos:stream8) 
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/ubuntu:latest) 
skipping: [localhost]

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) creation to complete] *******************************
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j164192299331.38028', 'results_file': '/home/aleksander/.ansible_async/j164192299331.38028', 'changed': True, 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'centos8', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j505301064948.38061', 'results_file': '/home/aleksander/.ansible_async/j505301064948.38061', 'changed': True, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos8]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install Vector] ********************************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [ubuntu]
changed: [centos8]

TASK [vector-role : Install vector deb] ****************************************
skipping: [centos8]
changed: [ubuntu]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [centos8]
changed: [ubuntu]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [centos8]
changed: [ubuntu]

PLAY RECAP *********************************************************************
centos8                    : ok=4    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
ubuntu                     : ok=4    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos8]

TASK [Include vector-role] *****************************************************

TASK [vector-role : Install Vector] ********************************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [ubuntu]
ok: [centos8]

TASK [vector-role : Install vector deb] ****************************************
skipping: [centos8]
ok: [ubuntu]

TASK [vector-role : Vector | Template Config] **********************************
skipping: [centos8]
ok: [ubuntu]

TASK [vector-role : Vector | Create systemd unit] ******************************
skipping: [centos8]
ok: [ubuntu]

PLAY RECAP *********************************************************************
centos8                    : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
ubuntu                     : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] ******************************************************************

TASK [Get Vector version] ******************************************************
ok: [ubuntu]
ok: [centos8]

TASK [Assert Vector instalation] ***********************************************
ok: [centos8] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Validation Vector configuration] *****************************************
ok: [ubuntu]
ok: [centos8]

TASK [Assert Vector validate config] *******************************************
ok: [centos8] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
centos8                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item=centos8)
changed: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
```
 
---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.
