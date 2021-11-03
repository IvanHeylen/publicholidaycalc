import datetime

#IF NEW YEAR'S DAY FALLS ON A WEEKEND IT WILL BE OBSERVED ON THE NEXT MONDAY.
#RETURNS NEW YEAR'S DAY AS WELL AS THE NEXT MONDAY SHOULD NYD FALL ON A WEEKEND.
#THE RETURN WILL BE IN DATE FORMAT (YYYY, MM, DD)
def newYearsDayCalc(year): 
    newYearsDay = datetime.date(year, 1, 1)
    if newYearsDay.weekday() == 5:
        newYearsDayExtension = newYearsDay + datetime.timedelta(days = 2)
        return str(newYearsDay) + " , " + str(newYearsDayExtension) + " OBSERVED"
    elif newYearsDay.weekday() == 6:
        newYearsDayExtension = newYearsDay + datetime.timedelta(days = 1)
        return str(newYearsDay) + " , " + str(newYearsDayExtension) + " OBSERVED"
    else:
        return newYearsDay

#AUSTRALIA DAY ALWAYS FALLS ON THE 26th OF JANUARY. HOWEVER, IF IT FALLS ON A WEEKEND, IT WILL BE CELEBRATED
#FOLLOWING MONDAY.
#RETURNS AUSTRALIA DAY AND THE FOLLOWING MONDAY IF APPLICABLE IN DATE FORMAT (YYYY, MM, DD)
def australiaDayCalc(year): 
    australiaDay = datetime.date(year, 1, 26)
    if australiaDay.weekday() == 5:
        australiaDayExtension = australiaDay + datetime.timedelta(days = 2)
        return str(australiaDay) + " , " + str(australiaDayExtension) + " OBSERVED"
    elif australiaDay.weekday() == 6:
        australiaDayExtension = australiaDay + datetime.timedelta(days = 1)
        return str(australiaDay) + " , " + str(australiaDayExtension) + " OBSERVED"
    else:
        return australiaDay

#LABOUR DAY IS CELEBRATED ON THE SECOND MONDAY OF MARCH.
#RETURNS THE SECOND MONDAY OF MARCH IN DATE FORMAT (YYYY, MM, DD)
def labourDayCalc(year):
    if datetime.date(year, 3, 1).weekday() == 0:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=7)
    elif datetime.date(year, 3, 1).weekday() == 1:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=13)
    elif datetime.date(year, 3, 1).weekday() == 2:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=12)
    elif datetime.date(year, 3, 1).weekday() == 3:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=11)
    elif datetime.date(year, 3, 1).weekday() == 4:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=10)
    elif datetime.date(year, 3, 1).weekday() == 5:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=9)
    elif datetime.date(year, 3, 1).weekday() == 6:
        labourDay = datetime.date(year, 3, 1) + datetime.timedelta(days=8)
    else:
        print("labourDayCalc failed to run properly.")
    return labourDay

#BUTCHER'S ALGORITHM FOR CALCULATING THE EXACT DATE OF EASTER FOR THE WESTERN CHURCH
#RETURNS THE EXACT DATE OF EASTER IN (YYYY, MM, DD) FORMAT.
def easterCalc(year):
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return datetime.date(year, month, day)

#RETURNS EASTER DAY MINUS 1
def satEasterCalc(year): 
    satEaster = easterCalc(year) + datetime.timedelta(days= -1)
    return satEaster

#RETURNS EASTER DAY MINUS 2
def friEasterCalc(year):
    friEaster = easterCalc(year) + datetime.timedelta(days= -2)
    return friEaster

#RETURNS EASTER DAY PLUS 1
def monEasterCalc(year):
    monEaster = easterCalc(year) + datetime.timedelta(days= 1)
    return monEaster

#MELBOURNE CUP IS CELEBRATED ON THE FIRST TUESDAY OF NOVEMBER.
#RETURN THE FIRST TUESDAY OF NOVEMBER IN DATE FORMAT (YYYY, MM, DD)
def melbourneCupCalc(year):
    if datetime.date(year, 11, 1).weekday() == 0:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=1)
    elif datetime.date(year, 11, 1).weekday() == 1:
        melbourneCup = datetime.date(year, 11, 1)
    elif datetime.date(year, 11, 1).weekday() == 2:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=6)
    elif datetime.date(year, 11, 1).weekday() == 3:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=5)
    elif datetime.date(year, 11, 1).weekday() == 4:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=4)
    elif datetime.date(year, 11, 1).weekday() == 5:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=3)
    elif datetime.date(year, 11, 1).weekday() == 6:
        melbourneCup = datetime.date(year, 11, 1) + datetime.timedelta(days=2)
    else:
        print("melbourneCupCalc failed")
    return melbourneCup

#THE QUEEN'S BIRTHDAY IS CELEBRATED ON THE SECOND MONDAY OF JUNE.
#RETURNS THE SECOND MONDAY OF JUNE IN DATE FORMAT (YYYY, MM, DD)
def queensBirthdayCalc(year):
    firstOfJune = datetime.date(year, 6, 1)
    if firstOfJune.weekday() == 0:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 7)
    elif firstOfJune.weekday() == 1:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 13)
    elif firstOfJune.weekday() == 2:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 12)
    elif firstOfJune.weekday() == 3:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 11)
    elif firstOfJune.weekday() == 4:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 10)
    elif firstOfJune.weekday() == 5:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 9)
    elif firstOfJune.weekday() == 6:
        queensBirthDay = firstOfJune + datetime.timedelta(days = 8)
    else:
        print("queensBirthDayCalc Failed")
    return queensBirthDay

