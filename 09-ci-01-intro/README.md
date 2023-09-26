# Домашнее задание к занятию 7 «Жизненный цикл ПО»

## Подготовка к выполнению

1. Получить бесплатную версию [Jira](https://www.atlassian.com/ru/software/jira/free).
2. Настроить её для своей команды разработки.
3. Создать доски Kanban и Scrum.
4. [Дополнительные инструкции от разработчика Jira](https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/).

## Основная часть

Необходимо создать собственные workflow для двух типов задач: bug и остальные типы задач. Задачи типа bug должны проходить жизненный цикл:

1. Open -> On reproduce.
2. On reproduce -> Open, Done reproduce.
3. Done reproduce -> On fix.
4. On fix -> On reproduce, Done fix.
5. Done fix -> On test.
6. On test -> On fix, Done.
7. Done -> Closed, Open.

Остальные задачи должны проходить по упрощённому workflow:

1. Open -> On develop.
2. On develop -> Open, Done develop.
3. Done develop -> On test.
4. On test -> On develop, Done.
5. Done -> Closed, Open.

**Что нужно сделать**

1. Создайте задачу с типом bug, попытайтесь провести его по всему workflow до Done. 
1. Создайте задачу с типом epic, к ней привяжите несколько задач с типом task, проведите их по всему workflow до Done. 
1. При проведении обеих задач по статусам используйте kanban. 
1. Верните задачи в статус Open.
1. Перейдите в Scrum, запланируйте новый спринт, состоящий из задач эпика и одного бага, стартуйте спринт, проведите задачи до состояния Closed. Закройте спринт.
2. Если всё отработалось в рамках ожидания — выгрузите схемы workflow для импорта в XML. Файлы с workflow и скриншоты workflow приложите к решению задания.

## Решение

1. Создаем board kanban и заполняем необходимые колонки для задач типа bugs
<p align="center">
  <img width="1200" height="600" src="./image/bugs_board.png">
</p>

2. Создаем workflow на основе ранее созданной board kanban для задач типа bugs и настраиваем необходимые переходы статусов
<p align="center">
  <img width="1200" height="600" src="./image/workflow_bugs.png">
</p>

3. Связываем новый workflow с типом проблемы (bugs)
<p align="center">
  <img width="1200" height="600" src="./image/workflow1.png">
</p>
<p align="center">
  <img width="1200" height="600" src="./image/workflow2.png">
</p>

4. Создаем board kanban и заполняем необходимые колонки для остальных типов задач 
<p align="center">
  <img width="1200" height="600" src="./image/other_board.png">
</p>

5. Создаем workflow на основе ранее созданной board kanban для остальных типов задач и настраиваем необходимые переходы статусов
<p align="center">
  <img width="1200" height="600" src="./image/workflow_other.png">
</p>

6. Связываем новый workflow для остальных типов задач
<p align="center">
  <img width="1200" height="600" src="./image/workflow3.png">
</p>
<p align="center">
  <img width="1200" height="600" src="./image/workflow4.png">
</p>

7. Проверяем состав workflow для типов задач
<p align="center">
  <img width="1200" height="600" src="./image/workflow_all.png">
</p>

8. Создаем задачу с типом bug, и проводим ее по всему workflow до Done.
<p align="center">
  <img width="1200" height="600" src="./image/bug.png">
</p>

9. Создаем задачу с типом epic, привязываем к ней несколько задач с типом task, и проводим их по всему workflow до Done.
<p align="center">
  <img width="1200" height="600" src="./image/epic1.png">
</p>
<p align="center">
  <img width="1200" height="600" src="./image/epic2.png">
</p>
<p align="center">
  <img width="1200" height="600" src="./image/epic3.png">
</p>
<p align="center">
  <img width="1200" height="600" src="./image/epic4.png">
</p>

10. Возвращаем задачи в статус Open.
<p align="center">
  <img width="1200" height="600" src="./image/back.png">
</p>
---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---
