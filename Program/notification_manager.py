def send_notification(reminder):
    # import dependencies
    from pynotifier import Notification
    Notification(
        title=f'{reminder.name} at {reminder.datetime}',
        description=f'Reminder: {reminder.name} at {reminder.datetime},\\'
                    f' notified on a {reminder.repeat} basis',
        duration=10,  # Duration in seconds
        urgency='normal'
    ).send()
    print('DEBUG: NOTIFICATION SENT')  # debug
