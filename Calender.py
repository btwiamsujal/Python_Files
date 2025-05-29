# write a code to find day if date is given
date = int(input("in %dd format: "))
month = int(input("in %mmformat: "))
year = int(input("in %yyyy format: "))

century = year % 100
cent = year // 100
rem = cent % 4
x = 0
if rem == 0:
    x = 6
elif rem == 1:
    x = 4
elif rem == 2:
    x = 2
elif rem == 3:
    x = 0

general_year = "033614625035"
lear_year = "623614625035"

if (year % 4 == 0 & year % 400 == 0 | year % 100 != 0):
    answer = (date + int(lear_year[month - 1]) + century + century // 4 + x) % 7
else:
    answer = (date + int(general_year[month - 1]) + century + century // 4 + x) % 7
 
match answer:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Invalid date")
   

