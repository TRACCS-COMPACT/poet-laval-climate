# Le climat du Poët-Laval

Atelier pratique (≈ 1 h) : **réaliser une petite étude climatique avec un agent IA, étape par étape.**

## La mission

Vous êtes chercheur·e en climat. La Mairie du Poët-Laval et le Département de la Drôme préparent un plan
d'adaptation au changement climatique, pour le village et pour son agriculture. Ils vous demandent une
**fiche d'une page** sur le climat de la commune et son évolution depuis 1950.

Lisez d'abord leur courrier : [`mission/lettre_de_mission.pdf`](mission/lettre_de_mission.pdf) (scénario fictif).

## Où trouver quoi

| Document | À quoi il sert | À donner à l'agent ? |
|---|---|---|
| La lettre | Le **contexte** : qui demande quoi, et pourquoi | **Non.** Lisez-la vous-même. |
| Ce README | La **méthode** : les niveaux, dans l'ordre | **Oui, un niveau à la fois** |
| [`data/README.md`](data/README.md) | La description des données | Oui, si utile |
| [`GRILLE.md`](GRILLE.md) | Comment la fiche sera jugée | Non |

## Comment travailler avec l'agent

L'agent peut écrire beaucoup de code très vite, et même tout faire d'un coup. Mais alors, vous ne pourrez
rien vérifier. Le but de l'atelier est d'apprendre à **travailler avec** l'agent, et à savoir **quand lui faire confiance**.

Pour chaque niveau :

1. **Lisez** l'objectif du niveau.
2. **Demandez à l'agent cette étape seulement**, avec vos propres mots. Pas la suite.
3. **Lisez** le code et **regardez** le résultat. Demandez à l'agent d'expliquer ce que vous ne comprenez pas.
4. **Répondez** aux questions de vérification. Si un résultat vous surprend, cherchez pourquoi avec l'agent.
5. **Montrez** votre résultat à un·e animateur·rice ou à une autre équipe, puis passez au niveau suivant.

## Les niveaux

| Niveau | Objectif | Temps conseillé |
|---|---|---|
| 0 | Découvrir les données | 10 min |
| 1 | Le climat aujourd'hui | 15 min |
| 2 | Fait-il plus chaud ? | 15 min |
| 3 | Un indicateur pour le village | 15 min |
| 4 | La fiche climat | 5 min |
| ★ | Bonus | s'il reste du temps |

### Niveau 0 : Découvrir les données

Chargez le fichier ERA5 et le fichier de la station de Montélimar. **Pas encore de figure.**

Questions de vérification :
- Quelles variables contient chaque fichier ? Dans quelles **unités** ?
- ERA5 est horaire, la station est journalière. Comment obtenir une valeur **journalière** avec ERA5 ?
  Est-ce la même chose pour la température et pour la pluie ?
- Quelle période couvre chaque fichier ? Toutes les années sont-elles **complètes** ?
- Quel est le cumul annuel moyen de pluie à Montélimar sur 1991–2020 ? Ce chiffre est-il réaliste ?

### Niveau 1 : Le climat aujourd'hui

Faites **une figure** qui montre la température et la pluie de chaque mois (1991–2020), pour la station et pour ERA5.

Questions de vérification :
- Quels sont les mois les plus pluvieux ? Les plus secs ?
- ERA5 et la station ne donnent pas la même température. Pourquoi ?
- Un·e élu·e ou un·e agriculteur·rice comprendrait-il·elle votre figure sans aide ?

### Niveau 2 : Fait-il plus chaud ?

Montrez l'évolution de la température depuis 1950, avec les deux sources de données.

Questions de vérification :
- De combien fait-il plus chaud aujourd'hui qu'en 1961–1990 ? Combien de °C par décennie ?
- Cette tendance est-elle **statistiquement significative** ? Comment le savez-vous ?
- ERA5 et la station sont-elles d'accord ? Sur quoi, et sur quoi pas ?

### Niveau 3 : Un indicateur pour le village

Choisissez **une seule** question de la lettre :
la chaleur en été, le gel de printemps pour les arbres fruitiers, l'eau, la vigne, ou les fortes pluies d'automne.
Trouvez un **indicateur** (un nombre que l'on peut calculer chaque année) et faites une figure.

Questions de vérification :
- Pourquoi cet indicateur ? À quelle question répond-il ?
- Quel **seuil** avez-vous utilisé (par exemple une température limite) ? Pourquoi cette valeur ?
- Que donne votre indicateur avec ERA5 et avec la station ?

### Niveau 4 : La fiche climat

Réalisez une **fiche d'une page** en PDF pour la Mairie : vos **3 figures** et **3 ou 4 phrases** simples,
avec les sources. Tous les outils sont permis ; l'agent peut vous aider à la mise en page.
Voir [`GRILLE.md`](GRILLE.md).

### ★ Bonus

- **Fortes pluies :** ERA5 voit-elle les gros orages d'automne ? Comparez avec la station, jour par jour.
- **Deuxième station :** Puy-Saint-Martin est plus proche du village. Raconte-t-elle la même histoire ?
- **Piste experte :** *fait-il plus ensoleillé qu'avant ? Cela explique-t-il une partie du réchauffement ?*
  Regardez l'insolation et le rayonnement à la station, et les termes du bilan d'énergie dans ERA5.
  Prudence dans vos conclusions.

## À la fin

Gardez votre conversation avec l'agent. Nous en discuterons ensemble :
**où l'agent s'est-il trompé, et comment l'avez-vous découvert ?**

## Les données

Toutes les données sont dans [`data/`](data/). Rien à télécharger. Détails dans [`data/README.md`](data/README.md).

| Fichier | Contenu |
|---|---|
| `era5_poet_laval_hourly.nc` | Réanalyse ERA5, horaire, 1950–2025, point de grille le plus proche du village |
| `station_montelimar_daily.csv` | Station Météo-France de Montélimar, journalière, de 1950 à aujourd'hui |
| `station_puy-saint-martin_daily.csv` | Station Météo-France de Puy-Saint-Martin, journalière, de 1969 à aujourd'hui |
| `meteofrance_fields_*.txt` | Description des colonnes des fichiers de station |

## Installation (à faire **avant** l'atelier)

```bash
git clone <ce dépôt>
cd poet-laval-climate
conda env create -f environment.yml     # ou : mamba / micromamba
conda activate poet-laval
python check_setup.py
```

Vous pouvez ajouter d'autres paquets Python si besoin.
