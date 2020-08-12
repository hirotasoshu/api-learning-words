[![Build Status](https://travis-ci.com/hirotasoshu/api-learning-words.svg?token=SqxTxzNQY6mpjoxotPcj&branch=master)](https://travis-ci.com/hirotasoshu/api-learning-words)
[![CodeFactor](https://www.codefactor.io/repository/github/hirotasoshu/api-learning-words/badge?s=3cb14a95d0bf4e70e4edbf9825a79cdd8979a71d)](https://www.codefactor.io/repository/github/hirotasoshu/api-learning-words)
[![codecov](https://codecov.io/gh/hirotasoshu/api-learning-words/branch/master/graph/badge.svg)](https://codecov.io/gh/hirotasoshu/api-learning-words)
====================
This project is implimenting REST API and django admin panel for a mobile app for learning English words.

Dev version is using django development server and sqlite3.

Prod version is using gunicorn+nginx and PostgreSQL.

Demo version launched [here](http://164.90.237.142/api/). (API_SECRET in demo: `ya_obyazatelno_proidu`)

## Dev version :building_construction:

Default API_SECRET: `t3st`. You can change it in `app/learning_words/settings/dev.py`.
```
docker-compose up --build -d
docker-compose run --entrypoint /migrate.sh --rm web
docker-compose run --entrypoint /createsuperuser.sh --rm web
```
### Tests :white_check_mark:
```
docker-compose run -e DJANGO_SETTINGS_MODULE=learning_words.settings.testing --rm web pytest -vv
```


## Prod version :rocket:

Default environment variables are defined in .example.env. You can define yours by creating your .env file (Don't forget to change env_file in docker-compose.prod.yml in db and web services).

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --entrypoint /migrate.sh --rm web
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --entrypoint /collectstatic.sh --rm web
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --entrypoint /createsuperuser.sh --rm web
```

# API

All requests should have 'Secret' header that equals to API_SECRET, otherwise you will get 403 status code.

## List categories

**URL**: `/api/categories/`

**METHOD**: `GET`

**RESPONSE EXAMPLE:**
```json
[
    {
        "id": 1,
        "name": "Фразовые глаголы",
        "icon": "http://164.90.237.142/media/icons/phrasal_verbs.jpg"
    }
]
```

## List levels

**URL**: `/api/levels/`

**METHOD**: `GET`

**RESPONSE EXAMPLE:**
```json
[
    {
        "id": 1,
        "name": "Elementary",
        "code": "A1"
    }
]
```

## List themes

**URL**: `/api/themes/`

**METHOD**: `GET`

**QUERY PARAMS:**

`category`:`integer`

`level`:`integer`

**RESPONSE EXAMPLE:**
```json
[
    {
        "id": 1,
        "category": 1,
        "level": 1,
        "name": "Relationship",
        "photo": "http://164.90.237.142/media/photos/relationship.png"
    }
]
```

## Retrieve theme

**URL**: `api/themes/:pk/`

**URL Parameters**: `pk=[integer]` where `pk` is the ID of the Theme on the server.

**METHOD**: `GET`

**RESPONSE EXAMPLE:**
```json
{
    "id": 1,
    "category": 1,
    "level": 1,
    "name": "Relationship",
    "photo": "http://164.90.237.142/media/photos/relationship.png",
    "words": [
        {
            "id": 1,
            "name": "to ask out"
        }
    ]
}
```

## Retrieve word

**URL**: `api/words/:pk/`

**URL Parameters**: `pk=[integer]` where `pk` is the ID of the Word on the server.

**METHOD**: `GET`

**RESPONSE EXAMPLE:**
```json
{
    "id": 1,
    "name": "to ask out",
    "translation": "Пригласить на свидание",
    "transcription": "tuː ɑːsk aʊt",
    "example": "John has asked Mary out several times.",
    "sound": "http://164.90.237.142/media/sounds/1.mp3"
}