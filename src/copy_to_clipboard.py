import logging as log
import pyperclip as clip
import random

from resources.commands_data import commands
from .call_api import get_last_joke as last_joke
from .favorite import get_favorite


def copy_to_clipboard(last_match):
    # check first if last_match was 'get_favorite'.
    if last_match == "get_favorite":

        # fetch favorite joke from favorite_jokes.json
        try:
            joke, joke_id = get_favorite()  # get favorite joke and joke_id.
        except ValueError as e:
            # handling: if jason file is compromised.
            return f"Oh no - I had a problem fetching your favorite joke."

        try:
            # check if favorite joke is already in clipboard.
            if clip.paste() == f"{joke}(by ChucklBot)":
                return f"Your favorite joke is already in your clipboard."

            joke = joke + "(by ChucklBot)"  # add (by ChucklBot).
            clip.copy(joke)  # copy joke to clipboard.
            log.info("copy_to_clipboard(): Favorite joke copied to clipboard. joke_id: %s", joke_id)  # log success with joke_id.
            randomize_response = random.randint(0, len(commands['clipboard_copy']) - 1)
            return f"{commands['clipboard_copy']['responses'][randomize_response]}"
        except clip.PyperclipException as e:
            # handle clipboard exception.
            log.error("copy_to_clipboard(): Exception copy to clipboard, favorite: %s", e)
            return f"Ouch - I have a problem copying this joke to your clipboard."

    # else: get last_joke, as last joke is not favorite.
    else:
        try:
            joke, joke_id = last_joke()  # retrieve last joke.
        except Exception:
            return f"Sorry - Failed to fetch joke."

        if joke is None:  # no joke to copy.
            return f"Yo - nothing to copy."
        elif joke == "error":  # exception caused in last_joke().
            log.error("copy_to_clipboard(): joke == 'error', exception in last_joke().")
            return f"Ouch - I have a problem copying your last joke."

        # check if joke is already in clipboard.
        elif clip.paste() == f"{joke}(by ChucklBot)":
            return f"That joke is already in your clipboard."

        # copy joke in clipboard
        else:
            try:
                copy_joke = joke + "(by ChucklBot)"  # add (by ChucklBot).
                clip.copy(copy_joke)
                log.info("copy_to_clipboard(): Joke copied to clipboard. joke_id = %s", joke_id)
                randomize_response = random.randint(0, len(commands['clipboard_copy']) - 1)
                return f"{commands['clipboard_copy']['responses'][randomize_response]}"
            except clip.PyperclipException as e:
                # handle clipboard exception.
                log.error("copy_to_clipboard(): Exception copy to clipboard: %s", e)
                return f"Ouch - I have a problem copying this joke to your clipboard."
