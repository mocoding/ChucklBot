🤖 ChucklBot 🤖 V1.0 (initial release)
------------------------------------------------------------------------------------------------------
A command-line-based chatbot that can tell jokes and engage in simple small talk.

Note: Start -> src/main.py.
Unit tests for the program are under test_boy.py.

Implementation:
Chat-Bot is realized with a dictionary and difflib.get_close_matches() for fuzzy matching.
Jokes are sourced by connecting to a public API (https://v2.jokeapi.dev/) and are displayed by reading from a JSON.
Strong focus on testing with simple unit testing via PyTest, Try/Except blocks, and logging.

Current Features:

- Telling jokes.
- Favorite: Saving and retrieving a favorite joke in JSON format.
- Ability to copy a joke to the clipboard.
- Extensive logging, edge case handling, and error management.
- Unit tests for critical functions.

Further features in Development:

- More personalization: Using the acceptance and storage of names for personalization.
