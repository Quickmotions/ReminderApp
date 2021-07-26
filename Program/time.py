from datetime import datetime

def update_reminder_times(initial_time ,initial_date ,repeats):
    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    current_date = str(now.date())
    while int(initial_time[:1]) <= int(current_time[:1]) and int(initial_time[3:]) <= int(current_time[3:]):
        if repeats == 'hourly':
            if int(initial_time[:2]) < 23:
                initial_time = str(int(initial_time[:2]) + 1) + initial_time[2:]
            else:
                initial_time = '00' + initial_time[2:]
    while int(initial_time[:1]) <= int(current_time[:1]) and int(initial_time[3:]) <= int(current_time[3:]): # do for dates
    if repeats == 'daily':
        if int(initial_date[8:]) in [] # months with 30
            if int(initial_date[8:]) < 30:  # have to add diffrence depending on months maybe mo0ve to new file
                initial_date = initial_date[:8] + str(int(initial_date[8:]) + 1)
        if int(initial_date[8:]) in []  # months with 31

        if int(initial_date[8:]) in []  # February with 28

# 2021-07-25
# 22:12