from persiantools.jdatetime import JalaliDate

def Milady_To_Shamsy(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    
    Jalali_date = JalaliDate.to_jalali(year, month, day)
    return Jalali_date

def Shamsy_To_Milady(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    
    Gregorian_date = JalaliDate(year, month, day).to_gregorian()
    return Gregorian_date

choise = int(input("Enter your chose: \n1.Milady to shamsy \n2.Shansy to Milady\n"))
if choise == 1 :
    Year = input("Enter the Gregorian year: ")
    Month = input("Enter the Gregorian month: ")
    Day = input("Enter the Gregorian day: ")

    result_jalali = Milady_To_Shamsy(Year, Month, Day)

    print(f"Shamsi Date: {result_jalali}")

elif choise == 2:
    
    JYear = input("Enter the Jalali year: ")
    JMonth = input("Enter the Jalali month: ")
    JDay = input("Enter the Jalali day: ")

    result_gregorian = Shamsy_To_Milady(JYear, JMonth, JDay)

    print(f"Gregorian Date: {result_gregorian}")

