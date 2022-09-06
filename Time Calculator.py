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


if __name__ == "__main__":
    add_time("11:55 AM", "3:12")
    add_time("11:30 AM", "2:32", "Monday")
    add_time("11:43 PM", "24:20", "tueSday")
    add_time("3:30 PM", "3:45")
    add_time("2:59 AM", "24:00")
    add_time("11:59 PM", "24:05")