class Ticket:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Ticket(number={self.number})"


# TODO: create a Ticket and print() it -- observe it uses __repr__ since
# there's no __str__ defined
