import datetime
import xlwings as xw
import os

class My_Excel:
    def __init__(self, file1):
        self.OpenExcelFile(file1)

    def OpenExcelFile(self, file):
        self.app = xw.App(visible=True, add_book=False)
        self.app.display_alerts = True
        self.app.screen_updating = True
        self.wb = self.app.books.open(file)
        self.st = self.wb.sheets

    def __del__(self):
        self.wb.save()
        self.wb.close()
        self.app.quit()

    def getTime(self, a):
        na = str(a)
        begain_time = datetime.datetime.strptime(na.split(",")[0], "%H:%M:%S")
        end_time = datetime.datetime.strptime(na.split(",")[-1], "%H:%M:%S")
        return (end_time - begain_time).seconds / 3600


    def write_to_excel(self, sheet_name):
        newrow = self.st[sheet_name].range("H65535").end("up").row
        for i in range(a):
            try:
                rng_value = self.st[sheet_name]["H" + str(newrow - i)].value
                self.st[sheet_name]["K" + str(newrow - i)].value = str(self.getTime(rng_value))
            except: 
                continue

def getDays():
    a = input("您想要计算最近几天的工作时间？请填相应的数字后回车:\n")
    return a 


def main():
    exfile = My_Excel("1907财务部考勤.xlsm")
    exfile.write_to_excel("打卡明细")

if __name__ == "__main__":
        main()