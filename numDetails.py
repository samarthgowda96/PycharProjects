import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate





def findDetails(num):
    number = phonenumbers.parse(num)
    details = geocoder.description_for_number(number,'en')
    network =  carrier.name_for_number(number,'en')
    information = [["Country", "Supplier"],
                   [details, network]]
    return tabulate(information, headers='firstrow', tablefmt='github')



num= input("Enter the Number : ")
print(findDetails(num))
