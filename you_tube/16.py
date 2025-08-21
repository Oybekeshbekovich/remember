ticket=input()
if len(ticket)==6 and ticket.isdigit():
    first_num=int(ticket[0])+int(ticket[1])+int(ticket[2])
    second_num=int(ticket[3])+int(ticket[4])+int(ticket[5])
    if first_num==second_num:
        print("YES")
    else:
        print("NO")
else:
    print("NO")