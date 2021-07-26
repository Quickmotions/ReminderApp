# other files
from time import update_reminder_times, update_reminder_dates
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
            self.reminder = f_line[0]
            self.time = f_line[1]
            self.date = f_line[2]
            self.repeat = f_line[3]
            print(self.date)

            print(self.date)

    def create_new(self):
        print('Create a new Reminder:')
        self.reminder = input('Reminder Name: ')
        self.time = input('Reminder Time (HH:MM): ')
        self.date = input('Reminder Date (YY-MM-DD): ')
        print('Reminder Repeat Options:\n-hourly\n-daily\n-weekly\n-monthly\n-yearly,')
        self.repeat = input('Reminder Repeat: ')
        with open('Storage\\reminders.csv', 'a') as f:
            f.write(f'{self.reminder},{self.time},{self.date},{self.repeat}\n')



def time_manager(r_list):
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.date()
        check_reminders(r_list, current_time, current_date)
        # update reminders
        for reminder in reminders:
            reminder.time = update_reminder_times(reminder.time, reminder.date, reminder.repeat)
        # check each min
        sleep(60)


def check_reminders(r_list, current_time, current_date):
    for r in r_list:
        sleep(0.5)
        if r.time == str(current_time) and r.date == str(current_date):
            Notification(
                title=f'{r.reminder} at {r.time}',
                description=f'Reminder: {r.reminder} at {r.time}, notified on a {r.repeat} basis',
                duration=10,  # Duration in seconds
                urgency='normal'
            ).send()
            r.update_reminder_times()


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
