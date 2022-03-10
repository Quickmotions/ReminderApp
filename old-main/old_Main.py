# other files
from time_manage import update_reminder_times
# built in imports
from time import sleep
import threading as th
from datetime import datetime
# dependencies
from pynotifier import Notification


class FileManager:
    def __init__(self, f_line=None, create_new=False):
        if create_new:
            self.create_new()
        else:
            f_line = f_line.strip('\n').split(',')
            self.name = f_line[0]
            self.datetime = f_line[1]
            self.repeat = f_line[2]
            print(self.date)

            print(self.date)

    def create_new(self):
        print('Create a new Reminder:') # need to convert date and time into datetime object
        self.name = input('Reminder Name: ')
        self.datetime = input('Reminder Time (HH:MM): ')
        print('Reminder Repeat Options:\n-hourly\n-daily\n-weekly\n-monthly\n-yearly,')
        self.repeat = input('Reminder Repeat: ')
        with open('Storage\\reminders.csv', 'a') as f:
            f.write(f'{self.name},{self.time},{self.date},{self.repeat}\n')


def time_manager(r_list):
    while True:
        current_datetime = datetime.now()
        # print time and date
        print(current_datetime.strftime('%H:%M'), current_datetime.strftime('%Y:%m:%d'))
        # check times
        check_reminders(r_list, current_datetime)
        # check each min
        sleep(60)

\
def check_reminders(r_list, datetime_now):

    # update timers that have expired
    for reminder in r_list:
        reminder.update_reminder_times(reminder.) # need to insert date time object and assign output to class object

    # check reminders against current time/date
    for reminder in r_list:
        if reminder.time == datetime_now.strftime('%H:%M') and reminder.date == datetime_now.strftime('%Y:%m:%d'):
            # send customised notification
            Notification(
                title=f'{reminder.name} at {reminder.time}',
                description=f'Reminder: {reminder.reminder} at {reminder.time}, notified on a {r.repeat} basis',
                duration=10,  # Duration in seconds
                urgency='normal'
            ).send()
            print('DEBUG', reminder.name, reminder.time, reminder.date)


if __name__ == '__main__':
    reminders = []
    with open('Storage\\reminders.csv', 'r') as f:
        for line in f.readlines():
            reminders.append(FileManager(line, False))
    time_thread = th.Thread(target=time_manager, args=[reminders])
    time_thread.start()
    while True:
        user_input = input('Options:\n-add\n-remove\n-edit\n-view\n: ')
        if user_input.lower() == 'add' or user_input == '1':
            reminders.append(FileManager(None, True))
