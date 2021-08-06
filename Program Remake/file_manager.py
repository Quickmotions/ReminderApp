class RemindersClass:
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


def create_reminders():
    reminders = []
    with open('Storage\\reminders.csv', 'r') as f:
        for line in f.readlines():
            reminders.append(RemindersClass(line, False))
    return reminders


def update_reminder_next(reminders, position):
    pass


def update_reminder_past(reminders, poistion):
    pass
