def time_converter(time_entered):
   
    time_in_hours = time_entered / 60
    time_in_hours = int(time_in_hours)

    time_in_minutes = time_entered % 60
    time_in_minutes = int(time_in_minutes)

    if time_in_hours == 1 and time_in_minutes == 1:
        return (str(time_in_hours) + " hour, " + str(time_in_minutes) + " minute")
    elif time_in_hours == 1 and time_in_minutes > 1:
        return (str(time_in_hours) + " hour, " + str(time_in_minutes) + " minutes")
    elif time_in_hours > 1 and time_in_minutes == 1:
        return (str(time_in_hours) + " hours, " + str(time_in_minutes) + " minute")
    else :
        return (str(time_in_hours) + " hours, " + str(time_in_minutes) + " minutes")  

returned_time = time_converter(71)
print(returned_time)