Проект представляет собой систему управления обучением (Learning Management System, LMS), предназначенную для
организации учебного процесса.


Модели данных:
Пользователи, платежи (Users, Payments).
Курсы (Course).
Уроки (Lesson).
Использование реляционной СУБД (PostgreSQL).
Записал в таблицу(course_course), соответствующую этой модели данные через json файл
(скрины успешной записи в БД прикреплены к фотрме сдачи ДЗ).
Для сериализатора для модели курса реализовано поле вывода уроков. 
Вывод реализован с помощью сериализатора для связанной модели.
Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:
менять порядок сортировки по дате оплаты,
фильтровать по курсу или уроку,
фильтровать по способу оплаты.

Для запуска приложения необходимо установить зависимости, указанные в файле pyproject.toml, 
загрузить приложенные фикстуры.

[Репозиторий на GitHub](https://github.com/Khapaevv/drf_project)
