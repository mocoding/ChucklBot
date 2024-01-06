"""
unit test to test program life-lines.

- test if fuzzy matching -> dict() still works
- test get_joke, api call.

"""

from src.main import respond_to_input
from src.call_api import get_joke
from resources.commands_data import commands


def test_greetings_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('hello there')  # for category: greetings

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['greetings']['responses']


def test_farewells_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('ciao')  # for category: farewells

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['farewells']['responses']


def test_compliments_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('well done')  # for category: compliments

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['compliments']['responses']


def test_encouragement_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('Im sad')  # for category: encouragement

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['encouragement']['responses']


def test_smalltalk_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('whats going on?')  # for category: smalltalk

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['smalltalk']['responses']


def test_random_category():
    # testing bot response accuracy.
    bot_response = respond_to_input('random fact')  # for category: smalltalk

    # test pass if bot response is in any of the categories responses
    assert bot_response in commands['random']['responses']


# TODO: not sure if that test makes sense! How do I test for joke not in/in tuple?
def test_save_joke():
    # testing save joke function.
    bot_response = respond_to_input('love it')

    assert bot_response == 'Since you like this joke so much. I have saved it.' or 'You have no favorite jokes, yet!'


def test_get_joke():
    # testing api call with correct endpoint.
    api_response = get_joke()

    assert api_response != 'error'


def test_get_joke_error_handling():
    # testing api call with fatal endpoint.
    api_response = get_joke('https://fake_api_endpoint.com')

    assert api_response == 'error'
