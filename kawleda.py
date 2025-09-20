import calendar as c

k = int(input("Kô: "))
t = int(input("Thla: "))

def a(t):
    match t:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
        case _:
            return "Invalid month"

thla_moh = a(t)
if thla_moh == "Invalid month":
    print("Invalid month entered.")
else:
    print(f"\nThe calendar of {thla_moh} {k} is:\n")
    print(c.month(k, t))