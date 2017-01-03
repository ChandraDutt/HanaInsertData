'''
Created on 03-Jan-2017

@author: ChandraDutt
'''
import random;
def generateRandomFromList(inputVar):
    return(random.choice(inputVar));


def generatePhoneNo():
    phoneNo = str(random.randint(7,9));
    return (int(phoneNo + str(random.randint(000000000,999999999))));


def generateSex():
    return(random.choice(['M','F']));

def generateRandomDate():
    year = random.randint(1990,2016);
    month = random.randint(1,12);
    if month == 2:
        l_year = isLeapYear(year);
        if l_year == True:
            date = random.randint(1,29);
        else:
            date = random.randint(1,28)
    elif month in (4,6,9,11) :
        date = random.randint(1,30);
    else:
        date = random.randint(1,31);
    return (str(year)+'-'+str(month)+'-'+str(date));


def isLeapYear(year):
    if ((year%4 == 0) & (year%100 != 0)) | (year%400 == 0):
        return True
    else:
        return False


def generateTwoDates():
    firstDate = generateRandomDate();
    secondDate = generateRandomDate();
    if int(secondDate[0:3])>int(firstDate[0:3]):
        return(firstDate,secondDate);
    else:
        return(generateTwoDates());
    
