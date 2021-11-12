class Place:
    def __init__(self, name = "", token = 0):
        self.name = name
        self.token = token

class Transition:
    def __init__(self, inputplace = [], outputplace = []):
        self.inputplace = inputplace
        self.outputplace = outputplace

    def fire(t):
        for i in range(len(t.inputplace)):
            if t.inputplace[i].token < 1:
                return False
            else: t.inputplace[i].token = t.inputplace[i].token - 1
        for i in range(len(t.outputplace)):
            t.outputplace[i].token = t.outputplace[i].token + 1
        return True

class PetriNet:
    def __init__(self, transMap = {}, placeSet = []):
        self.transMap = transMap
        self.placeSet = placeSet
    
    def printNet(N):
        print("[", end = '')
        for i in range(len(N.placeSet)):
            if i != 0: print(", ", end = '')
            print(N.placeSet[i].name, ".", N.placeSet[i].token, sep = '', end = '')
        print("]")

def problem_1():
    free = Place("Free", 0)
    busy = Place("Busy", 0)
    docu = Place("Docu", 0)

    start = Transition([free], [busy])
    change = Transition([busy], [docu])
    end = Transition([docu], [free])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.transMap["end"] = end
    SpecialistNet.placeSet = [free, busy, docu]

    print("Format: {x.free, y.busy, z.docu}\n")
    free.token = int(input("Enter x: "))
    busy.token = int(input("Enter y: "))
    docu.token = int(input("Enter z: "))

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change" and cmd != "end":
            print(cmd, " is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: print(cmd, " is not currently enabled")
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_2():
    print("====problem 2====")

def problem_3():
    print("====problem 3====")

def problem_4():
    print("====problem 4====")


def main():
    a = input("Input the problem you want to solve: ")
    if a == '1':
        problem_1()
    elif a == '2':
        problem_2()
    elif a == '3':
        problem_3()
    elif a == '4':
        problem_4()
    else: print("Exception: Your input must be 1 from 4!!!")

if __name__ == "__main__":
    main()