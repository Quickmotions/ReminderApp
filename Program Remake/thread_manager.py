def check_reminders(reminders):
    from notification_manager import send_notification
    from time_manager import get_datetime
    # check reminders against current time/date
    current_datetime = get_datetime()
    for each in reminders:
        if each.strftime('%H:%M:%Y:%m:%d') == current_datetime.strftime('%H:%M:%Y:%m:%d'):
            send_notification(each)




