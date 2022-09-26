/* 

Faire un map reduce avec Map Reduce.

Map reduce permet de réaliser une collection big data personnalisée, à parti d'une collection big Data mongoDb .

Exercice : 
Faire un map reduce pour retrouver quel voitures un ingénieur a créé .
dddd

 */

// Admettons qu'on ait une collection de ce type , dans mongoDb: 
var voitures= [
{
"_id": "voiture:1",
"nom": "Captur",
"year": 2010,
"genre": "berline",
"country": "FR",
"ingenieur": 	{
	"_id": "employe:3"	
	},
"technicien": [
	{
	"_id": "employe:15",
	"role": "roues"	
	},
	{
	"_id": "employe:16",
	"role": "volant"	
	},
	{
	"_id": "employe:282",
	"role": null	
	}
	]
},
{
"_id": "voiture:2",
"nom": "Renault4",
"year": 1979,
"genre": "berline",
"country": "FR",
"ingenieur": 	{
	"_id": "employe:4"	
	},
"technicien": [
	{
	"_id": "employe:5",
	"role": "roues"	
	}
	]
},
{
"_id": "voiture:3",
"nom": "Laguna",
"year": 1997,
"genre": "berline",
"country": "FR",
"ingenieur": 	{
	"_id": "employe:3"	
	},
"technicien": [
	{
	"_id": "employe:109",
	"role": "volant"	
	},
	{
	"_id": "employe:110",
	"role": "roues"	
	}
	]
}
]

// 1. La première fonction "mappe" un attribut du document dans un groupe ( le groupe est l'id de l'ingénieur  dans ce cas )
//  et place en valeur le nom
var mapIngenieur  = function() {
    emit(this.ingenieur._id, this.nom);
};

// 2. La deuxième fonction de reduce prends en paramêtre l'id de l'ingénieur, 
// et les noms de ses voitures qui ont été envoyés par la fonction de map dans le groupe approprié.
var reduceIngenieur = function(ingenieurId, noms) {
   var res = new Object();
   res.ingenieur = ingenieurId;
   res.noms = noms;
   return res;
 };

// 3. On execute le traitement (directement dans robo3t, ou on le récupère dans une variable JS dans un script)
db.movies.mapReduce(mapIngenieur,reduceIngenieur,{out: {"inline": 1}, query: {"country": "FR"}} )