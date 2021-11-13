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

    if free.token < 0 or free.token > 10 or busy.token < 0 or busy.token > 10 or docu.token < 0 or docu.token > 10:
        print("Exception: The number of specialists must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change" and cmd != "end":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start": print("\"No specialists are free\"")
                elif cmd == "change": print("\"No specialists are treating\"")
                else: print("\"No specialists are documenting\"") 
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_2():
    wait = Place("Wait", 0)
    inside = Place("Inside", 0)
    done = Place("Done", 0)

    start = Transition([wait], [inside])
    change = Transition([inside], [done])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.placeSet = [wait, inside, done]

    print("Format: {x.wait, y.inside, z.done}\n")
    wait.token = int(input("Enter x: "))
    inside.token = int(input("Enter y: "))
    done.token = int(input("Enter z: "))

    if wait.token < 0 or wait.token > 10 or inside.token < 0 or inside.token > 10 or done.token < 0 or done.token > 10:
        print("Exception: The number of patients must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start": print("\"No patients are waiting\"")
                else: print("\"No patients are being treated\"")
            if wait.token == 0 and inside.token == 0:
                print("\nNOTE: All of patients have been done treatment!!!")
                return
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_3():
    wait = Place("Wait", 0)
    inside = Place("Inside", 0)
    done = Place("Done", 0)
    free = Place("Free", 0)
    busy = Place("Busy", 0)
    docu = Place("Docu", 0)

    start = Transition([free, wait], [busy, inside])
    change = Transition([busy, inside], [docu, done])
    end = Transition([docu], [free])

    SpecialistNet = PetriNet()
    SpecialistNet.transMap["start"] = start
    SpecialistNet.transMap["change"] = change
    SpecialistNet.transMap["end"] = end
    SpecialistNet.placeSet = [wait, inside, done, free, busy, docu]

    print("Format: {x.wait, y.inside, z.done, a.free, b.busy, c.docu}\n")
    wait.token = int(input("Enter x: "))
    inside.token = int(input("Enter y: "))
    done.token = int(input("Enter z: "))
    free.token = int(input("Enter a: "))
    busy.token = int(input("Enter b: "))
    done.token = int(input("Enter c: "))

    if wait.token < 0 or wait.token > 10 or inside.token < 0 or inside.token > 10 or done.token < 0 or done.token > 10 or free.token < 0 or free.token > 10 or busy.token < 0 or busy.token > 10 or docu.token < 0 or docu.token > 10:
        print("Exception: The number of tokens must be from 0 to 10!!!")
        return

    cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

    while cmd != "END":
        if cmd != "start" and cmd != "change" and cmd != "end":
            print(cmd, "is not a transition")
        else:
            if SpecialistNet.transMap[cmd].fire() == True:
                print("Marking obtained after firing:")
                SpecialistNet.printNet()
            else: 
                print(cmd, "is not currently enabled")
                if cmd == "start":
                    if wait.token == 0: print("\"No patients are waiting\"")
                    else: print("No specialists are free")
                elif cmd == "change":
                    print("\"No treatments are occurring\"")
                else: print("\"The specialist isn't documenting\"")
            if wait.token == 0 and inside.token == 0 and busy.token == 0 and docu.token == 0:
                print("\nNOTE: All of patients have been done treatment and specialists are free!!!")
                return
        cmd = input("\nEnter transition that you want to fire OR enter \"END\" to exit:\n")

def problem_4():
    x = int(input("Format: {x.wait, 0.inside, 1.done, 1.free, 0.busy, 0.docu}\nEnter the number of patients x: "))
    
    if x < 0 or x > 10:
        print("Exception: The number of patients must be from 0 to 10!!!")
        return

    marking_key = ["wait", "inside", "done", "free", "busy", "docu"]
    marking_value = [x, 0, 1, 1, 0, 0]

    str = ""
    for i in range(x * 3 + 1):
        print("Firing sequence: [", str, "]\nMarking: [", sep = '', end = '')
        for k in range(6):
            if k != 5: print(marking_key[k], ".", marking_value[k], ", ", sep = '', end = '')
            else: print(marking_key[k], ".", marking_value[k], "]\n", sep = '')
        
        if i % 3 == 0:
            marking_value[0] = marking_value[0] - 1
            marking_value[3] = marking_value[3] - 1
            marking_value[1] = marking_value[1] + 1
            marking_value[4] = marking_value[4] + 1
        
        elif i % 3 == 1:
            marking_value[1] = marking_value[1] - 1
            marking_value[4] = marking_value[4] - 1
            marking_value[2] = marking_value[2] + 1
            marking_value[5] = marking_value[5] + 1

        else:
            marking_value[5] = marking_value[5] - 1
            marking_value[3] = marking_value[3] + 1
        
        str = str + ("start" if str == "" else ",start" if i % 3 == 0 else ",change" if i % 3 == 1 else ",end")

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
    else: print("Exception: Your input must be from 1 to 4!!!")

if __name__ == "__main__":
    main()