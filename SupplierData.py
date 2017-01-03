import myLib
import Data
# SuppReq = int(input('Enter required number of suppliers'));
# print("Required number of suppliers are",SuppReq);

class Supplier:
    supplierId = 1
    def __init__(self,SupplierId,SupplierName,EmailId,StartDate,CityName):
        self.SupplierId = Supplier.supplierId
        self.SupplierName = SupplierName
        self.EmailId = EmailId
        self.StartDate = StartDate
        self.CityName = CityName
        Supplier.supplierId += 1

    def get_supplier_count(self):
        return self.__SupplierCount


    def get_supplier_id(self):
        return self.__SupplierId


    def get_supplier_name(self):
        return self.__SupplierName


    def get_email_id(self):
        return self.__EmailId


    def get_start_date(self):
        return self.__StartDate


    def get_city_name(self):
        return self.__CityName


    def set_supplier_count(self, value):
        self.__SupplierCount = value


    def set_supplier_id(self, value):
        self.__SupplierId = value


    def set_supplier_name(self, value):
        self.__SupplierName = value


    def set_email_id(self, value):
        self.__EmailId = value


    def set_start_date(self, value):
        self.__StartDate = value


    def set_city_name(self, value):
        self.__CityName = value


    def del_supplier_count(self):
        del self.__SupplierCount


    def del_supplier_id(self):
        del self.__SupplierId


    def del_supplier_name(self):
        del self.__SupplierName


    def del_email_id(self):
        del self.__EmailId


    def del_start_date(self):
        del self.__StartDate


    def del_city_name(self):
        del self.__CityName


    SupplierCount = property(get_supplier_count, set_supplier_count, del_supplier_count, "SupplierCount's docstring")
    SupplierId = property(get_supplier_id, set_supplier_id, del_supplier_id, "SupplierId's docstring")
    SupplierName = property(get_supplier_name, set_supplier_name, del_supplier_name, "SupplierName's docstring")
    EmailId = property(get_email_id, set_email_id, del_email_id, "EmailId's docstring")
    StartDate = property(get_start_date, set_start_date, del_start_date, "StartDate's docstring")
    CityName = property(get_city_name, set_city_name, del_city_name, "CityName's docstring")
    
    



for key,value in Data.Suppliers.items():
    supplierObj = Supplier('',
                           key,
                           value,
                           myLib.generateRandomDate(),
                           myLib.generateRandomFromList(Data.Cities));
    print(supplierObj.get_supplier_id(),supplierObj.get_supplier_name(),supplierObj.get_start_date(),supplierObj.get_city_name());