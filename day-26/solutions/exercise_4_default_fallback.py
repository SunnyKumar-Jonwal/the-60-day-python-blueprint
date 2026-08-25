class Ticket:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Ticket(number={self.number})"


ticket = Ticket(42)
print(ticket)
