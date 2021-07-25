
from time import sleep
import threading as th
from datetime import datetime
# dependencies
import notify

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

    def create_new(self):
        print('Create a new Reminder:')
        self.reminder = input('Reminder Name: ')
        self.time = input('Reminder Time (HH:MM): ')
        self.date = input('Reminder Date (YY-MM-DD): ')
        print('Reminder Repeat Options:\n-hourly\n-daily\n-weekly\n-monthly\n-yearly,')
        self.repeat = input('Reminder Repeat: ')
        with open('Storage\\reminders.csv', 'a') as f:
            f.write(f'{self.reminder},{self.time},{self.date},{self.repeat}\n')

    def update_reminder_times(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.date()
        # if self.time < current_time and self.date < current_date:



def time_manager(r_list):
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.date()
        print(f'{current_time}{current_date}')
        check_reminders(r_list, current_time, current_date)
        sleep(60)


def check_reminders(r_list, current_time, current_date):
    for r in r_list:
        sleep(0.5)
        if r.time == str(current_time) and r.date == str(current_date):
            print('true')
            notify.notification(f'Reminder: for {r.reminder} at {r.time}', title=f'{r.reminder} at {r.time}')
            print(r.reminder)


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
