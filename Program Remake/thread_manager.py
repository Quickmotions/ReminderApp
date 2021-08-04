def check_reminders(reminders, current_datetime):
    from notification_manager import send_notification

    # check reminders against current time/date
    for each in reminders:
        if each.strftime('%H:%M:%Y:%m:%d') == current_datetime.strftime('%H:%M:%Y:%m:%d'):
            send_notification(each)




