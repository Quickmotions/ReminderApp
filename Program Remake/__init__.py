if __name__ == '__main__':
    # import python files
    from file_manager import create_reminders
    from thread_manager import check_reminders
    from time_manager import get_datetime

    # import built-in modules
    from time import sleep
    from threading import Thread

    reminders = create_reminders()

    time_thread = Thread(target=check_reminders, args=[reminders, get_datetime])
    time_thread.start()
