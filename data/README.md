# Données

## Réanalyse ERA5 : `era5_poet_laval_hourly.nc`

- **Quoi :** ERA5, la réanalyse mondiale du Centre européen pour les prévisions météorologiques à moyen terme (CEPMMT / ECMWF).
  Une réanalyse combine un modèle météorologique et des millions d'observations pour reconstruire le temps passé partout sur la Terre.
- **Où :** le point de grille ERA5 le plus proche du Poët-Laval (44,5° N, 5,0° E). Une maille fait environ 25 à 30 km de côté.
- **Quand :** horaire, du 1er janvier 1950 au 31 décembre 2025. Les heures sont en UTC.
- **Variables :** température, point de rosée, précipitations, nuages, vent, pression, rayonnement et flux d'énergie en surface.
  Les unités et les noms complets sont dans le fichier (ouvrez-le avec `xarray` et regardez les attributs).
- **Source :** Copernicus Climate Change Service (C3S), Climate Data Store,
  jeu de données [`reanalysis-era5-single-levels-timeseries`](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-timeseries).
- **Licence :** CC-BY 4.0.
- **Référence :** Hersbach, H. et al. (2020) : The ERA5 global reanalysis. *Q. J. R. Meteorol. Soc.*, 146, 1999–2049. doi:10.1002/qj.3803

## Stations Météo-France : `station_*_daily.csv`

| Station | Numéro | Distance au village | Altitude | Période |
|---|---|---|---|---|
| Montélimar | 26198001 | 23 km à l'ouest | 73 m | 1950 – aujourd'hui |
| Puy-Saint-Martin | 26258001 | 10 km au nord | 211 m | 1969 – aujourd'hui |

- **Quoi :** observations journalières de stations Météo-France, avec les noms de colonnes d'origine.
- **Colonnes :** décrites dans `meteofrance_fields_RR-T-Vent.txt` et `meteofrance_fields_autres-parametres.txt`.
  Chaque valeur a un code qualité dans la colonne qui commence par `Q` (par exemple `QRR` pour `RR`).
- **Source :** Météo-France, *Données climatologiques de base – quotidiennes*,
  [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/donnees-climatologiques-de-base-quotidiennes/).
- **Licence :** Licence Ouverte / Open Licence 2.0 (Etalab).
