





if __name__ == '__main__':
    reminders = []
    with open('Data\\reminders.csv', 'r') as f:
        for line in f.readlines():
            reminders.append(FileManager(line, False))
    time_thread = th.Thread(target=time_manager, args=[reminders])
    time_thread.start()
    while True:
        user_input = input('Options:\n-add\n-remove\n-edit\n-view\n: ')
        if user_input.lower() == 'add' or user_input == '1':
            reminders.append(FileManager(None, True))