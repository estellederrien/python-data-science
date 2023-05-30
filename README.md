# Fichiers Excel et python de recherche opérationnelle ( Optimisations linéaires et non linéaires)
# Scripts de Data sciences, probabilités et machine learning en Python

<b>CAS D'UTILISATIONS .</b>
![Screenshot](iconb.jpg)<br>

##  Français/French

Mon dépot qui traite principalement de la recherche opérationnelle mathématique, des statistiques et des mathématiques avec Python.
Orienté à fond sur la pratique, ou cas d'utilisations faciles à mettre en place, je pars toujours des cas les plus simples.
Souvent mis à jour désormais, avec suivi des "news".


## Dernières news du dépot : 

<p align="center" >
  <img  src="https://github.com/estelle15000/python-data-science/blob/master/operationsresearch.png" >
</p>

30/05/2023 :  Découverte du super livre "Numerical Python" de APress. Décision d'étudier une seule catégorie d'optimisation par semaine ( Les transports et le voyageur de commerce la semaine prochaine). Pour l'instant, je continue l'étude des variables binaires/conditionnelles, et des contraintes de type piecewize, avec des exemples concrets à venir, parce que c'est vraiment trop important à tenter de maitriser. Les eq diffs aussi... 

29/05/2023 : Un problème non linéaire de mix de produits, réduit à sa plus simple expression, avec Python Gekko :
[Problème non linéaire très simple](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/02.%20Non%20lin%C3%A9aire/02.%20PRODUITS%20MIXES/PYTHON/01.%20Plus%20grand%20qt%C3%A9%20d'objets%2C%20moins%20le%20prix%20est%20%C3%A9lev%C3%A9.ipynb)

29/05/2023 :  Ma méthode pour créer des variables de décision et des contraintes en itérant avec un solveur Python :<br>
[Lien Créer des variables de décision](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/04.%20Comment%20utiliser%20les%20variables%20binaires%20-%20conditionelles/02.%20CREER%20DES%20VARS%20DE%20DECISION%20RAPIDEMENT.ipynb)

25/05/2023:Mon Etude des variables conditionnelles binaire et de la méthode BigM en optimisation :<br>
[Lien variables conditionnelles](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/04.%20Comment%20utiliser%20les%20variables%20binaires%20-%20conditionelles/01.%20THEORIE.ipynb)

24/05/2023: Recréation du problème d'ordonnancement excel " Construction d'un stade" de Marc Sevaux et Christian Prins, avec Python Mip  :<br>
[Lien optimisation de durée de projet](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/01.%20Lin%C3%A9aire/06%20-%20GESTION%20DE%20PROJETS%20(%20PROJECTS%20MANAGEMENT)/EXCEL/01%20-%20DUREE%20DE%20PROJET%20MPM%20CHRISTIAN%20PRINS/RECREATION%20PYTHON/Ordonnancement%20de%20projet.ipynb)


01/05/2023: Etablir le meilleur prix pour un objet, à l'aide de l'équation non linéaire de la demande, mon code ( et celui de John Hedengren) : 
[Lien Pricing à l'aide de l'équation N.L de la demande](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/02.%20Non%20lin%C3%A9aire/01.%20ETABLISSEMENT%20DES%20PRIX%20(PRICING)/00.%20Pricing%20de%201%20produit/GEKKO/La%20companie%20M.ipynb)


## Introduction
Je stocke ici divers scripts de data science et de mathématiques <b>descriptives</b> ou <b>prédictives</b> en Python, en langue Française. Mes études sont principalement axées sur les solveurs linéaires, les régressions multiples, les lois de probabilité et les chaines de Markov. Un peu de finances aussi...<br>
<br><B>New 2022</b> : Je vais dorénavant stocker des centaines de fichiers de recherche opérationnelle avec le solveur EXCEL , c'est donc désormais du <b>Prescriptif</b> (Optimisation linéaire et non linéaires mathématique), que je traduis en Français, je leur crée des légendes simplifiées et les valide( Produits mixs, Produits mix non linéaires, Mélanges, Production multi périodes avec gestion des stocks, Job Shop sur multiples machines, Cutting stock, Bin Packing 2d et bien plus etc ... Je crée aussi le code en python correspondant afin de vérifier que les résultats collent entre eux !
je ne fais plus que ça ....<br> 
<br><B>New 2022</b>: I will now store hundreds of operational research files with the EXCEL solver, so it is now <b>Prescriptive</b> (Linear and nonlinear mathematical optimization ), which I translate into French, I create simplified legends for them and validate them (mixed products, non-linear mixed products, mixtures, multi-period production with inventory management, Job Shop on multiple machines, Cutting stock, Bin Packing 2d and many more etc. I will create the corresponding Python solver code too ...
I just do that....<br>

<p align="center" >
  <img  src="https://github.com/estelle15000/python-data-science/blob/master/2007_solveur2.jpg" >
</p>

Important : Il faut savoir que les valeurs dans les fichiers Excel pourraient provenir de bases de données et non pas être des valeurs 'statiques'  , et donc se modifier en temps réel, et pas seulement être statiques, ce qui procure une puissance incroyable au Solveur Excel. Je tente également de comparer les résultats  en python à ceux en Excel dès que c'est possible, pour l'instant, c'est assez largement OK, et les solveurs trouvent les mêmes résultats (Solveur Excel = Solveur Python).
<br><br>
N'hésitez pas à consulter mon application commerciale ,  www.solvgraph.com ,![alt text](http://www.solvgraph.com/static/img/output-onlinepngtools.213abb5a.png) pour comprendre plus facilement ce qu'est la Recherche opérationnelle, en mode graphique, ainsi que son grand intérêt pour les entreprises.<br><br>
Do not hesitate to consult my commercial application, www.solvgraph.com, to understand more easily what Operational Research is, in graphic mode, as well as its great interest for companies.


## News (suite)

24/03/2023: En train d'évaluer comment je vais coder en full stack l'intégration de Gekko Solver à mon application www.solvgraph.com . Je pense commencer par proposer le pricing non linéaire, le products mix non linéaire, le Portefeuille aux moindres carrés, ce sera déjà un bon départ, mais une évaluation globale des modèles de data et du fonctionnement de SolvGraph au niveau des components est nécessaire.
www.solvgraph.com doit router vers les solveurs, et proposer un mode graphique facile. Le travail est assez énorme. Un audit de ma propre application effectué par moi même est nécessaire, afin de la faire évoluer.
le back end n'est pas difficile à réaliser, une fois que je l'ai testé, je sais qu'il fonctionne. Par contre, le Front end est assez difficile quand aux choix à entreprendre quand à ne pas révinventer la roue, mais de ne pas arriver à un code incompréhensible par de futurs collaborateurs. L'intérêt de Solvgraph est bien sur de proposer une surcouche graphique de facilité extrême pour faire de la recherche opérationnelle mathématique en temps réel, en mode graphique, et d'avoir des résultats irréprochables identiques à Excel, par exemple(Sinon, quel serait l'intérêt ?).
La plus grande difficulté est de gérer le transfert du modèle de data du front end au solveur back end, ceci est opéré par une fonction spécifique, qui au fil du temps et des différents modèles mathématiques et leurs spécificité, a tendance a devenir trop lourde à lire pour les partenaires, sans parler des components qui devront à l'avenir finalement être parfois totalement personnalisés, un travail gigantesque, mais pas impossible. Vu la complexité du système, un schéma UML est pour le coup vraiment nécessaire, pour faire le point et avancer. 
C'est cette fonction qui transfère et formatte l'instance mathématique d'une optimisation (les datas) du front end au back end que je vais réécrire (La fonction ne sera plus dans le front end et en Js, mais en Python dans le back end) et simplifier, afin d'aborder le non linéaire en mode graphique plus facilement.


03/24/2023: Evaluating how I will full stack code the Gekko Solver integration to my www.solvgraph.com application. I think to start by proposing the non-linear pricing, the non-linear product mix, the least squares Portfolio, it will already be a good start, but a global evaluation of the data models and the functioning of SolvGraph at the component level is necessary. www.solvgraph.com must route to solvers, and offer an easy graphing mode. The work is quite enormous. An audit of my own application carried out by myself is necessary, in order to make it evolve. the back end is not hard to make, once i tested it i know it works. On the other hand, the Front end is quite difficult when it comes to the choices to be made when not to reinvent the wheel, but not to arrive at a code incomprehensible by future collaborators. The interest of Solvgraph is of course to offer a graphic overlay of extreme ease to carry out operational research in real time, in graphic mode, and to have irreproachable results (Otherwise, what would be the interest?).
The biggest difficulty is to manage the transfer of the data model from the front end to the back end solver, this is operated by a specific function, which over time and with the different mathematical models and their specificities, tends to become too cumbersome to read for the partners, not to mention the components which will in the future have to be sometimes completely personalized, a gigantic task, but not impossible.Given the complexity of the system, a UML diagram is really necessary, to take stock and move forward.
It is this function which transfers and formats the mathematical instance of an optimization (the data) from the front end to the back end that I will rewrite (The function will no longer be in the front end and in Js, but in Python in the back end) and simplify, in order to approach the nonlinear in graphic mode more easily.







06/03/2023:
Découverte du cours du Mit en ligne :
https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/resources/mit15_053s13_lec11/

Surtout pour les contraintes conditionelles binaires en programmation linéaire et surtout les contraintes piecewise linear functions pour par exemple avoir des coûts variables en fonction des quantités dans des lps de type produit mixes.

Egalement : 
https://download.aimms.com/aimms/download/manuals/AIMMS3OM_IntegerProgrammingTricks.pdf

05/02/2023 : Je suis toujours en train de principalement réaliser le répertoire 02 Recherche opérationnelle . Je passe le tout en Notebooks python et je continue bien sur à en ajouter, ainsi que du Solveur Excel, surtout du non linéaire  à l'avenir...
Je fais aussi dorénavant le répertoire 3 machine Learning et il faut aussi que je fasse les équations différentielles et le traitement du signal ... Le dépot n'est donc pas du tout en état définitif , en travaillant tous le sjours dessus, il y en a encore pour un ou deux ans au moins ,je dirais.<br>

22/01/2023 : Restructuration et correction des lois de probabilités, en particulier Poisson et passages en fichier notebooks directement visualisable dans github, J'utilise prioritairement les fonctions SCIPY désormais (poisson.cdf, uniform.cdf , expon.cdf etc...). Le bon lien : https://www.w3schools.com/python/numpy/numpy_random_exponential.asp<br>

26/10/2022 : J'avance désormais sur les optimisations non linéaires sous Excel et le Solveur Gekko Python
<br>I'm now starting to tackle lots of non linear optimizations using the Excel Solver and the Gekko Solver !
:


[Lien optimisation en français non lin](https://github.com/estelle15000/python-data-science/blob/master/01.%20Recherche%20op%C3%A9rationnelle%20(Operations%20research%20-%20Management%20science)/02.%20Non%20lin%C3%A9aire/01.%20PRODUITS%20MIXES%20N.L%20(PRODUCTS%20MIXES)/04.%20Fabrique%20de%20tshirts%20avec%20contraintes%20multiples/GEKKO/Produit%20mix%20n-l%20avec%20contraintes.ipynb)

26/09/2022 : Réduction drastique du nombre de répertoires ! Les optimisations avec le solveur Excel sont encore en cours de tri mais à la fin , ca va être très bien , et je crée les fichiers en python équivalents dès que je peux et les place dans le même répertoire... Pour le machine learning, j'ai pleins de nouveaux livres ( Surtout du O'reilly) et j'en fait 35% du temps par rapport à la Recherche opérationnelle.

22-09-2022 : Passage définitif en fichiers ipynb, Notebook python pour plus de simplicité pour les optimisations en Python Pulp et Gekko. On peut voir directement les fichiers fonctionner dans Github, c'est beaucoup plus ludique.

15-09-2022 : Création du nouveau répertoire 33 recherche opérationnelle , trié par catégories d'optimisations , ou il y aura dans chaque cas le code Excel, Pulp et Gekko. Ce sera beaucoup plus simple ! Les catégories sont tirées des livres référence d'optimisation Excel et aussi d'Internet, comme ça, c'est standardisé.

27-07-2022 : Très important, découverte de 2 livres majeurs de référence en anglais, abordant tous les thèmes et modèles mathématiques , au moins 800 pages:

- B W Taylor - Introduction to management science  - Pearson
- Wyane Winston  - Practical Management science - winston Albright 
<br>
J'aurais préféré les trouver tout de suite.

Pour les exercices :
- Step by step optimization with excel solver - Mark Hamon mba
- optimizations modeling with spreadsheets - Wiley

Pour les statistiques (descriptif): 
- Aide mémoire Statistiques et probabilités - Dunod 2 ème édition
- Premiers pas en statistiques de Pearson

Cours Coursera - Université Taïwan - Operation research :
https://lnkd.in/e_UhSs-k

Udemy - Solveur Excel - optimisations linéaires et non linéaires :
https://lnkd.in/e2y8AGJS

Le cours Pyomo est vraiment spécifique et mathématique,voir mécanique, mais très bien ( Optimisation d'objet dans un container cylindrique etc ...)
https://lnkd.in/ekZeQmpx



10-06-2022 : Découverte d'une librairie dédiées aux problèmes à objectifs multiples : https://pymoo.org/getting_started


10-06-2022 : Répertoire 11 / 03. Production planifiée - Comparaison Excel/Python Pulp : Le fichier excel et python ne donnent pas le même résultat objectif - mais les mêmes ordonnances de planification de production par mois. La raison est que le calcul de la fonction objectif utilise une valeur de stock moyen ' average ' dans Excel, mais  le script Python ( Qui est exact) , lui, ne calcule pas le résultat de l'objectif ( Minimiser le cout ) en utilisant cette valeur de stock moyen (average inventory), qui est optionnelle.<br><br>

23-05-2022 : Découverte de l'excellente page wikipedia traitant de l'ordonnancement d'atelier, très très claire !  (Job shop, flow shop): 
https://fr.wikipedia.org/wiki/Ordonnancement_d%27atelier

23-05-2022 : Découverte du magnifique site du cours B6015: Decision Models de Columbia university, avec des tas d'exemples du solveur excel opérationnels et de la finance ( En particulier, l'allocation de fonds) ! 
https://www.meiss.com/columbia/en/teaching/2000/fall/B6015/#Download

23-05-2022 : Ajout dans le rep 11 des scripts python pulp de planification de production multi période + Comparaison avec le solveur Excel = Python Pulp et le Solveur Excel trouvent exactement le même résultat !
05-23-2022: Addition in rep 11 of the python pulp scripts for multi-period production planning + Comparison with the Excel solver = Python Pulp and the Excel Solver find exactly the same result!



20-05-2022 : 2 excellents cours de R.O en Anglais, j'hallucine devant la qualité et précision du cours dispensé : 
Cours Coursera - Université Taïwan - Operation research :<br>
https://www.coursera.org/learn/operations-research-modeling?action=enroll

Cours Udemy - Solveur Excel - optimisations linéaires et non linéaires :<br>
https://www.udemy.com/course/optimization-with-excel-operations-research-without-coding/

20-05-2022 : Ajout du répertoire 28 , pour les scripts du solveur non linéaire GEKKO

12-04-2022 : Restructuration du répertoire 11 Solveurs linéaire + ajout de codes Product mixes incluant affichage des ressources inutilisées et shadow price en python pulp

27-04-2022 : Découverte du superbe site http://mba.tuck.dartmouth.edu/opt/index.html du super livre "Optimization Modeling with Spreadsheets" - Présence et explication d'un modèle de Job Shop avec disjonctions + Ficher excel ! Ce livre fait partie de mes  4 livres d'optimisation linéaire avec Excel en Anglais que j'étudie désormais, Microsoft Excel 2013 Data Analysis and Business Modeling , et Step-By-Step_Optimization_S et Wayne_L._Winston_S._Christian_Albright_Practical_Management_Science</br>

25-04-2022 : Découverte du programme Lekin 2010  pour gérer les optimisations linéaires Job Shops / Flow Shop <br>



- 08-04-2022 : 26. Recherche opérationnelle en Excel - > Je prends chaque problème linéaire EXCEL , valide les résultats, puis les traduits ( Quand ce ne sont pas ceux de Christian Prins et Marc Sevaux) et ajoute des légendes. A terme, j'aurais chaque catégories de programmes linéaires parfaitement triés et susceptibles d'êtres modifiés en fonction des besoins.


- 06-04-2022 : Les fichiers 'MULTIPLES' du répertoire 'Recherche opérationnelle avec Excel' sont fantastiques avec optimisation d'affectation sur une semaine par exemple -> création de légendes et traductions.. C'est précisément ça qui est très difficile à coder en full stack (Python + Js) dans www.solvgraph.com, pourtant, en toute logique, ça doit être possible à l'avenir, mais très difficile.
L'objectif est de parvenir à programmer les 'objectifs multiples' et les 'groupes de variables de décisions' en python ( et aussi dans Excel)





- 30-04-2021 : Ajout du répertoire de la théorie des files d'attente. Découverte du site de cours de mathématiques de université Lille L1 L2 et L3 : http://exo7.emath.fr/index.html

- 19-02-2021 : Création du chapitre "19. Notebooks de Data Science Kaggle, traduits en Français" , avec des stats simples, mais aussi, du Keras et du Tensorflow (Machine Learning), pour l'analyse de photos ( Exemple : détection de cancers)...

- 10-02-2021 - J'ai désormais une tablette avec des tas de livres, et j'en prends 2 ou 3 à étudier seulement(Toujours les mêmes) et retranscrit des formules en python dans ce dépot GITHUB dès que possible, triées par chapitres. Cette année c'est :


Introduction to machine learning de Andreas Muller ...chez O'reilly en Anglais : Super bien écrit et facile à comprendre.



Dunod - Mini manuel de mathématiques financières: Il contient d'excellentes bases .( Je retranscrit les formules de Maths du livre en python dans mon chapitre 5)

Mastering Python for Finance by James Ma Weiming : Livre En anglais, bien écrit et assez difficile, avec les scripts de la frontière efficace  (efficiente), du Python Pulp, etc ..

--> Mon objectif est d'utiliser dans des apps concrêtes les formules de Finances en gestion de Portfolios(Portefeuille), Les probabilités en chaines de Markov et les solveurs linéaires en programmation linéaire ( Pour mon app : http://solvgraph.com)

- 17-11-2020 - Excellent lien en Français ! : https://dridk.me/
- 17-11-2020 - Lien difficile pour les équations différentielles, en Anglais: https://apmonitor.com/pdc/index.php/Main/PhysicsBasedModels



## Notebooks de Data Science à télécharger sur Kaggle (En Anglais)!
https://www.kaggle.com/notebooks<br><br>
ting 
## Modifier les notebooks Python avec Anaconda et Jupiter : 
![Screenshot](anacondanew.jpg)<br>
Ensuite, cliquer sur " Home " , "Jupiter Notebooks", et ouvrir ou créer un notebook...

## Pourquoi créer des notebooks Python n'est il pas suffisant ?
Parce qu'il faut aussi savoir créer des apps réelles en Full stack, puis tenter un business model quelconque , pour la vendre. Il faut donc également savoir programmer en Full Stack ( y compris du JS), en plus de faire de la Data science. Voilà pourquoi j'ai aussi des fichiers .py que je peux placer sur un serveur Flask, sur Heroku par exemple. 

## Références (Livres)

Maths : 
- "Mathématiques L1 L2 - 30 fiches" Dunod
- "Aide mémoire , Statistiques et probabilités pour l'ingénieur " Dunod
- "Mathématiques pour l'informatique" ( Version bts sio, plus courte que la version compléte ) de Dunod
- "Outils mathématiques pour l'informaticien, mathématiques discretes" De Boaeck
- "Programmation linéaire avec Excel" https://www.eyrolles.com/Informatique/Livre/programmation-lineaire-avec-excel-9782212126594/
- Livres de Maths de révision de lycées ( 2nd, Séries L, éco, S et Stg et quelques uns de collège 3 ème).
- "Mathématiques appliquées à la gestion" Pearson education ( + difficile)
- https://www.cmath.fr/

Général :
- " Visa pour la prépa " de DUNOD

Statistiques : 
- "Premiers pas en statistique" de Springer :Toutes les bases incontournables en stats : https://www.springer.com/gp/book/9782287302787

Finances:
- "Mastering Python for Finance" by James Ma Weiming
- "Mini manuel de mathématiques financières" - Dunod

Data science et ML : 
- " Big Data et Machine Learning, Manuel du Data scientist " Dunod
- " Apprendre le ML en 2 semaines" de la chaine youtube Machine Learnia
- " Data science for dummies" : La data science pour les nuls, en anglais.
- " Introduction to machine learning with python" O reilly , en anglais
- 
BI :
- " Talend for Big Data" Packt

Projets : 
- "Logistique" de Dunod , Yves Pimor"
- Lean :  " Toyota Supply Chain Management A Strategic Approach to Toyotas Renowned System" by Ananth Iyer, Sridhar Seshadri, Roy Vasher
- "Gestion de projet pour les nuls"
- " La méthode Prince 2"


Divers :
- "Maxi fiches Physique , 2 ème édition - Mécanique , Thermodynamique, Electricité, ondes , optique pour L1 et L 2 " Dunod
- " L'électronique de Poche pour les nuls"
- " La comptabilité pour les nuls"


--> Professeurs, Phd doctorants, et liens en Français :

- Le site d'un professeur de l'ENSAE: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a.html#machine-learning-les-briques-de-bases<br>
- Sacha Schutz : https://dridk.me/ et  https://dridk.me/equation-differentielle.html



## Infos : 
<b>Les scripts possédant la lettre C au début de leur noms ont un statut confirmé.</b><br>
<b>Les scripts possédant l'attribut BASE au début de leurs noms sont les plus simples et fiables.</b><br>
<b>Les scripts possédant la lettre KO au début de leurs noms ont un statut à vérifier ou en défaut.</b>
<br>
(Note : Confirmé, veut dire résultat bon, confirmé par comparaison, cependant, la méthode/stratégie pour obtenir le resultat n'est pas forcément encore la meilleure, les fonctions peuvent parfois être très laides.)</br>
<br>

## Librairies utilisées
* numpy<br>
* matplotlib<br>
* pandas<br>
* scipy<br>
* sklearn<br>
* pulp (Solvers)<br>
* pyschedule https://github.com/timnon/pyschedule<br>
* Survival regression https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#the-dataset-for-regression <br><br>

## Les Chaines Youtube Françaises:

<b>Data science, Machine Learning : </b><br>
Machine Learnia https://www.youtube.com/channel/UCmpptkXu8iIFe6kfDK5o7VQ<br>
Nicolas Br https://www.youtube.com/channel/UCzsU0h6kxkSSCqpXTRUHubg<br>
Science4All : https://www.youtube.com/watch?v=Jf40Xd52NyQ<br><br>

  
<b>Maths :</b><br>
Clipedia : https://www.youtube.com/channel/UCNwWU1hqK3q-DclufllWCfg<br>
ProMath : https://www.youtube.com/channel/UC2flwAftkypBx2gLIamxwqg<br>
J'ai compris Maths : https://www.youtube.com/channel/UCo-O74A4qVz6nq5cfCIee6w<br>
Yvan Monka : https://www.youtube.com/user/YMONKA<br>
Saïd Chermak : https://www.youtube.com/channel/UCppNXkk1sgDguxe8fQK9tng<br>

**Excellente chaine d'optimisation en Anglais ( explications très simples et structurées) :**<br>
https://www.youtube.com/channel/UC1S4Jeodbr5EbsCOIgBWJPQ<br>
Example : Les contraintes binaires en optimisation : https://www.youtube.com/watch?v=B3biWsBLeCw

<b>Liens et références (Suite)</b><br>
A regarder également le super dépot Columbia-Intro-Data-Science avec tout le travail d'étudiants de Columbia dans ce domaine avec Python.<br>

https://github.com/Columbia-Intro-Data-Science<br>

Les cours sont ici : <br>
https://github.com/Columbia-Intro-Data-Science/APMAE4990-/tree/master/notebooks<br>

Un autre dépot sympa :<br>
https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers<br>

- http://www.jybaudot.fr/Bourse/theoptf.html : Le site de Jy Baudot


## Ecoles :
1. S'inscrire à l'université de Brest : http://formations.univ-brest.fr/fr/index.html
2. S'inscrire à l'université de Rennes  : https://formations.univ-rennes1.fr/master-1-data-science
3. S'inscrire à l'EICNAM : http://ecole-ingenieur.cnam.fr/hors-temps-de-travail/inscription-a-l-eicnam/
4. S'inscrire à l'ENSAE : https://www.ensae.fr/auditeurs-libres/
5. S'inscrire à L'université de Bordeaux : http://www.math.u-bordeaux.fr/~mchave100p/teaching/ https://www.math.u-bordeaux.fr/imb/spip.php<br><br>
6. S'inscrire au D.U de Statistiques à Toulouse : https://www.ut-capitole.fr/formations/se-former-autrement/formation-ouverte-et-a-distance/diplome-universitaire-statistique-appliquee-formation-a-distance--326811.kjsp?RH=1319186952079

## Moocs :
Coursera <br>
- Programmer en Python pour la Data Science de A à Z :https://www.udemy.com/course/data-science-avec-python/<br>
- Les Data Sciences de A à Z  : https://www.udemy.com/course/les-data-sciences-de-a-a-z/<br>
- Spécialisation Science des données appliquée avec Python : https://fr.coursera.org/specializations/data-science-python<br>
- Modélisation financière : https://www.coursera.org/specializations/finance-quantitative-modeling-analysts#courses<br><br>
- real-data-science-problems : https://www.udemy.com/course/real-data-science-problems-with-python/<br>
- Finances : https://www.my-mooc.com/fr/mooc/python-and-statistics-for-financial-analysis/<br>

Tous les cours de programmation linéaire : <br>
- https://www.udemy.com/courses/search/?q=%22LINEAR%20PROGRAMMING%22&src=sac&kw=linear%20programmaing<br><br>

Moocs de Maths:<br>
- https://www.fun-mooc.fr/courses/course-v1:MinesTelecom+04008+session06/about<br><br>

Moocs de sciences Physique : <br>
- https://www.my-mooc.com/fr/categorie/physique<br><br>


##  Collabs : 
Vous désirez collaborer avec moi (Surtout sur les solveurs linéaires ( Monde agricole, productions alimentaires, production et j'espère... finance)) ... Ok ! envoyez moi un message<br>

<br>

## English
Just Some ordered python regressions, various maths and linear solvers studies scripts...

## Books
Data science for dummies : <br>
- https://www.amazon.fr/Python-Data-Science-Dummies-Mueller/dp/1119547628<br>
Python Data Science Handbook :<br>
- https://jakevdp.github.io/PythonDataScienceHandbook/<br>

## Info 
Files with the C letter at the start of their names have confirmed status. <br>
Files with the KO letters at the beginning of their names have a result to check or fail.

