"""
Project: Analyses elections municipales 2026 Toulouse
Copyright (C) 2026 Alexis Hucteau

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import pandas as pd
import numpy as np

premier_tour = pd.read_parquet('data/raw/resultats-elections-municipales-2026-1er-tour.parquet')
deuxieme_tour = pd.read_parquet('data/raw/resultats-elections-municipales-2026-2nd-tour.parquet')
lieux_de_vote = pd.read_parquet('data/raw/election-2026-lieux-de-vote.parquet')

columns_premier_tour = ['N', 'Municipales', 'Annee', 'Tour', 'Departement', 'Code_Insee', 'bureau', 'Indicatif', 'inscrits', 'abstentions', 'votants', 'votants_ap_emargement', 'blancs', 'nuls', 'exprimes', 'nb_listes', '01', 'Briançon', '02', 'Scalli', '03', 'Adrada', '04', 'Menendez', '05', 'Moudenc', '06', 'Leonardelli', '07', 'Cottrel', '08', 'Meilhac', '09', 'Piquemal', '10', 'Pedinotti']
columns_deuxieme_tour = ['N', 'Municipales', 'Annee', 'Tour', 'Departement', 'Code_Insee', 'bureau', 'Indicatif', 'inscrits', 'abstentions', 'votants', 'votants_ap_emargement', 'blancs', 'nuls', 'exprimes', 'nb_listes', '01', 'Moudenc', '02', 'Piquemal']
columns_lieux_de_vote = ['adresse', 'Geo_Point', 'Geo_Shape', 'gml_id', 'infobulle', 'oid', 'bureau', 'Nom']

premier_tour.columns = columns_premier_tour
deuxieme_tour.columns = columns_deuxieme_tour
lieux_de_vote.columns = columns_lieux_de_vote

premier_tour_filtered = premier_tour.drop(columns=['N', 'Municipales', 'Annee', 'Departement', 'Code_Insee', 'nb_listes', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'Indicatif'])
deuxieme_tour_filtered = deuxieme_tour.drop(columns=['N', 'Municipales', 'Annee', 'Departement', 'Code_Insee', 'nb_listes', '01', '02', 'Indicatif'])

print(premier_tour_filtered.info())
lieux_de_vote['bureau'] = lieux_de_vote['bureau'].astype(str)
lieux_de_vote['bureau'] = lieux_de_vote['bureau'].str.zfill(4)

premier_tour_filtered_spatial = pd.merge(premier_tour_filtered, lieux_de_vote, on = 'bureau')
deuxieme_tour_filtered_spatial = pd.merge(deuxieme_tour_filtered, lieux_de_vote, on = 'bureau')
print(premier_tour_filtered_spatial.info())

premier_tour_filtered_spatial.to_parquet('data/processed/premier_tour_cleaned.parquet')
deuxieme_tour_filtered_spatial.to_parquet('data/processed/deuxieme_tour_cleaned.parquet')
