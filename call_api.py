"""

TODO: put category in response for more accurate description of joke from BOT.
TODO: create a 'get all jokes' to give information about all jokes ever told in this session. use tuple, count and fetch.

"""
import logging as log
import requests as request

# api endpoint to fetch joke -> receive JSON.
api_endpoint = ("https://v2.jokeapi.dev/joke/Any?lang=en&"
                "blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
jokes = ()  # tuple to store jokes.


# function to get joke via jokeapi.dev api.
def get_joke(test_api_endpoint=None):
    global jokes, api_endpoint  # declare global variables.

    # unit test: sets api_endpoint to fake URL for testing -> see test_get_joke_error_handling()
    if test_api_endpoint:
        api_endpoint = test_api_endpoint

    try:
        while True:  # create an infinite loop, to keep looking for a new joke.
            r = request.get(api_endpoint)
            if r.status_code != 200:  # API availibility check.
                log.error("Error message: %s", r.status_code)
                raise SystemError('Ups. API is down.')

            joke_dict = r.json()  # API response -> dict().
            joke_id = joke_dict['id']  # get joke_id to store in jokes tuple.

            if joke_id not in jokes:  # if joke has not been used yet (is not in jokes tuple.)
                jokes = jokes + (joke_dict['id'],)  # add id to jokes tuple.
                log.info("Joke successfully fetched. Joke ID: %s", joke_dict['id'])  # log
                return joke_dict['joke']  # exit loop with joke.

    except request.exceptions.RequestException as e:
        # handle api request exception.
        log.exception("Error message: %s", e)
        return f"error"


# get the last joke.
def get_last_joke():
    global jokes  # declare global variable.

    if jokes == ():  # if tuple is empty, no jokes can be retrieved.
        log.warning("get_last_joke(): Joke tuple is empty.")
        return f"nojoke", None
    else:
        last_id = str(jokes[len(jokes) - 1])  # get id of last joke.
        # log.debug("get_last_joke(): jokes tuple, last_id: %s", last_id)  # debugging. check accuracy of last joke id.

        try:
            last_joke_endpoint = f"{api_endpoint}&idRange={last_id}"  # create api endpoint to get joke by ID.
            r = request.get(last_joke_endpoint)

            if r.status_code != 200:  # API availibility check.
                # if status_code not 200. log error.
                log.error("get_last_joke(): request status_code error: %s", r.status_code)
                raise SystemError('Ups. API is down.')

            joke_dict = r.json()  # store api load in dict().
            value = (joke_dict['joke'], last_id)
            return value  # return joke and joke_id as list.
        except request.exceptions.RequestException as e:
            # handle get last joke _ api request exception.
            log.exception("get_last_joke(): API exception: %s", e)
            return f"error", None
