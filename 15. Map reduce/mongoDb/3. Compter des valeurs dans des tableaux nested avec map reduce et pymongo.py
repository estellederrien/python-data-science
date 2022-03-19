""" 

Réaliser un map-reduce avec python et mongodb

(+ Compter le nombre d'éléments d'un tableau inséré dans les objets json)

Source :
https://api.mongodb.com/python/2.0/examples/map_reduce.html

 """


#1. On importe la librairie qui permet de se connecter
from pymongo import MongoClient

# 2. On se connecte à la bonne bdd et collection
client = MongoClient('mongodb://localhost:27017/')
db = client.thing

# 3. On insère des données randomisées, il y a un tableau (arrray) dans chaque objet.
db.things.insert_one({"x": 1, "tags": ["dog", "cat"]})
db.things.insert_one({"x": 2, "tags": ["cat"]})
db.things.insert_one({"x": 3, "tags": ["mouse", "cat", "dog"]})
db.things.insert_one({"x": 4, "tags": []})

# 4. On crée la fonction de map qui envoie dans chaque z (un groupe qui s'appelle par le nom du tag), une valeur de 1 .
# Note : C'est du JS
from bson.code import Code
map = Code("function () {"
 "  this.tags.forEach(function(z) {"
 "    emit(z, 1);"
 "  });"
  "}")

# 5. On crée la fonction de reduce qui récupère pour chaque groupe 'z' ses valeurs associées, puis les compte.
# Note : C'est du JS
reduce = Code("function (key, values) {"
             "  var total = 0;"
               "  for (var i = 0; i < values.length; i++) {"
               "    total += values[i];"
              "  }"
               "  return total;"
               "}")

# 6. On place le résultat dans un tableau d'objets json
result = db.things.map_reduce(map, reduce, "myresults")

# 7. On affiche le résultat dans la console .
for doc in result.find():
    print(doc)

""" 
{'_id': 'cat', 'value': 3.0}
{'_id': 'dog', 'value': 2.0}
{'_id': 'mouse', 'value': 1.0} """