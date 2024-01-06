"""
unit test to test program life-lines.

- test if fuzzy matching with resources.commands_data dict() works.
- test get_joke api call.
- test get_favorite function.

"""
import pytest

from src.main import respond_to_input
from src.call_api import get_joke
from resources.commands_data import commands
from src.favorite import get_favorite


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


def test_save_joke():
    # testing save joke function.
    bot_response = respond_to_input('love it')

    assert bot_response == 'Since you like this joke so much. I have saved it.' or 'You have no favorite jokes, yet!'


def test_get_joke():
    # testing api call with correct endpoint.
    try:
        api_response = get_joke()
    except Exception as e:
        # if any exception is raised, the test will fail.
        pytest.fail(f"Unexpected exception in get_joke(): {e}")


def test_get_joke_error_handling():
    # testing api call with fatal endpoint.
    # with pytest.raises(Exception) checks if any exception of type 'Exception' or its subclass is raised in the block.
    with pytest.raises(Exception):
        get_joke('https://fake_api_endpoint.com')  # if get_joke raises an exception the test will pass.


def test_get_favorite_check_for_exception():
    # testing get_favorite(), no exception expected. Regardless of file exist / not exist.
    try:
        api_response = get_favorite()
    except Exception as e:
        pytest.fail(f"Unexpected exception in get_favorite(): {e}")
