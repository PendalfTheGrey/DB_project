import time
class DataBase:
    def __init__(self):
        self.DB = {"Names": [],
              "SNames": [],
              "FNames": [],
              "Dates": [],
              "Phones": []}

    def PushAtTheEnd(self, string):
        '''эта функция добавляет человека в конец списка'''
        if string == "wrongvalue":
            return 0
        self.DB["Names"].append(string[0])
        self.DB["SNames"].append(string[1])
        self.DB["FNames"].append(string[2])
        self.DB["Dates"].append(string[3])
        self.DB["Phones"].append(string[4])
    def ReadInput(self):
        userInput = input().split()
        if len(userInput[4]) != 10:
            return "wrongvalue"
        try:
            phone = int(userInput[4])
        except ValueError:
            print("incorrect number")
            return "wrongvalue"
        userInput[3] = self.ConvertDate(userInput[3])
        return userInput
    def ShowPerson(self, n):
        print(self.DB["Names"][n], self.DB["SNames"][n], self.DB["FNames"][n], self.DB["Dates"][n], self.DB["Phones"][n])
    def ReadDB(self, path):
        file = open(path, "r")
        DBlist = file.readlines()
        DBlist = list(map(str.split, DBlist))[1:]
        for person in DBlist:
            self.PushAtTheEnd(person)

    def PrettyTime(self, tm):
        return time.strftime("%d.%m.%Y", time.gmtime(tm))

    def ConvertDate(self, dt):
        # dt = dt.replace(".", " ")
        dt = time.strptime(dt, "%d.%m.%Y")
        return time.mktime(dt)

    def ShowTable(self):
        n = len(self.DB["Names"])
        output = []
        output.append("{:12s} {:12s} {:12s} {:12s} {:12s}".format("Names", "SNames", "FNames", "Dates", "Phones"))
        for i in range(0, n):
            output.append("{:12s} {:12s} {:12s} {:12s} {:12s}".format(self.DB["Names"][i], self.DB["SNames"][i], self.DB["FNames"][i],
                                                                      self.PrettyTime(self.DB["Dates"][i]), self.DB["Phones"][i]))
        for string in output:
            print(string)
        return output

    def SaveToFile(self):
        File = open("database.txt", "a")
        for string in self.ShowTable():
            File.write(string + "\n")
        File.close()