Небольшой HTTP сервис для работы с импортируемыми данными.

Пользователь загружает файл .csv через кнопку на главном меню, файл загружается в базу данных. После этого пользователя перенаправляет на главную страницу, где выведен список файлов по 3 штуки на страницу. В данном списке есть информация о названии файла и колонках файла.
В главном меню можно удалить уже ранее созданный файл через соответствующую кнопку, а также просмотреть содержимое через кнопку посмотреть содержимое. Если открыть содержимое файла, то содержимое можно будет сортировать по колонкам и фильтровать по словам, а также настраивать количество отображения данных.
Реализована регистрация пользователя, вход и выход через соответствующие кнопки в главном меню, а также незарегистрированным пользователям нельзя загружать файл и просматривать содержимое файла.

Информация по развертыванию
1) Необходимо установать через пакетный менеджер pip файл requirements.txt
2) Настроить базу данных (у меня использовалась PostgreSQL)
3) Создать .env файл на основании файла .env sample
4) Запустить Django сервер 
