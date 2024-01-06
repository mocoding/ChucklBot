"""

TODO: store multiple jokes and randomly picking one as return.
TODO: unit - test!

"""
import json
import logging as log

from pathlib import Path
from .call_api import get_last_joke as last_joke


def save_favorite():
    try:
        joke, joke_id = last_joke()  # get last joke and joke_id/NONE if empty joke tuple.
    except Exception:
        log.error("save_favorite(): System Error in last_joke().")
        return f"Sorry, I had a problem fetching your joke."

    if joke is None:  # tuple empty == no joke.
        log.warning("save_favorite(): joke value is None. last_joke(): %s", joke)
        return f"You have no favorite joke, yet!"
    else:
        try:
            path = Path('../resources/favorite_jokes.json')  # file path via Path object
            content = json.dumps(last_joke())  # serializes dict last_joke into JSON formatted string.
            path.write_text(content)  # write JSON string in JSON file.
            log.info("save_favorite(): Joke saved as favorite: joke_id: %s", joke_id)  # log success.

            return (f"Since you like this joke so much. I have saved it. \n"
                    f"Just ask: 'favorite'.")
        except IOError as e:
            # handle IO (most common) file exceptions.
            log.error("save_favorite(): JSON file exception in saving favorite joke: %s", e)
            # raise IOError("Oh no - I had a problem remembering this joke") from e
            return f"Oh oh - I had a problem remembering this joke."


def get_favorite():
    path = Path('../resources/favorite_jokes.json')

    if path.exists():
        content = path.read_text()

        if not content:
            log.error("get_favorite(): favorite_jokes.json exists, but is empty")
            return f"You have no favorite joke, yet.", None  # main expects two values -> return an extra none.
        try:
            joke = json.loads(content)
            log.info("get_favorite(): Favorite joke successfully fetched. joke_id: %s", joke[1])  # log success.
            return joke  # return joke and joke_id as list.
        except ValueError as e:
            # handle format exceptions in the json.
            log.error("get_favorite(): ValueError fetching favorite joke: %s", e)
            raise ValueError("Oh no, I had a problem fetching your favorite joke") from e
            # return f"Oh no, I had a problem fetching your favorite joke.", None  # main expects two values.

    else:  # no json == no jokes saved.
        log.warning("get_favorite(): No file: favorite_jokes.json.")
        return f"Oh - You have no favorite joke, yet.", None  # main expects two values -> return an extra none.
