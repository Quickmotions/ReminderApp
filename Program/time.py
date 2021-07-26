from datetime import datetime

def update_reminder_times(initial_time ,initial_date ,repeats):
    now = datetime.now()
    current_time = str(now.strftime("%H:%M"))
    current_date = str(now.date())
    while initial_time <= current_time and initial_date <= current_date:
        if repeats == 'hourly':
            if int(initial_time[:2]) < 23:
                initial_time = str(int(initial_time[:2]) + 1) + initial_time[2:]
            else:
                initial_time = '00' + initial_time[2:]
        if repeats == 'daily':
            if int(initial_date[8:]) < 30:  # have to add diffrence depending on months maybe mo0ve to new file
                initial_date = initial_date[:8] + str(int(initial_date[8:]) + 1)


