def VotingCheck(age):
    if age >= 18:
        print('Congrats, you can vote.')
    else:
        print("Not old enough to vote.")


def movieTicket(age):
    if age <= 13:
        print("Ticket = 10.00")
    elif age >= 14:
        print("Ticket = 15.00")
    elif age >= 25:
        print("Ticket = 20.00 ")
    else:
        print('Ticket = 10.00')