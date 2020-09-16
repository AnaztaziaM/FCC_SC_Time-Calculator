def add_time(start, duration, day_of_the_week=False):

    #Convert to 24 h.
    width = len(start)
    if start[-2:] == "AM" and start[:2] == "12":
        start_24 = "00" + start[2:-2]
    elif start[-2:] == "AM":
        start_24= start[:-3]
    elif start[-2:] == "PM" and start[:2] == "12":
        start_24 = start[:-2]
    else:
        start_24 = str(int(start[:(width-6)]) + 12) + start[(width-6):(width-3)]

    #Setting the variables.
    hours_s = start_24[:-3]
    minutes_s = start_24[-2:]
    hours_d = duration[:-3]
    minutes_d = duration[-2:]


    # Finding the minutes.
    add_minutes = int(minutes_s) + int(minutes_d)

    if add_minutes > 59:
        remainder = add_minutes/60
        final_minutes = str(add_minutes % 60).zfill(2)
    else:
        remainder = 0
        final_minutes=str(add_minutes).zfill(2)

    #Calculating the hours.
    add_hours = int(hours_s) + int(hours_d) + int(remainder)

    if add_hours < 24:
        day = 0
        day_adding = ""
        time = int(add_hours)

    elif add_hours > 24 and add_hours < 48:
        day = 1
        day_adding = "(next day)"
        time = int(add_hours % 24)

    else:
        day = int(add_hours/24)
        day_adding ="(" + str(day) +" days later)"
        time = int(add_hours % 24)

    #Converting back to 12 h.
    if time == 0:
        final_time = 12
        am_pm = "AM"
    elif time < 12 and time !=0:
        final_time = time
        am_pm = "AM"
    elif time == 12:
        final_time = time
        am_pm = "PM"
    elif time > 12 and time % 12 ==0:
        final_time = 12
        am_pm = "AM"
    else:
        final_time = time % 12
        am_pm = "PM"

    # Calculating the week day.
    if day_of_the_week:
        days_dic = {"monday":1,"tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
        w_d = int(day % 7)
        todays_day = []
        for k,v in days_dic.items():
            if k == str(day_of_the_week.lower()):
                calculation_w_d = v + w_d
                if calculation_w_d > 7:
                    the_day = calculation_w_d - 7
                    for k,v in days_dic.items():
                        if v == the_day:
                            todays_day.append(k)
                else:
                    the_day = calculation_w_d
                    for k,v in days_dic.items():
                        if v == the_day:
                            todays_day.append(k)
            else:
                continue
        today = todays_day[0].capitalize()
        if day == 0:
            return (str(final_time) + ":" + str(final_minutes) + " " + str(am_pm) + ", " + str(today))
        else:
            return (str(final_time) + ":" + str(final_minutes)+ " "+ str(am_pm) + ", " + str(today) + " " + str(day_adding))

    else:
        if day == 0:
            return (str(final_time) + ":" + str(final_minutes) + " " + str(am_pm))
        else:
            return (str(final_time) + ":" + str(final_minutes)+ " "+ str(am_pm) + " " + str(day_adding))


