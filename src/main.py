"""

TODO: ask and store name for personaliziation.

"""

import difflib
import random
import logging as log

from src.call_api import get_joke
from src.favorite import save_favorite as favorite
from src.favorite import get_favorite
from resources.commands_data import commands
from src.copy_to_clipboard import copy_to_clipboard as copy
from src.print_intro_message import print_intro_message as intro

# last_match stores the last commands_data category matched via fuzzy matching.
last_match = ""  # for example: "jokes" or "get_favorite".


def respond_to_input(user_input):
    global last_match

    for category, content in commands.items():

        """
        using built-in fuzzy matching algo.  
        'get_close_matches' compares a string with a list. 
        n = closest match string gets returned. cutoff = similarity threshold, 1 = exact match.
        returns a list. match is an empty list if there is no match.
        """
        match = difflib.get_close_matches(user_input, content['commands'], n=1, cutoff=0.6)
        # log.debug("respond_to_input(): match %s", match)  # debug: log match.

        if match:  # if match has any value. check the category that we are currently in.

            if category == 'jokes':
                last_match = category
                randomize_response = random.randint(0, len(commands['jokes']['responses']) - 1)

                try:
                    joke = get_joke()
                    return f"{commands['jokes']['responses'][randomize_response]}\n{joke}"
                except Exception as e:
                    log.error("respond_to_input(): if match: category == jokes -> get_joke(): %s", e)
                    return f"Ouch - I had a problem fetching a joke."

            elif category == 'clipboard_copy':
                return copy(last_match)
            elif category in ('store_favorite', 'get_favorite'):
                if category == 'store_favorite':
                    return favorite()
                else:
                    last_match = category

                    try:
                        joke, _ = get_favorite()  # only get joke and not joke_id from favorite return list.
                        return joke
                    except ValueError as e:
                        # handling: if jason file is compromised.
                        return f"Oh no - I had a problem fetching your favorite joke."

            elif category in commands:
                last_match = category
                randomize_response = random.randint(0, len(commands[category]['responses']) - 1)
                return f"{commands[category]['responses'][randomize_response]}"

    # log: user_input if no category match is found.
    log.warning("respond_to_input(): no category match. user_input = %s", user_input)
    return "Hmm, I'm scratching my circuits over here! Maybe try tickling me with a 'tell me a joke' request?"


def main():
    # logging configuration.
    # filemode a == append -> add to existing file. level DEBUG == lowest level and accepts every log entry.
    log.basicConfig(filename='../test/application.log', filemode='a', level=log.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

    # set logger for requests library to WARNING to not get all debugging info on our api calls.
    log.getLogger('urllib3').setLevel(log.WARNING)

    log.info("- session start -")  # log: start of user session.

    # loop to keep the chatbot running until user makes a farewell command.
    while True:
        user_input = input("You: ")  # remember: input() has to be in __main__, otherwise PyTest doesn't work.
        response = respond_to_input(user_input)
        print("Bot:", response)
        if user_input in commands['farewells']['commands']:
            log.info("- session end -")  # log: end of user session.
            break


if __name__ == '__main__':
    # ChucklBot introduction -> print_intro_message.py
    print(intro())

    # run main() in try to catch graceful user termination.
    try:
        main()
    except KeyboardInterrupt:
        log.warning("except KeyboardInterrupt - User terminated app.")  # log: user termination.
