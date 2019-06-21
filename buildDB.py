#! python3
import json

d = """{
    "_id": {
        "$oid": "569190ca24de1e0ce2dfcd4f"
    },
    "title": "Once Upon a Time in the West",
    "year": 1968,
    "rated": "PG-13",
    "released": {
        "$date": "1968-12-21T05:00:00.000Z"
    },
    "runtime": 175,
    "countries": [
        "Italy",
        "USA",
        "Spain"
    ],
    "genres": [
        "Western"
    ],
    "director": "Sergio Leone",
    "writers": [
        "Sergio Donati",
        "Sergio Leone",
        "Dario Argento",
        "Bernardo Bertolucci",
        "Sergio Leone"
    ],
    "actors": [
        "Claudia Cardinale",
        "Henry Fonda",
        "Jason Robards",
        "Charles Bronson"
    ],
    "plot": "Epic story of a mysterious stranger with a harmonica who joins forces with a notorious desperado to protect a beautiful widow from a ruthless assassin working for the railroad.",
    "poster": "http://ia.media-imdb.com/images/M/MV5BMTEyODQzNDkzNjVeQTJeQWpwZ15BbWU4MDgyODk1NDEx._V1_SX300.jpg",
    "imdb": {
        "id": "tt0064116",
        "rating": 8.6,
        "votes": 201283
    },
    "tomato": {
        "meter": 98,
        "image": "certified",
        "rating": 9,
        "reviews": 54,
        "fresh": 53,
        "consensus": "A landmark Sergio Leone spaghetti western masterpiece featuring a classic Morricone score.",
        "userMeter": 95,
        "userRating": 4.3,
        "userReviews": 64006
    },
    "metacritic": 80,
    "awards": {
        "wins": 4,
        "nominations": 5,
        "text": "4 wins \u0026 5 nominations."
    },
    "type": "movie"
}"""

x = json.loads(d)
