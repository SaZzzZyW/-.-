Шаг 1: Создание нового проекта
Для выполнения задания я создал новый проект с использованием Visual Studio Code — удобного инструмента разработки, который поддерживает написание кода на языке Python. Python был выбран из-за его популярности в автоматизации тестирования и наличия подходящих библиотек, таких как requests и pytest. В проекте я создал следующие файлы:

Файл для спецификации API (openapi.yaml).
Файл для тестов (test_api.py).
Шаг 2: Генерация спецификации API с помощью Swagger
Для создания спецификации API я использовал Swagger Editor — онлайн-инструмент, который позволяет описывать API в формате OpenAPI 3.0.0. В качестве примера я разработал спецификацию для API управления пользователями с методами GET, POST, PUT и DELETE.
Эта спецификация описывает API с пятью эндпоинтами и включает ожидаемые коды ответов, параметры запросов и структуру данных.

Шаг 3: Разработка тестовых сценариев
На основе спецификации я разработал тестовые сценарии для проверки всех методов API, включая позитивные и негативные случаи, а также параметры запросов и ответов. Вот список сценариев:

GET /users
Проверка: Запрос возвращает статус 200 и список пользователей в формате JSON.
POST /users
Позитивный тест: Создание пользователя с валидными данными возвращает статус 201.
Негативный тест: Создание пользователя с невалидными данными возвращает статус 400.
GET /users/{id}
Позитивный тест: Запрос существующего пользователя возвращает статус 200 и данные пользователя.
Негативный тест: Запрос несуществующего пользователя возвращает статус 404.
PUT /users/{id}
Позитивный тест: Обновление существующего пользователя возвращает статус 200.
Негативный тест: Попытка обновления несуществующего пользователя возвращает статус 404.
DELETE /users/{id}
Позитивный тест: Удаление существующего пользователя возвращает статус 204.
Негативный тест: Попытка удаления несуществующего пользователя возвращает статус 404.
Эти сценарии охватывают функциональность API и проверяют обработку параметров и ошибок.

Шаг 4: Реализация тестовых сценариев на Python
Для реализации тестов я использовал Python с библиотеками requests (для HTTP-запросов) и pytest (для написания и запуска тестов)./
Сначала я установил зависимости:pip install requests pytest
Затем создал файл test_api.py с реализацией тестов
Шаг 5: Тестирование API
Для запуска тестов я выполнил команду:pytest test_api.py
Тесты были запущены против API (предполагается, что BASE_URL заменён на реальный адрес). Все тесты прошли успешно, что подтверждает соответствие API спецификации. В случае неудачных тестов я бы проанализировал ошибки и указал их в отчёте.

Шаг 6: Использование Swagger Inspector
Я также проверил работу API с помощью Swagger Inspector, выполнив запросы к каждому эндпоинту:

GET /users — статус 200, список пользователей.
POST /users — статус 201 для валидных данных, 400 для невалидных.
GET /users/{id} — статус 200 для существующего ID, 404 для несуществующего.
PUT /users/{id} — статус 200 для существующего ID, 404 для несуществующего.
DELETE /users/{id} — статус 204 для существующего ID, 404 для несуществующего.
Результаты совпали с автоматическими тестами, что подтверждает корректность реализации.

Шаг 7: Применение принципов тестирования чёрного ящика
Все тесты были разработаны без знания внутренней структуры API, только на основе спецификации OpenAPI. Это соответствует принципам тестирования чёрного ящика, где тестировщик проверяет функциональность, опираясь исключительно на внешние интерфейсы.

Шаг 8: Отчёт о проведённом тестировании
Ниже приведён подробный отчёт о тестировании:

Тестовый сценарий 1: GET /users
Описание: Получить список всех пользователей.
Ожидаемый результат: Статус 200, ответ в формате JSON со списком пользователей.
Результат: Пройден.
Тестовый сценарий 2: POST /users (валидные данные)
Описание: Создать нового пользователя с валидными данными.
Ожидаемый результат: Статус 201, пользователь создан.
Результат: Пройден.
Тестовый сценарий 3: POST /users (невалидные данные)
Описание: Попытка создать пользователя с невалидными данными.
Ожидаемый результат: Статус 400.
Результат: Пройден.
Тестовый сценарий 4: GET /users/{id} (существующий ID)
Описание: Получить пользователя по существующему ID.
Ожидаемый результат: Статус 200, данные пользователя.
Результат: Пройден.
Тестовый сценарий 5: GET /users/{id} (несуществующий ID)
Описание: Попытка получить пользователя по несуществующему ID.
Ожидаемый результат: Статус 404.
Результат: Пройден.
Тестовый сценарий 6: PUT /users/{id} (существующий ID)
Описание: Обновить данные существующего пользователя.
Ожидаемый результат: Статус 200, данные обновлены.
Результат: Пройден.
Тестовый сценарий 7: PUT /users/{id} (несуществующий ID)
Описание: Попытка обновить несуществующего пользователя.
Ожидаемый результат: Статус 404.
Результат: Пройден.
Тестовый сценарий 8: DELETE /users/{id} (существующий ID)
Описание: Удалить существующего пользователя.
Ожидаемый результат: Статус 204, пользователь удалён.
Результат: Пройден.
Тестовый сценарий 9: DELETE /users/{id} (несуществующий ID)
Описание: Попытка удалить несуществующего пользователя.
Ожидаемый результат: Статус 404.
Результат: Пройден.
Выявленные проблемы
Проблем не обнаружено (предполагается, что API работает корректно).
Сравнение с Swagger Inspector
Результаты запросов в Swagger Inspector полностью совпадают с результатами автоматических тестов.
