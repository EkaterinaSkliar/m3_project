Тестовое задание для компании ООО Айти - Альбион.

Стек: 
- django==2.2.2
- m3-django-compat==1.9.2
- m3-objectpack==2.2.47

Реализовано:

-  GUI интерфейс CRUD операций для моделей: ContentType, User, Group, Permission.
-  В справочнике для Permission работает выбор ContentType через выпадающий список.
-  Для модели User, реализовано окно редактирования и добавления записи ручным способом, описанным в https://objectpack.readthedocs.io/ru/latest/tutorial.html#id8
-  Создан файл setup.py для сборки пакета и распространения.
-  Описан файл .gitignore, исключающий файлы *.pyc директорию *.egg-info и файл бд sqlite
-  Размещен проект на github.