#THE FRIDAY BEFORE AFL GRAND FINAL IS CELEBRATED ON THE LAST FRIDAY OF SEPTEMBER
#UNLESS THE GRAND FINAL IS AFTER THE 1st of OCTOBER. IN THAT CASE IT WILL BE THE FIRST
#FRIDAY OF OCTOBER.
#RETURNS THE FRIDAY BEFORE THE AFL GRAND FINAL IN DATE FORMAT (YYYY, MM, DD)
def aflGrandFinalCalc(year):
    if datetime.date(year, 9, 30).weekday() == 4:
        aflGrandFinal = datetime.date(year, 9, 30)
    elif datetime.date(year, 9, 30).weekday() == 5:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= -1)
    elif datetime.date(year, 9, 30).weekday() == 6:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= -2)
    elif datetime.date(year, 9, 30).weekday() == 0:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= -3)
    elif datetime.date(year, 9, 30).weekday() == 1:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= 3)
    elif datetime.date(year, 9, 30).weekday() == 2:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= 2)
    elif datetime.date(year, 9, 30).weekday() == 3:
        aflGrandFinal = datetime.date(year, 9, 30) + datetime.timedelta(days= 1)
    else:
        print("aflGrandFinalCalc failed") 
    return aflGrandFinal

#CHRISTMAS DAY WILL BE CELEBRATED ON THE 25th OF DECEMBER AND 
#ON THE FOLLOWING MONDAY IF IT FALLS ON A SATURDAY. IF IT FALLS ON A SUNDAY
#THEN IT WILL BE CELEBRATED ON THE FOLLOWING TEUSDAY INSTEAD OF MONDAY.
#RETURN CHRISTMAS DAY AND THE FOLLOWING MONDAY IF APPLICABLE.
def christmasDayCalc(year):
    christmasDay = datetime.date(year, 12, 25)
    if christmasDay.weekday() == 5:
        christmasExtension = christmasDay + datetime.timedelta(days = 2)
        return str(christmasDay) + " , " + str(christmasExtension)
    elif christmasDay.weekday() == 6:
        christmasExtension = christmasDay + datetime.timedelta(days = 2)
        return str(christmasDay) + " , " + str(christmasExtension)
    else:
        return christmasDay

#BOXING DAY WILL BE CELEBRATED ON THE 26th OF DECEMBER AND THE FOLLOWING MONDAY IF IT FALLS ON 
#SATURDAY. IF IT FALLS ON A SUNDAY THEN THE FOLLOWING TUESDAY WILL BE A PUBLIC HOLIDAY AS WELL.
#RETURNS BOXING DAY AND THE MONDAY OR TUESDAY IF THE ABOVE CONDITIONS ARE MET.
def boxingDayCalc(year):
    boxingDay = datetime.date(year, 12, 26)
    christmasDay = datetime.date(year, 12, 25)
    if boxingDay.weekday() == 5:
        boxingDayExtension = boxingDay + datetime.timedelta(days = 2)
        return str(boxingDay) + " , " + str(boxingDayExtension)
    elif boxingDay.weekday() == 6:
        boxingDayExtension = boxingDay + datetime.timedelta(days = 2)
        return str(boxingDay) + " , " + str(boxingDayExtension)
    else:
        return boxingDay
    
#MAIN FUNCTION
#RUNS A WHILE LOOP USING A START YEAR AND END YEAR.
#IT WILL ITERATE THROUGH EACH YEAR UNTIL IT REACHES THE END YEAR.
def main():
    
    print(
    '''
PUBLIC HOLIDAY CALCULATOR
Enter a year range to calculate
    '''
    )
    #USER INPUT FOR THE YEAR THEY SELECT
    try: 
        year = int(input("From: "))
    except:
        print("You must enter a number!")
    try:
        endyear = int(input("To: "))
    except:
        print("You must enter a number!")

    while year < endyear + 1:
        print("\n" + str(year) + "\n----")
        print("New Year's Day: " + " "*25 + str(newYearsDayCalc(year)))
        print("Australia Day: " + " "*26 + str(australiaDayCalc(year)))
        print("Labour Day: " + " "*29 + str(labourDayCalc(year)))
        print("Easter Friday: " + " "*26 + str(friEasterCalc(year)))
        print("Easter Saturday: " + " "*24 + str(satEasterCalc(year)))
        print("Easter: " + " "*33 + str(easterCalc(year)))
        print("Easter Monday: " + " "*26 + str(monEasterCalc(year)))
        print("Anzac Day: " + " "*30 + str(datetime.date(year, 4, 25)))
        print("Queen's Birthday: " + " "*23 + str(queensBirthdayCalc(year)))
        print("Friday before AFL Grand Final: " + " "*10 + str(aflGrandFinalCalc(year)))
        print("Melbourne Cup Day: " + " "*22 + str(melbourneCupCalc(year)))
        print("Christmas Day: " + " "*26 + str(christmasDayCalc(year)))
        print("Boxing Day: " + " "*29 + str(boxingDayCalc(year)) + "\n")
        year = year + 1

#RUNNING THE MAIN FUNCTION
if __name__ == '__main__':
    main()