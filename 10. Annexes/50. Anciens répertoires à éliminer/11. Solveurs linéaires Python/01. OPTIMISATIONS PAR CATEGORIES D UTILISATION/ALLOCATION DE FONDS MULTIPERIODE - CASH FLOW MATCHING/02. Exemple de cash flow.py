""" Source : http://web.math.ku.dk/~rolf/CT_FinOpt.pdf
Chapter 3
LP Models: Asset/Liability
Cash Flow Matching
chapitre 3
Modèles LP : Actif/Passif
Appariement des flux de trésorerie """

""" 3.1 Financement à court terme

Les entreprises sont régulièrement confrontées au problème du financement des liquidités à court terme.
engagements. La programmation linéaire peut aider à déterminer une com-
combinaison d'instruments financiers pour faire face à ces engagements. Pour illustrer
ceci, considérons le problème suivant. Pour simplifier l'exposition, nous gardons
l'exemple très petit.

Une entreprise a le problème de financement à court terme suivant.

Month           Jan Feb Mar Apr May Jun
Net Cash Flow -150 -100 200 -200 50 300

Les besoins nets de trésorerie sont exprimés en milliers de dollars. La com-
La société dispose des sources de financement suivantes
• Une marge de crédit pouvant atteindre 100 000 $ à un taux d'intérêt de 1 % par mois,
• Au cours de n'importe lequel des trois premiers mois, il peut émettre des messages commerciaux de 90 jours
papier portant un intérêt total de 2% pour la période de 3 mois.
• Les fonds excédentaires peuvent être investis à un taux d'intérêt de 0,3 % par mois.


L'entreprise peut vouloir répondre à de nombreuses questions.

Combien de paiements d'intérêts l'entreprise devra effectuer entre janvier et
Juin? 
Est-il économique d'utiliser la marge de crédit certains mois? 
Le cas échéant, Combien? 

La programmation linéaire nous donne un mécanisme pour répondre à
ces questions rapidement et facilement. 

Cela permet aussi de répondre à certains "et si"questions sur les changements dans les données 
sans avoir à résoudre le problème.

Et si le Net Cash Flow de janvier était de -200 (au lieu de -150) ? 
Et si la limite de la ligne de crédit est passée de 100 à 200 ? 
Et si le négatif Le cash-flow net de janvier est dû à l'achat d'une machine d'une valeur de 150
et le vendeur autorise une partie ou la totalité du paiement sur cette machine
en juin à un taux d'intérêt de 3 % pour la période de 5 mois ? 

Les réponses à ces questions sont facilement disponibles lorsque ce problème est formulé et résolu
sous forme de programme linéaire.
Il y a trois étapes dans l'application de la programmation linéaire : la modélisation, la résolution,
et interprétariat



 """

