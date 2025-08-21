#MATCH-case statement(switch)-> ko'p eliflar ishlatishni oldini oladi ("|"=="or")
def is_weekend(date):
    match date:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Thursday" | "Friday" | "Wednesday" | "Tuesday":
            return False
        case _:
            return False
print(is_weekend('Saturday'))
print(is_weekend('Monday'))