def add_time(t1: str, t2: str, day_of_week=None) -> str:
    #Add two times together in the format HH:MM 
    #the first with AM or PM in the text
    #and return the result in the same format.
    #Split the times into hours, minutes and AM/PM
    # add_time("11:55 AM", "3:12") ➞ "3:07 PM"
    # add_time("11:30 AM", "2:32", "Monday") ➞ "2:02 PM, Monday"
    # add_time("11:43 PM", "24:20", "tueSday") -> "12:03 AM, Thursday (2 days later)"
    # add_time("3:30 PM", "3:45") ➞ "7:15 PM"
    # add_time("2:59 AM", "24:00") ➞ "2:59 AM (next day)"
    # add_time("11:59 PM", "24:05") ➞ "12:04 AM (2 days later)"
    t1 = t1.upper()
    t2 = t2.upper()


if __name__ == "__main__":
    print(add_time("3:30 PM", "3:45"))
    print(add_time("11:55 AM", "3:12"))