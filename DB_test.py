import Database
c = 0

DB = Database.DataBase()
DB.PushAtTheEnd(DB.ReadInput())
DB.ShowTable()
try:
    print(int(1/0))
except ValueError:
    print("000")
except ZeroDivisionError:
    print("0")


'''while c < 3:
    try:
        DB.PushAtTheEnd(DB.ReadInput())
        DB.ShowTable()
    except:
        print("try again")
    c += 1
DB.SaveToFile()'''
