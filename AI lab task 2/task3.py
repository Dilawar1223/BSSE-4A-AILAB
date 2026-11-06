class ACController:

    def __init__(self):
        self.old_mode = None

    def control(self, temp, occup):

        if not occup:
            target = "OFF"

        elif temp < 16:
            target = "HEAT"

        elif temp > 23:
            target = "COOL"

        else:
            target = "OF"

        if target == self.old_mode:
            command = "NO SEND"
        else:
            command = "SEND"

        previous = self.old_mode
        self.old_mode = target

        return previous, target, command


ac = ACController()

tests = [
    ("First reading", 20, True),
    ("Repeated reading", 20, True),
    ("Lower boundary", 18, True),
    ("Upper boundary", 24, True),
    ("Mode change to COOL", 26, True),
    ("Repeated COOL", 26, True),
    ("Empty room", 26, False)
]

print("Previous Mode | Percept | Target | Command")

for name, temp, person in tests:
    previous, target, command = ac.control(temp, person)

    percept = "Temp=" + str(temp) + ", Occup=" + str(person)

    print(previous, "|", percept, "|", target, "|", command)