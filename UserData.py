'''
Created on 03-Jan-2017

@author: ChandraDutt
'''
import Data;
import myLib;
class User:
    userId = 1;
    def __init__(self,UserId,FirstName,LastName,Sex,ContactNumber,CityName,EmailId,DOB,DateOfCreation):
        self.UserId = User.userId;
        self.FirstName = FirstName;
        self.LastName = LastName;
        self.Sex = Sex;
        self.ContactNumber = ContactNumber;
        self.CityName = CityName;
        self.EmailId = EmailId;
        self.DOB = DOB;
        self.DateOfCreation = DateOfCreation;
        User.userId += 1;
    def get_user_id(self):
        return self.__UserId


    def get_first_name(self):
        return self.__FirstName


    def get_last_name(self):
        return self.__LastName


    def get_sex(self):
        return self.__Sex


    def get_contact_number(self):
        return self.__ContactNumber


    def get_city_name(self):
        return self.__CityName


    def get_email_id(self):
        return self.__EmailId


    def get_dob(self):
        return self.__DOB


    def get_date_of_creation(self):
        return self.__DateOfCreation


    def set_user_id(self, value):
        self.__UserId = value


    def set_first_name(self, value):
        self.__FirstName = value


    def set_last_name(self, value):
        self.__LastName = value


    def set_sex(self, value):
        self.__Sex = value


    def set_contact_number(self, value):
        self.__ContactNumber = value


    def set_city_name(self, value):
        self.__CityName = value


    def set_email_id(self, value):
        self.__EmailId = value


    def set_dob(self, value):
        self.__DOB = value


    def set_date_of_creation(self, value):
        self.__DateOfCreation = value


    def del_user_id(self):
        del self.__UserId


    def del_first_name(self):
        del self.__FirstName


    def del_last_name(self):
        del self.__LastName


    def del_sex(self):
        del self.__Sex


    def del_contact_number(self):
        del self.__ContactNumber


    def del_city_name(self):
        del self.__CityName


    def del_email_id(self):
        del self.__EmailId


    def del_dob(self):
        del self.__DOB


    def del_date_of_creation(self):
        del self.__DateOfCreation

    UserId = property(get_user_id, set_user_id, del_user_id, "UserId's docstring")
    FirstName = property(get_first_name, set_first_name, del_first_name, "FirstName's docstring")
    LastName = property(get_last_name, set_last_name, del_last_name, "LastName's docstring")
    Sex = property(get_sex, set_sex, del_sex, "Sex's docstring")
    ContactNumber = property(get_contact_number, set_contact_number, del_contact_number, "ContactNumber's docstring")
    CityName = property(get_city_name, set_city_name, del_city_name, "CityName's docstring")
    EmailId = property(get_email_id, set_email_id, del_email_id, "EmailId's docstring")
    DOB = property(get_dob, set_dob, del_dob, "DOB's docstring")
    DateOfCreation = property(get_date_of_creation, set_date_of_creation, del_date_of_creation, "DateOfCreation's docstring")

usersToCreate = int(input('Enter number of users you want me to create'));
j=0;
for i in range(1,usersToCreate+1):
    fName=myLib.generateRandomFromList(Data.UsersFirstName);
    lName=myLib.generateRandomFromList(Data.UsersLastName);
    dates = myLib.generateTwoDates();
    userObj = User('',
                   fName,
                   lName,
                   myLib.generateSex(),
                   myLib.generatePhoneNo(),
                   myLib.generateRandomFromList(Data.Cities),
                   fName + lName+'@gmail.com',
                   dates[0],
                   dates[1],
                   );
    print(userObj.UserId,userObj.FirstName,userObj.LastName,userObj.Sex,userObj.ContactNumber,userObj.EmailId,userObj.DOB,userObj.DateOfCreation)