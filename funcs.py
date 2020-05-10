import datetime


def uptime_com(start_time): # get bot's uptime
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time # get delta time
    hours, remainder = divmod(int(delta.total_seconds()), 3600) # get hours and remainder (mins and secs)
    minutes, seconds = divmod(remainder, 60) # get mins and secd from remainder
    days, hours = divmod(hours, 24) # get days and hours
    if days: # if days > 0
        time_format = "{d} дней, {h} часов, {m} минут, {s} секунд." # set time format with days
    else:
        time_format = "{h} часов, {m} минут, {s} секунд." # set time format without days
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds) # set uptime stamp
    uptime = ("{} активен уже {}".format("Бот", uptime_stamp)) # finally uptime message
    return uptime # return finally message