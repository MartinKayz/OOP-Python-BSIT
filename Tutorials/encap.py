class ServiceProvider:
    email = "fotogenix@gmail.com"
    discount = 0.02

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.name

    @classmethod
    def isuing_invoice(cls):
        return "Here is the invoice"

class JuniorServProvider(ServiceProvider):
    def __init__(self, name, phone, location):
        super().__init__(name, phone, location)
        self.location = location

serv_1 = ServiceProvider("Photogenix", 700232657)
serv_2 = ServiceProvider("FreshKid", 3000012)
serv_3 = JuniorServProvider("UNRA", 933953, "Kololo")

serv_1.discount = 0.30
print(serv_1.discount)
print(serv_2.discount)
print(serv_3.discount)

# print(ServiceProvider(serv_1))
ServiceProvider.email = "Jeny@gmail.com"

# print(serv_1.email)



