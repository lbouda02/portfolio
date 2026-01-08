# Construction d’un index d’inégalités de santé

## Présentation du projet
Réalisé au cours de mon stage en Roumanie, ce projet visait à étudier les inégalités de santé à l’échelle européenne en exploitant la base de données **EHIS Wave 3**. L'objectif était de construire un index de santé composite fidèle aux standards du **SF-36 Health Survey** pour évaluer de manière synthétique l’état de santé auto-perçu et révéler des disparités entre pays.

## Étapes de réalisation

### Familiarisation et exploration des données
* Analyse de la structure modulaire de la base EHIS.
* Étude des variables, des pondérations et de la codification des réponses.
* Gestion des données manquantes pour anticiper les défis du nettoyage.

### Recodage et alignement méthodologique
* Étude du SF-36 (santé physique, mentale, limitations fonctionnelles).
* Utilisation d'un script **R** pour transformer les modalités qualitatives en variables numériques.
* Inversion d'échelles pour la cohérence directionnelle et normalisation des scores.

### Construction de l’index composite
* Assemblage des variables en un score unique par individu via une somme brute.
* Filtrage strict des valeurs aberrantes.
* Exclusion des réponses non applicables (systématiquement codées en -1).

### Analyse statistique et visualisation
* Utilisation des packages **ggplot2** et **dplyr** sous R.
* Production de visualisations révélant les inégalités entre pays et catégories socio-économiques.

# Projet OAT : Outil d'Automatisation des Tests (Octobre 2024)

## Présentation du projet
Projet réalisé avec le **Laboratoire de la Vendée** visant à concevoir un outil simplifiant l’interaction avec les fichiers **.robot** (**Robot Framework**). L'objectif était de permettre à des utilisateurs sans connaissances en programmation de manipuler des processus d'automatisation (**RPA**).

## Détails techniques
* **Interface :** Interface graphique développée en **Python** avec **Tkinter**.
* **Fonctionnalités :** Charger, modifier, sauvegarder et exécuter des fichiers .robot localement.
* **Architecture :** Fonctionnement sans base de données ni connexion Internet.

## Défis et solutions
* **Analyse :** Traduction des besoins fonctionnels en interface opérationnelle et immersion dans la syntaxe des fichiers .robot.
* **Gestion des données :** Utilisation de fichiers texte ou de variables internes pour gérer les enregistrements et les données volumineuses.
* **Technique :** Ajustements précis pour l'édition ligne par ligne et la synchronisation du scroll avec la numérotation personnalisée.

## Résultats et évolutions
L'outil permet de traduire des commandes techniques en langage clair. Des axes d'amélioration sont identifiés : fluidité de navigation, gestion dynamique de fichiers multiples, ergonomie et portage vers une version web ou multiplateforme.


# Répondre aux besoins du territoire (Enseignement)

## Présentation du projet
Ce projet répondait à un besoin externe à l'IUT. J'ai choisi la voie de l'enseignement pour explorer le métier de professeur, par intérêt pour la transmission de connaissances.

## Réalisation
* **Public :** Collégiens.
* **Mission :** Dispenser trois cours sur les bases d'**Excel** et la création de **graphiques**.
* **Finalité :** Préparer les élèves à un concours de dataviz avec des élèves de seconde.

## Apprentissages critiques
* **Pédagogie :** Présentation claire de concepts, adaptation du discours et communication.
* **Collaboration :** Travail avec des collégiens et des enseignants du secondaire (collaboration interdisciplinaire).
* **Technique :** Mise en pratique et renforcement de la compréhension des fonctionnalités d'Excel.
* **Impact social :** Contribution au développement des compétences des jeunes de la communauté locale.


# Reporting d'une analyse multivariée

## Présentation du projet
L'objectif était de présenter une analyse sur les **accidents de la route** (période 2009-2022) sous la forme d'une application **R Shiny**. Le projet s'appuie sur plusieurs fichiers Excel concernant les usagers et les véhicules.

## Compétences développées

### Maîtrise de R Shiny
* Création d'une application interactive pour la visualisation des données.

### Manipulation de données complexes
* Fusion, nettoyage et préparation de données issues de plusieurs fichiers sources Excel.

