import pandas
import random
import uuid
import time
import datetime

groceries = {}
with open('groceries.csv') as csvfile:
    reader = pandas.read_csv(csvfile, delimiter=';')
    groceries = reader.to_dict('records')

names = {}
with open('name.csv') as csvfile:
    reader = pandas.read_csv(csvfile, delimiter=';')
    names = reader.to_dict('records')

while True:
    eol = '\n'
    idBasket = uuid.uuid4().hex
    idName = str(random.randint(3, 12)*'X')
    nbOrder = random.randint(0, 50)
    nameRand = random.randint(0, len(names)-1)
    firstName = names[nameRand]['firstname']
    now = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    groceriesBasket = []
    for i in range(nbOrder):
        itemRand = random.randint(0, len(groceries)-1)
        groceriesBasket.append(groceries[itemRand])
    newFile = open('baskets/'+idBasket, 'a+')
    newFile.write(idBasket+eol)
    newFile.write(now+eol)
    newFile.write(idName+';'+firstName+eol)
    newFile.write(str(nbOrder)+eol)
    for item in groceriesBasket:
        newFile.write(item['name']+';'+item['type']+';'+str(item['price'])+eol)
    newFile.close()
    sleepTime = random.randint(1, 20)
    time.sleep(sleepTime)
