days_of_week = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
def sum_time(h1: int, m1: int, h2: int, m2: int) -> dict:
    """
    Sum two times and return a dict with the result
    Args:
        h1 (int): hours of the first time
        m1 (int): minutes of the first time
        h2 (int): hours of the second time
        m2 (int): minutes of the second time
    """
    dic_time = {"h": 0, "m": 0, "days": 0}
    h_total = h1 + h2
    m_total = m1 + m2
    t_total = h_total * 60 + m_total
    h3 = t_total // 60
    m3 = t_total % 60
    dic_time["h"] = h3 % 24
    dic_time["m"] = m3
    dic_time["days"] = h3 // 24
    return dic_time

def add_time(t1: str, t2: str, initial_day=None) -> None:
    """ 
    add two times and print the result
    Args:
        t1 (str): initial time in format "hh:mm" or "hh:mm AM/PM"
        t2 (str): time interval in the format hh:mm
        initial_day (str, optional): string who represents the day of the week. Defaults to None.
    """
    t1 = t1.lower()
    t2 = t2.lower()
    t1_time, t1_ampm = t1.split(' ')
    h1, m1 = t1_time.split(':')
    h2, m2 = t2.split(':')
    if t1_ampm == 'pm':
        h1 = int(h1) + 12
    time = sum_time(int(h1), int(m1), int(h2), int(m2))
    ampm = 'AM' if time['h'] < 12 else 'PM'
    time['h'] = time['h'] % 12
    out = f"{time['h'] % 12}:{time['m']:02d} {ampm}"
    if initial_day is not None:
        initial_day = initial_day.capitalize()
        day = days_of_week[(list(days_of_week.keys())[list(days_of_week.values()).index(initial_day)] + time['days']) % 7]
        out += f', {day}'
    match int(time['days']):
        case 0: pass
        case 1: out += ' (next day)'
        case _: out += f' ({time["days"]} days later)'
    print(out)