dict= {'first_name':'John','last_name':'Doe',

        'x':'Samarth','d':'Gowda',
       'y':'Saketh','e':'Maddula',
       'z':'Deepansh','f':'Parab',
        'a':'prathik','g':'Gaikwad',
        'b':'Sunil','h':'ramaiah',
        'c':'Sujay','i':'Ramaiah'}



def printDict(**dict):
    for k,v in dict.items():
        print("{}={}".format(k,v))




printDict(**dict)