### Analyse statistique
* Utilisation de techniques d'analyse multivariée pour explorer les relations entre les variables.

### Communication et Gestion de projet
* Présentation claire des résultats pour différents publics.
* Gestion du cycle complet : de la collecte des données à la création de l'application, en respectant les délais et l'organisation.

# Développement d'un composant d'une solution décisionnelle

## 📌 Présentation du projet
L'objectif central de ce projet était la création d'une **API** (Interface de Programmation d'Applications) pour permettre la communication entre différentes applications. 

Dans ce contexte précis, nous devions exploiter des données structurées provenant de **fichiers XML** et les rendre accessibles via cette interface. L'application a été déployée en utilisant **Docker** pour garantir la portabilité et la gestion des environnements.

---

## 🛠️ Technologies et outils
* **Langage de programmation :** Python.
* **Format de données :** XML (source) et JSON/XML (retour API).
* **Déploiement :** Docker (construction et exécution d'images).
* **Système :** Commandes Linux pour la gestion des conteneurs.

---

## 🧠 Apprentissages critiques

### Compréhension approfondie des API
* Apprentissage des règles et protocoles pour permettre l'interaction entre services.
* Conception d'une interface robuste et cohérente pour la communication applicative.

### Maîtrise de l'intégration avec Docker
* Construction et exécution de conteneurs Docker.
* Compréhension pratique de la virtualisation des applications et de la gestion des environnements de développement.

### Manipulation de fichiers XML
* Extraction d'informations pertinentes à partir de données structurées.
* Formatage approprié des données pour les rendre accessibles via l'API.

### Développement en Python
* Utilisation de bibliothèques spécifiques pour manipuler les données.
* Gestion des requêtes HTTP pour construire une interface performante.

### Gestion des erreurs et des exceptions
* Anticipation des problèmes techniques et mise en place de mécanismes de gestion des erreurs.
* Garantie de la fiabilité et du bon fonctionnement continu de l'application.

---

> **Bilan :** Ce projet a permis de développer des compétences essentielles en développement logiciel, en intégration de technologies (Docker/Python) et en gestion de données structurées.


# Conformité réglementaire pour traiter/analyser des données

## 📌 Présentation du projet
L'objectif de ce projet était de comprendre en profondeur la réglementation entourant la gestion des données. Le travail s'est appuyé sur le cas d'une **entreprise fictive** sollicitant des conseils stratégiques sur l'utilisation et la gouvernance de ses données.

---

## ⚖️ Axes d'analyse et d'exploration

### Cadre réglementaire et bonnes pratiques
* Étude des **bonnes pratiques** à adopter pour le traitement des données.
* Identification des **erreurs à éviter** pour garantir la conformité.

### Gestion du stockage des données
* Définition des **types de données** autorisés à être stockés par l'organisation.
* Analyse des règles relatives à la **durée de conservation** des informations (combien de temps les données peuvent être légalement gardées).

---

> **Bilan :** Ce projet a permis d'acquérir une vision concrète des enjeux juridiques et éthiques liés à la manipulation des données en entreprise.

# Description et prévision de données temporelles

## 📌 Présentation du projet
L'objectif de ce projet était de réaliser des prévisions sur le **taux de chômage** d'un État des États-Unis. Pour cette étude, j'étais en charge des données relatives à l'État du **Tennessee**.

---

## 🛠️ Méthodologie et Modélisation
Afin d'obtenir les prévisions les plus fiables, une phase de test et de comparaison de modèles a été mise en place :

* **Modèles testés :** Utilisation de plusieurs approches, notamment des modèles **linéaires** et **exponentiels**.
* **Critère d'évaluation :** Évaluation de la performance de chaque modèle en mesurant l'**écart avec les valeurs réelles**.
* **Sélection :** Identification du modèle présentant le moins d'écart pour garantir la précision des prévisions.

---

> **Bilan :** Ce projet a permis d'appliquer des techniques de modélisation statistique à des données réelles pour anticiper les tendances économiques d'un territoire spécifique.


# Collecte automatisée de données web

## 🏁 Présentation du projet
Ce projet s'articulait autour de deux axes : une mise en pratique technique du **web scraping** et une étude théorique sur le fonctionnement des **API**. L'objectif final était de collecter, analyser et visualiser les données des vainqueurs du championnat de Formule 1.

---

## 🕷️ Partie 1 : Web Scraping
L'objectif était d'extraire automatiquement des données de la page Wikipedia des vainqueurs de la Formule 1 pour créer une page web comportant une carte et des graphiques.



### Méthodologie et outils
* **Configuration :** Utilisation de **Python** avec les librairies **BeautifulSoup** (parsing HTML) et **Requests** (requêtes HTTP).
* **Extraction :** Récupération du contenu HTML pour extraire les noms des vainqueurs, les années de victoire et le nombre de victoires par coureur et par pays.
* **Nettoyage :** Organisation des données dans un format structuré (DataFrame **pandas**).

### Visualisation et restitution
* **Graphiques :** Utilisation de **Matplotlib** et **Seaborn** pour illustrer les tendances et la dominance par nation.
* **Cartographie :** Création d'une carte interactive avec **Folium** pour afficher géographiquement les pays d'origine des vainqueurs.

---

## 🌐 Partie 2 : Théorie des API
Une API (Application Programming Interface) est un ensemble de règles et protocoles permettant à différentes applications de communiquer entre elles et d'accéder à des fonctionnalités ou données tierces.



### Usages identifiés :
* **Accès en temps réel :** Scores sportifs, météo, taux de change.
* **Automatisation :** Notifications, gestion d'utilisateurs, analyse de données.
* **Intégration :** Paiements en ligne, services de messagerie ou cartes interactives.

*Note : Bien que non utilisée directement dans ce projet, l'API aurait pu apporter une dimension dynamique avec des résultats de courses en temps réel.*

---

> **Conclusion :** Ce projet a permis de pratiquer la collecte automatisée et l'analyse de données historiques. La mise en évidence des tendances de la Formule 1 via des outils de visualisation constitue une compétence clé pour l'analyse de données future.


# Estimation par échantillonnage

## 📌 Présentation du projet
L'objectif de ce travail, réalisé avec le logiciel **R**, était de développer des compétences dans l'appréhension de l'incertitude et de la précision de l'estimation d'une grandeur mesurable dans une population. Le projet s'est appuyé sur l'utilisation d'**intervalles de confiance** basés sur des processus d'échantillonnage.

---

## 🛠️ Méthodologie
Le processus d'échantillonnage a été structuré en deux étapes distinctes :
1.  **Sondage aléatoire simple :** Utilisation de probabilités égales où tous les individus de la population ont le même poids.
2.  **Sondage ou échantillonnage par strates :** Mise en œuvre d'une méthode segmentée pour affiner l'estimation.





---

## 🧠 Compétences acquises
* **Maîtrise du logiciel R :** Utilisation de l'outil pour l'analyse statistique avancée.
* **Théorie de l'estimation :** Compréhension du concept d'estimation et de l'incertitude associée.
* **Méthodes d'échantillonnage :** Connaissance des différentes méthodes et de leurs implications pratiques.
* **Construction statistique :** Capacité à mettre en œuvre des sondages et à construire des intervalles de confiance pour des estimations de population.
* **Interprétation :** Aptitude à analyser et interpréter les résultats obtenus à partir des intervalles de confiance.

---

> **Bilan :** Ce projet a permis de comprendre les principes fondamentaux de l'estimation statistique. Grâce à la pratique sur R, je suis désormais en mesure de choisir la méthode d'échantillonnage appropriée selon le contexte et d'évaluer la précision des estimations pour prendre des décisions éclairées.

# Analyse de données, reporting et datavisualisation (Recrutement)

## 📌 Présentation du projet
L'objectif de ce projet était de concevoir un **outil d'aide au recrutement de masse** en utilisant la programmation Python. Le système permet d'automatiser le traitement des candidatures, d'analyser les profils et de faciliter la prise de décision pour les services RH.

---

## ⚙️ Fonctionnalités de l'outil
L'outil a été développé pour optimiser chaque étape du processus de sélection :
* **Traitement des données :** Filtrage et tri automatisé des données de recrutement pour extraire les informations pertinentes.
* **Profilage des candidats :** Création d'indicateurs spécifiques pour évaluer les compétences et l'adéquation des candidats avec les postes.
* **Aide à la décision :** Capacité à générer des explications pour les décisions favorables ou défavorables.
* **Automatisation :** Génération automatique d'un fichier de synthèse (reporting) regroupant l'ensemble des candidats.
* **Interface Graphique :** Création d'une interface conviviale pour faciliter l'accès aux fonctionnalités sans manipulation directe du code.



---

## 🧠 Compétences acquises

### Développement et Programmation
* Maîtrise de **Python** pour la création d'outils dynamiques.
* Conception d'interfaces graphiques pour améliorer l'expérience utilisateur.
* Manipulation de fichiers et génération automatisée de rapports de synthèse.

### Analyse et Stratégie RH
* Expertise dans l'analyse et le tri de données de recrutement.
* Développement de critères d'évaluation et d'indicateurs de profilage.
* Compréhension approfondie des critères de sélection utilisés par les services RH.

---

> **Bilan :** Ce projet permet d'optimiser le processus de recrutement en réduisant le temps de tri tout en améliorant la qualité et la transparence des décisions prises par le service RH.


# Dataviz (SNCF)

## 📌 Présentation du projet
L'objectif de ce projet était de concevoir une **dataviz** (visualisation de données) pour la **SNCF**. Le travail consistait à exploiter une base de données fournie afin de traduire les informations brutes en représentations visuelles exploitables.



---

## 📊 Objectifs et réalisation
Le projet s'est concentré sur les points suivants :
* **Exploitation de données :** Utilisation de la base de données spécifique à la SNCF.
* **Analyse d'indicateurs :** Mise en évidence d'indicateurs clés pour faciliter la compréhension des données.
* **Représentation visuelle :** Création de supports visuels permettant une lecture rapide et efficace des informations.

---

> **Bilan :** Ce projet a permis de transformer des données complexes en outils visuels clairs, facilitant ainsi l'identification et le suivi des indicateurs de performance de la SNCF.


# Régression sur données réelles

## 📌 Présentation du projet
L'objectif de ce projet était de concevoir un modèle statistique capable de prédire avec précision les **prix de vente de logements**. Le travail incluait également la rédaction d'un texte explicatif détaillant la démarche analytique entreprise.

---

## 🛠️ Méthodologie et Modélisation
Pour construire ce modèle de prédiction, nous avons exploité un jeu de données d'entraînement regroupant diverses caractéristiques (type de logement, surface, etc.).

* **Sélection de variable :** Après analyse, la variable la plus pertinente pour prédire les prix s'est avérée être la **surface du logement**.
* **Outil utilisé :** Le logiciel **R** a été utilisé pour la syntaxe, la structure du code et la visualisation des données.



---

## 🧠 Compétences acquises

### Maîtrise de l'outil R
* Approfondissement des connaissances en syntaxe et structure du langage.
* Utilisation du logiciel pour la visualisation et l'analyse de données réelles.

### Statistiques et Analyse
* Compréhension du fonctionnement de la **régression linéaire** et de son contexte d'utilisation.
* Mise en pratique des concepts de prédiction pour résoudre des problèmes concrets.
* Renforcement des compétences analytiques et développement d'une approche méthodique.

### Communication et Rédaction
* Amélioration des compétences rédactionnelles pour expliquer une démarche technique.
* Capacité à présenter des résultats de manière claire et structurée.

---

> **Bilan :** Ce projet a permis de lier la théorie statistique à la pratique logicielle, tout en développant une capacité à communiquer efficacement sur des résultats analytiques.



# Conception et implémentation d’une base de données

## 📌 Présentation du projet
L'objectif de ce projet était de développer une solution sur mesure pour répondre aux besoins spécifiques d'une **entreprise de menuiserie**. Le système visait à assurer le suivi complet des équipements : pannes, réparations, achats, types de matériel et utilisateurs.

---

## 🛠️ Méthodologie et Réalisation

### 1. Conception et Schématisation
Avant la mise en œuvre technique, une phase de modélisation a été nécessaire :
* **Schéma relationnel :** Élaboration d'une représentation graphique des liens entre les tables pour valider la fonctionnalité du système.
* **Outil utilisé :** **LoopingMCD**.

### 2. Implémentation technique
* **Base de données :** Création et hébergement de la base via **EasyPhp**.
* **Développement logiciel :** Création d'une interface graphique en **Python**.
* **Interaction SQL :** Programmation de requêtes spécifiques pour l'extraction de données (ex: calcul du total des achats de matériel pour l'année 2021).



---

## 🚀 Fonctionnalités de l'interface
L'interface ergonomique et interactive permet aux utilisateurs de :
* **Visualiser** le contenu des différentes tables de la base.
* **Ajouter** de nouvelles données.
* **Exécuter** des requêtes de synthèse pour la gestion des équipements.

---

## 🧠 Compétences acquises
* **Conception de données :** Capacité à élaborer un schéma relationnel fonctionnel et adapté aux besoins.
* **Maîtrise technologique :** Utilisation combinée de **Python** et **SQL** pour lier l'interface à la base de données.
* **Outils d'hébergement :** Utilisation d'**EasyPhp** pour la mise en ligne de la solution.
* **Analyse des besoins :** Aptitude à interpréter les demandes d'un commanditaire pour concevoir une solution métier sur mesure.
* **Ergonomie :** Création d'une interface utilisateur conviviale et interactive.

---

> **Bilan :** Ce projet a permis de fournir une solution fonctionnelle facilitant la gestion opérationnelle d'une entreprise de menuiserie, tout en renforçant des compétences techniques en programmation et en gestion de données.


# Mise en œuvre d’une enquête

## 📌 Présentation du projet
L'objectif de ce projet était de concevoir un questionnaire pour mener une enquête sur le **logement des étudiants à l'université de Niort**. Ce travail visait à identifier les questions les plus pertinentes pour couvrir l'ensemble du sujet au sein de l'IUT.

---

## 🛠️ Méthodologie et Conception

### 1. Préparation et Logique
Avant la phase de saisie, un travail de réflexion sur la structure a été mené :
* **Élaboration d'un organigramme :** Réalisation d'un schéma pour déterminer l'ordre et la logique des questions.
* **Gestion des branchements :** Prise en compte des différentes réponses possibles pour orienter efficacement les répondants (filtres et sauts de questions).



### 2. Structure du Questionnaire
Le questionnaire a été organisé en trois parties distinctes :
* **Identification du répondant :** Profil et informations générales.
* **Situation de logement :** État actuel de l'habitation de l'étudiant.
* **Opinion :** Avis et ressenti sur les logements étudiants.

### 3. Outil utilisé
* **Sphinx :** Utilisation du logiciel pour créer un questionnaire interactif et convivial.

---

## 🧠 Compétences acquises

* **Maîtrise de l'outil Sphinx :** Exploitation des fonctionnalités du logiciel pour la création d'enquêtes.
* **Conception et Ingénierie de questionnaire :** Capacité à identifier des questions pertinentes et à les structurer de manière logique et cohérente.
* **Compétences rédactionnelles :** Travail sur la formulation claire et concise des questions pour éviter les ambiguïtés et obtenir des réponses précises.
* **Analyse de données et graphiques :** Réflexion basée sur l'exploitation de données existantes pour orienter les thématiques de l'enquête.

---

> **Bilan :** Ce projet a permis de développer une expertise dans la création d'outils de collecte de données, en mettant l'accent sur la rigueur logique et la clarté de la communication avec les répondants.


# Création d’un reporting : Logiciel de suivi de notes personnel

## 📌 Présentation du projet
Ce projet consiste en la conception d'un logiciel réalisé sous **Excel VBA**, destiné à suivre les notes d'un ou plusieurs étudiants tout au long d'une année universitaire au sein d'un programme de formation spécifique.

---

## ⚙️ Fonctionnalités du logiciel
L'application intègre trois fonctionnalités essentielles pour la gestion du parcours académique :

1.  **Gestion des évaluations :** Ajout de notes en fonction du semestre, de la compétence et du cours concerné.
2.  **Édition :** Possibilité de modifier une note existante.
3.  **Tableau de bord décisionnel :** * Calcul et affichage des moyennes pour les trois blocs de compétences de la formation.
    * Indication des compétences acquises par l'étudiant.
    * Affichage automatique du statut d'admission en deuxième année.

---

## 🧠 Compétences acquises

### Maîtrise technique
* **Excel VBA :** Approfondissement des connaissances en programmation pour mettre en œuvre des fonctionnalités dynamiques.
* **Développement applicatif :** Création d'une application interactive complète.
* **Ergonomie :** Compréhension de l'optimisation et de la conception d'interfaces utilisateur fluides.

### Soft Skills et Organisation
* **Travail en groupe :** Amélioration des méthodes d'organisation au sein d'une équipe.
* **Analyse de données :** Conception d'un tableau de bord de suivi de performance académique.

---

> **Bilan :** Ce projet a permis de transformer un besoin de suivi pédagogique en une solution logicielle concrète, tout en renforçant des compétences en automatisation et en ergonomie logicielle.



# Ecriture et lecture de fichiers de données (JSON & CSV)

## 📌 Présentation du projet
Dans le cadre d'un projet de groupe, nous avons développé un programme en **Python** dédié à l'analyse de la concentration des polluants dans l'air ambiant. L'objectif était de manipuler des données sources au format **JSON** pour générer un tableau **CSV** final, trié, filtré et ordonné selon des colonnes spécifiques.

---

## 🛠️ Méthodologie et Traitement des données

### 1. Analyse structurelle
* Étude préalable de la structure des données à l'aide d'un outil de visualisation en ligne pour comprendre l'organisation du fichier JSON.

### 2. Algorithmie et Transformation
Le programme Python a été conçu pour traiter les données ligne par ligne selon des consignes précises :
* **Nettoyage :** Suppression systématique des lignes de données incomplètes.
* **Formatage temporel :** Conversion des dates du format anglais vers le format français.
* **Structuration :** Organisation des données nettoyées et converties avant l'écriture finale.

### 3. Exportation
* Génération d'un fichier CSV structuré respectant l'ordre des colonnes défini par les besoins du projet.

---

## 🧠 Compétences acquises

### Maîtrise technique
* **Gestion de formats :** Manipulation avancée des fichiers JSON et CSV avec Python.
* **Algorithmie :** Compréhension et mise en œuvre des bases des structures algorithmiques.
* **Programmation Python :** Approfondissement des compétences en développement pour le traitement de données.

### Analyse et Méthodologie
* **Analyse de données :** Compréhension de l'importance de connaître la structure des données pour une exploitation optimale.
* **Gestion de projet :** Interprétation des besoins et des demandes d'un commanditaire en respectant des consignes et modalités strictes.

---

> **Bilan :** Ce projet a permis de renforcer la rigueur nécessaire au traitement de données environnementales, de la compréhension de la structure source jusqu'à la production d'un fichier d'analyse propre et exploitable.


# Préparation et synthèse d’un tableau de données en vue d’une analyse exploratoire simple

## 📌 Présentation du projet
Ce projet consistait à rédiger un rapport d'analyse basé sur les résultats d'une enquête menée à l'université de Niort concernant l'**utilisation des téléphones portables** par les étudiants. L'objectif était de mettre en évidence trois aspects spécifiques révélés par l'enquête à l'aide de données chiffrées et de graphiques.

---

## 🛠️ Méthodologie et Analyse
Pour traiter les données collectées, le logiciel **Sphinx** a été utilisé comme outil central de traitement et d'analyse.



### Étapes clés :
* **Sélection des données :** Tri et discernement parmi un volume important de données pour identifier les aspects les plus pertinents à développer.
* **Analyse exploratoire :** Utilisation de Sphinx pour extraire les tendances significatives.
* **Visualisation :** Sélection et création de graphiques informatifs pour étayer les arguments du rapport.
* **Rédaction :** Synthèse cohérente des résultats pour produire un document professionnel.

---

## 🧠 Compétences acquises

### Analyse et Logiciel
* **Maîtrise de Sphinx :** Utilisation efficace du logiciel pour analyser les données d'une enquête.
* **Synthèse de données :** Capacité à sélectionner avec soin les données les plus utiles pour illustrer un argument de manière convaincante.
* **Datavisualisation :** Création de graphiques appropriés et significatifs.

### Communication Professionnelle
* **Rédaction technique :** Amélioration des capacités rédactionnelles pour produire un contenu clair, concis et cohérent.
* **Structure de rapport :** Maîtrise des conventions de mise en forme et de la structure des documents professionnels.

---

> **Bilan :** Cette expérience a permis de perfectionner ma capacité à transformer un volume important de données d'enquête en un rapport de synthèse professionnel, tout en renforçant ma maîtrise des outils de traitement d'enquêtes.


# Apprendre en situation la production de données en entreprise

## 📌 Présentation du projet
L'objectif de ce projet était de rédiger un rapport statistique complet visant à évaluer la situation de l'**emploi**, de la **population** et du **chômage** dans le département de la **Seine-Saint-Denis**. Ce travail a permis de construire des indicateurs précis reflétant la réalité socio-économique du territoire.

---

## 🛠️ Méthodologie et Outils
Le projet a été structuré autour de l'utilisation de données officielles et d'outils de bureautique classiques :

* **Collecte de données :** Recherche de données pertinentes sur le site de l'**INSEE**.
* **Traitement et calculs :** Utilisation d'**Excel** pour le calcul des indicateurs socio-économiques.
* **Rédaction et mise en forme :** Utilisation de **Word** pour la production d'un rapport professionnel structuré.



---

## 🧠 Compétences acquises

### Maîtrise des logiciels de bureautique
* Manipulation efficace des données sous **Excel**.
* Utilisation avancée de **Word** pour la rédaction et la présentation professionnelle des résultats.

### Analyse et Recherche de données
* Capacité à rechercher des données fiables et pertinentes (INSEE).
* Aptitude à effectuer des calculs d'indicateurs pour évaluer une situation territoriale spécifique.
* Approfondissement de la compréhension de la situation socio-économique d'un département.

### Rédaction et Communication
* Amélioration des compétences rédactionnelles pour produire un contenu clair, précis et bien structuré.
* Maîtrise des principes de mise en forme d'un rapport professionnel.

---

> **Bilan :** Ce projet a permis de développer une maîtrise opérationnelle de la production de données statistiques, de la phase de recherche jusqu'à la présentation finale sous forme de rapport professionnel, tout en offrant une lecture fine de la réalité de la Seine-Saint-Denis.



# Présentation en anglais d’un territoire économique et culturel

## 📌 Présentation du projet
L'objectif de ce projet était de présenter une commune sous deux angles : un volet **économique** et un volet **culturel**. La commune de **Dijon** a été choisie pour cette étude. Une particularité de cet exposé était que la première partie de la présentation devait être réalisée en **anglais**.

---

## 🛠️ Méthodologie et Recherche
Pour construire ce projet, nous avons utilisé des sources numériques et des outils de présentation professionnelle :

* **Collecte d'informations :** Utilisation d'Internet pour consulter le site officiel de la commune de **Dijon** (patrimoine et entreprises) ainsi que le site de l'**INSEE** pour les indicateurs économiques et démographiques.
* **Conception du support :** Utilisation de **PowerPoint** en respectant les normes universitaires pour créer un diaporama visuellement attrayant et professionnel.
* **Volet linguistique :** Rédaction et présentation en anglais en s'appuyant sur nos connaissances, l'aide du professeur d'anglais et des outils de traduction en ligne.



---

## 🧠 Compétences acquises

### Maîtrise de l'outil PowerPoint
* Création de présentations attractives, professionnelles et captivantes.
* Optimisation du support visuel pour accompagner une présentation orale.

### Recherche et Analyse
* Capacité à mener des recherches efficaces sur Internet.
* Sélection d'informations pertinentes auprès de sources fiables (sites officiels et INSEE).

### Compétences en Anglais
* Amélioration de la maîtrise de la langue, tant sur le plan de la rédaction que de la présentation orale.
* Apprentissage en situation de communication internationale.

---

> **Bilan :** Ce projet a permis de développer des compétences combinées en recherche documentaire, en conception visuelle sous PowerPoint et en communication en langue anglaise, le tout appliqué à l'analyse d'un territoire.