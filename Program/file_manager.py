class RemindersClass:
    def __init__(self, f_line=None):
        f_line = f_line.strip('\n').split(',')
        self.name = f_line[0]
        self.datetime = f_line[1]
        self.repeat = f_line[2]

    def update(self, new_datetime):
        self. datetime = new_datetime


def create_reminders():
    reminders = []
    with open('Data\\reminders.csv', 'r') as f:
        for line in f.readlines():
            reminders.append(RemindersClass(line))
    return reminders


def create_new():
    from time_manager import get_datetime
    print('Create a new Reminder:')  # need to convert date and time into datetime object
    name = input('Reminder Name: ')
    datetime = get_datetime()
    print('Reminder Repeat Options:\n-hourly\n-daily\n-weekly\n-monthly\n-yearly,')
    repeat = input('Reminder Repeat: ')
    with open('Data\\reminders.csv', 'a') as f:
        f.write(f'{name},{datetime},{repeat}\n')


def update_reminders(reminders, new_dts):
    val = 0
    with open('Data\\reminders.csv', 'w') as f:
        f.truncate()  # clears the file
    for each in reminders:
        each.update(new_dts[val])
        val += 1
        with open('Data\\reminders.csv', 'a') as f:
            f.write(f'{each.name},{new_dts[val]},{each.repeat}\n')

