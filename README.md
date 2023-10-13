# О проекте

Проект по получению вопросов для викторины с публичного API.

Функционал:
* получение от публичного API определенного количества вопросов. 
* получить все записанные вопросы из базы данных.


# Оглавление

[Requirements](#Requirements) <br>
[Запуск проекта](#Запуск-проекта) <br>
[Создание среды разработки](#Создание-сред-разработки) <br>
[Используемые технологии](#Используемые-технологии) <br>
[Примеры запросов](#Примеры-запросов) <br>

# Requirements

* Python 3.10
* Docker 20.10+ [(инструкция по установке)](https://docs.docker.com/get-docker/).

# Клонирование репозитория
Склонируйте репозиторий git clone git@github.com:SergoSolo/quiz_questions.git

# Запуск проекта

Все команды выполняются из корневой директории проекта.

<details>
<summary>Проверка docker</summary>
<br>
По умолчанию проект запускается в докере. Для начала нужно убедиться, что докер
установлен. Открой любой терминал и выполни следующую команду:

```shell
docker --version
```
Должна быть выведена версия докера, это выглядит примерно так:
```
Docker version 20.10.21, build baeda1f
```
Если докер не установлен, то установите его, следуя [инструкции](https://docs.docker.com/get-docker/).
</details>

<details>
<summary>Настройка переменных окружения</summary>
<br>

Переменные окружения проекта хранятся в файле `.env` , для которого есть шаблон `.env.template`.
Создай в корне проекта файл `.env` простым копированием файла `.env.template`.

</details>

<details>
<summary>Запуск сервисов</summary>
<br>
<hr>

Для запуска проекта выполни следующую команду:
```
docker-compose up --build -d
```

Убедимся, что все контейнеры запущены:
```
docker-compose ps
```

Результат должен быть примерно такой (список сервисов может отличаться, но статус всех сервисов
должен быть `running`):
```
NAME                COMMAND                  SERVICE             STATUS              PORTS
quiz_api            "sh -c 'alembic upgr…"   api                 running             0.0.0.0:8000->8000/tcp
quiz_db             "docker-entrypoint.s…"   db                  running             0.0.0.0:5432->5432/tcp
```

Каждый ресурс описан в документации: точки доступа (адрес для выполнения запроса), типы запросов, вспомогательные параметры.
Проект с полным описанием доступен по ссылке http://localhost:8000/docs или http://localhost:8000/redoc.

Остановить и удалить запущенные контейнеры:
```
docker-compose down
```

</details>

<details>
<summary>Примеры запросов.</summary>
<br>

POST запрос к публичнму API.
Запрос на http://localhost:8000/api/questions/:

```
{
  "questions_num": 25,
}
```
В результате ответом на запрос вы получите предыдущий сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

```
{
  "question_id": 145456,
  "question": "Reggie Love represents 11-year-old Mark Sway, the title character of this legal thriller",
  "answer": "<i>The Client</i>",
  "created_at": "2022-12-30T20:28:59.900000"
}
```

GET запрос для получения списка вопросов. Мы можем ограничить вывод количества вопросов на 1 странице или перейти на другу страницу с помощью параметров size и page.
Запрос на http://localhost:8000/api/questions/get_all?page=1&size=3:

```
{
    "items": [
        {
            "question_id": 31230,
            "question": "Legend says Veal Oscar was named for this Scandinavian country's King Oscar II, who liked to eat it",
            "answer": "Sweden",
            "created_at": "2022-12-30T18:50:27.225000"
        },
        {
            "question_id": 176812,
            "question": "In 2015 this state U. of N.J. was down 7 & spiked the ball to stop the clock with 3 ticks left; problem was, it was already 4th down",
            "answer": "Rutgers",
            "created_at": "2022-12-30T21:13:24.085000"
        },
        {
            "question_id": 12853,
            "question": "Since a chariot of fire took him up to heaven, it's a long trip back on Passover for the wine",
            "answer": "Elijah",
            "created_at": "2022-12-30T18:42:48.598000"
        }
    ],
    "total": 285,
    "page": 1,
    "size": 3,
    "pages": 95
}
```
Если сделать запрос без параметров(http://localhost:8000/api/questions/get_all), то выведет список из 50(значение по умолчанию) вопросов.

</details>

##  Используемые технологии:
- Python version 3.10
- FastAPI
- Alembic
- SQLAlchemy
- Pydantic
- Aiohttp


## Автор:
> [Sergey](https://github.com/SergoSolo)