#Your task in order to complete this Kata is to write a 
#function which formats a duration, given as a number 
#of seconds, in a human-friendly way.

#The function must accept a non-negative integer. 
#If it is zero, it just returns "now". 
#Otherwise, the duration is expressed as a combination 
#of years, days, hours, minutes and seconds.

#It is much easier to understand with an example:

#  format_duration(62)    # returns "1 minute and 2 seconds"
#  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
#Note that spaces are important.


def pluralize(n, word):
    if n == 1:
        return '%d %s' % (n, word)
    return '%d %ss' % (n, word)
         
def format_duration(seconds):
    if seconds == 0:
        return "now"
     
    min = 60
    hr = 60 * min
    day = 24 * hr
    yr = 365 * day
     
    units = (
        (yr, 'year'),
        (day, 'day'),
        (hr, 'hour'),
        (min, 'minute'),
        (1, 'second'),
    )
         
    r = []
    for unit in units:
        time_period, word = unit
        if seconds >= time_period:
            n = int(seconds / time_period)
            r.append(pluralize(n, word))
            seconds -= n * time_period
     
    return ' and'.join(', '.join(r).rsplit(',', 1))
