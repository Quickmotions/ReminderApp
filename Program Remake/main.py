if __name__ == '__main__':
    # import python files
    from file_manager import create_reminders
    from thread_manager import check_reminders
    from time_manager import get_datetime

    # import built-in modules
    from time import sleep
    from threading import Thread

    reminders = create_reminders()
    while True:  # 1 min loop
        check_reminders(reminders, current_datetime)
        sleep(60)
