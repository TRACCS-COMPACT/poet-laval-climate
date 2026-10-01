"""Vérifie que l'environnement et les données sont prêts. Lancer : python check_setup.py"""

from pathlib import Path

import matplotlib
import pandas as pd
import xarray as xr

DATA = Path(__file__).parent / "data"

ds = xr.open_dataset(DATA / "era5_poet_laval_hourly.nc")
print(f"Fichier ERA5 OK : {len(ds.data_vars)} variables, {ds.sizes[list(ds.sizes)[0]]} pas de temps")

for name in ["montelimar", "puy-saint-martin"]:
    df = pd.read_csv(DATA / f"station_{name}_daily.csv", sep=";", low_memory=False)
    print(f"Station {name} OK : {len(df)} jours")

print(f"matplotlib {matplotlib.__version__}, xarray {xr.__version__}, pandas {pd.__version__}")
print("Tout est prêt. À bientôt à l'atelier !")
