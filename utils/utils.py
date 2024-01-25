import inspect

# CONSTANTS

URL = "https://eleven36.com/login"
URL1 = "https://lambdatest.github.io/sample-todo-app/"
USERNAME = "sgka6475@gmail.com"
PASSWORD = "Test@2006"


def whoami():
    return inspect.stack()[1][3]