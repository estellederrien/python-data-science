""" 

Réaliser un map-reduce avec python et mongodb

Compter le prix total dépensé par clients.

Source :
https://docs.mongodb.com/manual/tutorial/map-reduce-examples/

 """


#1. On importe la librairie qui permet de se connecter
from pymongo import MongoClient

# 2. On se connecte à la bonne bdd et collection
client = MongoClient('mongodb://localhost:27017/')
db = client.orders

# 3. On insère des données 

myList =[
{"_id":1,"cust_id":"Michel","ord_date":"2020-03-01","prix":25,"items":[{"sku":"oranges","qty":5,"prix":2.5},{"sku":"apples","qty":5,"prix":2.5}],"status":"A"},
{"_id":2,"cust_id":"Michel","ord_date":"2020-03-08","prix":70,"items":[{"sku":"oranges","qty":8,"prix":2.5},{"sku":"chocolates","qty":5,"prix":10}],"status":"A"},
{"_id":3,"cust_id":"Kamel","ord_date":"2020-03-08","prix":50,"items":[{"sku":"oranges","qty":10,"prix":2.5},{"sku":"pears","qty":10,"prix":2.5}],"status":"A"},
{"_id":4,"cust_id":"Kamel","ord_date":"2020-03-18","prix":25,"items":[{"sku":"oranges","qty":10,"prix":2.5}],"status":"A"},
{"_id":5,"cust_id":"Kamel","ord_date":"2020-03-19","prix":50,"items":[{"sku":"chocolates","qty":5,"prix":10}],"status":"A"},
{"_id":6,"cust_id":"Thierry","ord_date":"2020-03-19","prix":35,"items":[{"sku":"carrots","qty":10,"prix":1.0},{"sku":"apples","qty":10,"prix":2.5}],"status":"A"},
{"_id":7,"cust_id":"Thierry","ord_date":"2020-03-20","prix":25,"items":[{"sku":"oranges","qty":10,"prix":2.5}],"status":"A"},
{"_id":8,"cust_id":"Lee","ord_date":"2020-03-20","prix":75,"items":[{"sku":"chocolates","qty":5,"prix":10},{"sku":"apples","qty":10,"prix":2.5}],"status":"A"},
{"_id":9,"cust_id":"Lee","ord_date":"2020-03-20","prix":55,"items":[{"sku":"carrots","qty":5,"prix":1.0},{"sku":"apples","qty":10,"prix":2.5},{"sku":"oranges","qty":10,"prix":2.5}],"status":"A"},
{"_id":10,"cust_id":"Lee","ord_date":"2020-03-23","prix":25,"items":[{"sku":"oranges","qty":10,"prix":2.5}],"status":"A"}
]

# On envoie la collection sur la DB mongoDb.
db.orders.insert_many(myList)

# 4. On crée la fonction de map : 
# Lors du loop sur chaque documents de la collection, 
# custom_id ( Le nom du client) fait désormais office de 'groupe', et this.prix est une valeur ajoutée dans un groupe.
# Note : C'est du JS
from bson.code import Code
map = Code("function() {"
   "emit(this.cust_id, this.prix);"
"};"
)

# 5. On crée la fonction de reduce qui récupère pour chaque groupe cust_id ses valeurs associées (les prix), puis on les somme.
# Note : C'est du JS
reduce = Code("function(keyCustId, valeursPrix) {"
  "return Array.sum(valeursPrix);"
"};")

# 6. On place le résultat dans un tableau d'objets json
resultat = db.orders.map_reduce(map, reduce, "myresults")

# 7. On affiche le résultat dans la console .
for doc in resultat.find():
    print(doc)

""" 
{'_id': 'Kamel', 'value': 125.0}
{'_id': 'Lee', 'value': 155.0}
{'_id': 'Michel', 'value': 95.0}
{'_id': 'Thierry', 'value': 60.0}

kamel a acheté pour 125 euros et Thierry pour 60 euros en tout, dans un intervalle de dates.

 """