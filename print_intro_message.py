# reads out and returns INTRO_MESSAGE.txt for bot introduction.
def print_intro_message():
    # 'with open' file handler the file is automatically closed when code is run or any exceptions happen.
    with open('INTRO_MESSAGE.txt', 'r') as intro:
        return intro.read()
