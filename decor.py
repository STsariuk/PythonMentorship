import time
from datetime import datetime
from typing import Callable


def calculate_time_execution(func: Callable):
    def wrapper(*args, **kwargs):
        start = datetime.now()

        try:
            func(*args, **kwargs)
        except Exception as err:
            print('we go error: ', err)

        finish = datetime.now() - start
        print("Total time of func execution is: ", str(finish))

    return wrapper


@calculate_time_execution
def calculate(*args, **kwargs):
    print('Start calculating, with: ', args, kwargs)
    raise Exception("My custom exception")
    time.sleep(8)
    print('Finish calculating...')


if __name__ == "__main__":
    calculate(1, 2, 3, hello=True)






"""
1) create function for handling response (print all items)
2) Create decorator - and check if user has group `admin_users` - 
    if yes -> call function
    if not -> return not authorized
"""


response = {
    "status_code": 200,
    "msg": "OK",
    "groups": ["auth_users", "admin_users"],
    "ts": datetime.now()
}