class Guitar:
    def play(self):
        return "Strumming the guitar"


class Piano:
    def play(self):
        return "Playing the piano"


class Drum:
    def play(self):
        return "Hitting the drum"


instruments = [Guitar(), Piano(), Drum()]
for instrument in instruments:
    print(instrument.play())
