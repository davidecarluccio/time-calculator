def add_time(start, duration, starting_day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM':
        start_hour += 12 if start_hour < 12 else 0
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate new time
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)
    
    # Determine new period and hour
    period = 'AM' if new_hour < 12 else 'PM'
    new_hour = new_hour if new_hour != 0 else 12
    if new_hour > 12:
        new_hour -= 12
    
    # Handle day of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if starting_day:
        starting_day = starting_day.capitalize()
        day_index = days_of_week.index(starting_day)
        new_day = days_of_week[(day_index + days_later) % 7]
    else:
        new_day = None
    
    # Format result
    time_string = f"{new_hour}:{new_minute:02d} {period}"
    if new_day:
        time_string += f", {new_day}"
    if days_later == 1:
        time_string += " (next day)"
    elif days_later > 1:
        time_string += f" ({days_later} days later)"
    
    return time_string
