# import python files
from file_manager import create_reminders
from time_manager import get_datetime, check_reminders

# import built-in modules
from time import sleep
from threading import Thread
restart = False


if __name__ == '__main__':
    reminders = create_reminders()
    for each in reminders:
        print(each.name, each.datetime, each.repeat)
    while True:  # 1 min loop
        reminders = create_reminders()
        restart = False
        while not restart:
            return_value = check_reminders(reminders)
            if return_value == "reset":
                restart = True
            sleep(60)
