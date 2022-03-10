def get_datetime():
    from datetime import datetime
    current_datetime = datetime.now()
    return current_datetime


def check_reminders(reminders):
    from notification_manager import send_notification
    from time_manager import get_datetime, update_times
    # check reminders against current time/date
    current_datetime = get_datetime()
    for each in reminders:
        if each.datetime == current_datetime.strftime('%H:%M:%Y:%m:%d'):
            send_notification(each)
            update_times(reminders)
            return "reset"
    return None


def update_times(reminders):
    from datetime import datetime, timedelta
    from file_manager import update_reminders
    current_datetime = get_datetime()
    new_dts = []
    for each in reminders:
        if int(current_datetime.strftime('%H')) >= int(each.datetime.strftime('%H')) \
                and int(current_datetime.strftime('%M')) >= int(each.datetime.strftime('%M')):
            if each.repeat == "hourly":
                time_to_add = timedelta(hours=1)
            if each.repeat == "daily":
                time_to_add = timedelta(days=1)
            if each.repeat == "weekly":
                time_to_add = timedelta(days=7)
            if each.repeat == "monthly":
                time_to_add = timedelta(months=1)
            if each.repeat == "yearly":
                time_to_add = timedelta(years=1)
            try:
                new_dts.append(each.datetime + time_to_add)
            except:
                print("missing repeat")
        else:
            new_dts.append(each.datetime)
    update_reminders(reminders, new_dts)
