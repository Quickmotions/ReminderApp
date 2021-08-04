def send_notification(reminder):
    # import dependencies
    from pynotifier import Notification
    Notification(
        title=f'{reminder.name} at {reminder.datetime.strftime("%H:%M")}',
        description=f'Reminder: {reminder.reminder} at {reminder.datetime.strftime("%H:%M")},\\'
                    f' notified on a {reminder.repeat} basis',
        duration=10,  # Duration in seconds
        urgency='normal'
    ).send()
    print('DEBUG: NOTIFICATION SENT')  # debug
