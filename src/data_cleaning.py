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
import geopandas as gpd

premier_tour = pd.read_parquet('data/raw/resultats-elections-municipales-2026-1er-tour.parquet')
deuxieme_tour = pd.read_parquet('data/raw/resultats-elections-municipales-2026-2nd-tour.parquet')
europeennes = pd.read_parquet('data/raw/euro-2024-1t-resultats.parquet')
lieux_de_vote = gpd.read_file("data/raw/election-2026-lieux-de-vote.geojson")

columns_premier_tour = ['N', 'Municipales', 'Annee', 'Tour', 'Departement', 'Code_Insee', 'bureau', 'Indicatif', 'inscrits', 'abstentions', 'votants', 'votants_ap_emargement', 'blancs', 'nuls', 'exprimes', 
                        'nb_listes', '01', 'Briançon_Voix', '02', 'Scalli_Voix', '03', 'Adrada_Voix', '04', 'Menendez_Voix', '05', 'Moudenc_Voix', '06', 'Leonardelli_Voix', '07', 'Cottrel_Voix', '08', 
                        'Meilhac_Voix', '09', 'Piquemal_Voix', '10', 'Pedinotti_Voix']

columns_deuxieme_tour = ['N', 'Municipales', 'Annee', 'Tour', 'Departement', 'Code_Insee', 'bureau', 'Indicatif', 'inscrits', 'abstentions', 'votants', 'votants_ap_emargement', 'blancs', 'nuls', 'exprimes', 
                         'nb_listes', '01', 'Moudenc_Voix', '02', 'Piquemal_Voix']

columns_europeennes = ['Séquence', 'Type', 'Année', 'Tour', 'Département', 'Ville', 'bureau', 'Canton', 'Circonscription', 'Indicatif', 'inscrits', 'abstentions', 'Votants', 'Nombre de votants émargement', 'blancs', 'nuls', 
                       'exprimes', 'Nombre de candidats', 'Dépôt de liste 1', 'Léopold_Edouard_Deher_Lesaint_Voix', 'Dépôt de liste 2', 'Philippe_Ponge_Voix', 'Dépôt de liste 3', 'Marion_Maréchal_Voix', 
                       'Dépôt de liste 4', 'Manon_Aubry_Voix', 'Dépôt de liste 5', 'Jordan_Bardella_Voix', 'Dépôt de liste 6', 'Marie_Toussaint_Voix', 'Dépôt de liste 7', 'Nagib_Azergui_Voix', 'Dépôt de liste 8', 
                       'Hélène_Thouy_Voix', 'Dépôt de liste 9', 'Olivier_Terrien_Voix', 'Dépôt de liste 10', 'Caroline_Zorn_Voix', 'Dépôt de liste 11', 'Valérie_Hayer_Voix', 'Dépôt de liste 12', 'Audric_Alexandre_Voix', 
                       'Dépôt de liste 13', 'Marine_Cholley_Voix', 'Dépôt de liste 14', 'Yann_Wehrling_Voix', 'Dépôt de liste 15', 'François_Asselineau_Voix', 'Dépôt de liste 16', 'Michel_Simonin_Voix', 'Dépôt de liste 17', 
                       'Jean_Marc_Fortané_Voix', 'Dépôt de liste 18', 'François_Xavier_Bellamy_Voix', 'Dépôt de liste 19', 'Nathalie_Arthaud_Voix', 'Dépôt de liste 20', 'Pierre_Larrouturou_Voix', 'Dépôt de liste 21', 'Georges_Kuzmanovic_Voix', 'Dépôt de liste 22', 'Selma_Labib_Voix', 
                       'Dépôt de liste 23', 'Camille_Adou_Voix', 'Dépôt de liste 24', 'Florian_Philippot_Voix', 'Dépôt de liste 25', 'Édouard_Husson_Voix', 'Dépôt de liste 26', 'Pierre_Marie_Bonneau_Voix', 'Dépôt de liste 27', 'Raphaël_Glucksmann_Voix', 'Dépôt de liste 28', 
                       'Charles_Hoareau_Voix', 'Dépôt de liste 29', 'Jean_Lassalle_Voix', 'Dépôt de liste 30', 'Francis_Lalanne_Voix', 'Dépôt de liste 31', 'Guillaume_Lacroix_Voix', 'Dépôt de liste 32', 'Lorys_Elmayan_Voix', 'Dépôt de liste 33', 'Léon_Deffontaines_Voix', 
                       'Dépôt de liste 34', 'Gaël_Coste_Meunier_Voix', 'Dépôt de liste 35', 'Jean_Marc_Governatori_Voix', 'Dépôt de liste 36', 'Hadama_Traoré_Voix', 'Dépôt de liste 37', 'Laure_Patas_d_Illiers_Voix', 'Dépôt de liste 38', 'Patrice_Grudé_Voix']
columns_lieux_de_vote = ['adresse', 'Geo_Point', 'Geo_Shape', 'gml_id', 'infobulle', 'oid', 'bureau', 'Nom']

premier_tour.columns = columns_premier_tour
deuxieme_tour.columns = columns_deuxieme_tour
europeennes.columns = columns_europeennes
lieux_de_vote.columns = columns_lieux_de_vote

print(lieux_de_vote.head(2))

premier_tour_filtered = premier_tour.drop(columns=['N', 'Tour', 'Municipales', 'Annee', 'Departement', 'Code_Insee', 'votants_ap_emargement', 'nb_listes', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 'Indicatif'])
deuxieme_tour_filtered = deuxieme_tour.drop(columns=['N', 'Municipales', 'Annee', 'Departement', 'Code_Insee', 'nb_listes', '01', '02', 'Indicatif'])
europeennes_filtered = europeennes.drop(columns=['Séquence', 'Type', 'Année', 'Tour', 'Département', 'Ville', 'Canton', 'Circonscription', 'Nombre de candidats', 'Indicatif', 'Nombre de votants émargement', 'Dépôt de liste 1', 
                                                 'Dépôt de liste 2', 'Dépôt de liste 3', 'Dépôt de liste 4', 'Dépôt de liste 5', 'Dépôt de liste 6', 'Dépôt de liste 7', 'Dépôt de liste 8', 
                                                 'Dépôt de liste 9', 'Dépôt de liste 10', 'Dépôt de liste 11', 'Dépôt de liste 12', 'Dépôt de liste 13', 'Dépôt de liste 14', 'Dépôt de liste 15', 
                                                 'Dépôt de liste 16', 'Dépôt de liste 17', 'Dépôt de liste 18', 'Dépôt de liste 19', 'Dépôt de liste 20', 'Dépôt de liste 21', 'Dépôt de liste 22', 
                                                 'Dépôt de liste 23', 'Dépôt de liste 24', 'Dépôt de liste 25', 'Dépôt de liste 26', 'Dépôt de liste 27', 'Dépôt de liste 28', 'Dépôt de liste 29', 
                                                 'Dépôt de liste 30', 'Dépôt de liste 31', 'Dépôt de liste 32', 'Dépôt de liste 33', 'Dépôt de liste 34', 'Dépôt de liste 35', 'Dépôt de liste 36', 
                                                 'Dépôt de liste 37', 'Dépôt de liste 38'])

premier_tour_filtered = premier_tour_filtered.add_suffix('_premier_tour')
deuxieme_tour_filtered = deuxieme_tour_filtered.add_suffix('_second_tour')
europeennes_filtered = europeennes_filtered.add_suffix('_europeennes')

print(premier_tour_filtered.info())

lieux_de_vote['bureau'] = lieux_de_vote['bureau'].astype(str)
lieux_de_vote['bureau'] = lieux_de_vote['bureau'].str.zfill(4)

final_data = pd.merge(premier_tour_filtered, deuxieme_tour_filtered, left_on = 'bureau_premier_tour', right_on='bureau_second_tour', how='outer')
final_data = pd.merge(final_data, europeennes_filtered, left_on = 'bureau_premier_tour', right_on='bureau_europeennes', how='outer')

final_data.to_parquet('data/processed/final_data.parquet')

final_data['scores_gauche_Voix_premier_tour'] = final_data['Briançon_Voix_premier_tour'] + final_data['Piquemal_Voix_premier_tour'] + final_data['Pedinotti_Voix_premier_tour'] + final_data['Menendez_Voix_premier_tour'] + final_data['Adrada_Voix_premier_tour'] + final_data['Scalli_Voix_premier_tour']

final_data['scores_union_Voix_premier_tour'] = final_data['Briançon_Voix_premier_tour'] + final_data['Piquemal_Voix_premier_tour'] 

final_data['scores_droite_Voix_premier_tour'] = final_data['Moudenc_Voix_premier_tour'] + final_data['Cottrel_Voix_premier_tour'] + final_data['Leonardelli_Voix_premier_tour'] 

final_data['blc_nuls_Voix_premier_tour'] = final_data['blancs_premier_tour'] + final_data['nuls_premier_tour']

final_data['blc_nuls_Voix_second_tour'] = final_data['blancs_second_tour'] + final_data['nuls_second_tour']

final_data['blc_nuls_europeennes_Voix'] = final_data['blancs_europeennes'] + final_data['nuls_europeennes']

final_data = final_data.drop(columns=['blancs_premier_tour', 'nuls_premier_tour', 'blancs_second_tour', 'nuls_second_tour', 'blancs_europeennes', 'nuls_europeennes'])

final_data['Delta_Abstention'] = final_data['abstentions_second_tour'] - final_data['abstentions_premier_tour']

final_data['Delta_Gauche_municipales'] = final_data['Piquemal_Voix_second_tour'] - (final_data['Briançon_Voix_premier_tour'] + final_data['Piquemal_Voix_premier_tour'])

final_data['Delta_blc_nuls'] = final_data['blc_nuls_Voix_second_tour'] - final_data['blc_nuls_Voix_premier_tour']

final_data['Delta_vote_droite'] = final_data['Moudenc_Voix_second_tour'] - final_data['Moudenc_Voix_premier_tour']

final_data['report_moudenc'] = final_data['Moudenc_Voix_premier_tour'] + final_data['Cottrel_Voix_premier_tour'] + final_data['Leonardelli_Voix_premier_tour'] 

final_data['vivre_mieux_europeennes'] = final_data['Marie_Toussaint_Voix_europeennes'] + final_data['Raphaël_Glucksmann_Voix_europeennes']

final_data['union_gauche_europeennes'] = final_data['Manon_Aubry_Voix_europeennes'] + final_data['vivre_mieux_europeennes']

final_data['delta_europeennes_municipales_Vivre_Mieux'] = final_data['Briançon_Voix_premier_tour'] - final_data['vivre_mieux_europeennes']

final_data['ratio_europeennes_municipales_Vivre_Mieux'] = final_data['Briançon_Voix_premier_tour'] / final_data['vivre_mieux_europeennes']

final_data['prediction_voix_LE_municipales_premier_tour'] = final_data['Marie_Toussaint_Voix_europeennes'] * final_data['ratio_europeennes_municipales_Vivre_Mieux']

final_data['force_relative_des_partis'] = final_data['Marie_Toussaint_Voix_europeennes'] / (final_data['Marie_Toussaint_Voix_europeennes'] + final_data['Raphaël_Glucksmann_Voix_europeennes'])

final_data['force_relative_des_partis_LE_PS_LFI'] = final_data['Marie_Toussaint_Voix_europeennes'] / (final_data['Marie_Toussaint_Voix_europeennes'] + final_data['Raphaël_Glucksmann_Voix_europeennes'] + final_data['Manon_Aubry_Voix_europeennes'])

final_data['force_relative_des_partis_PS_LE_LFI'] = final_data['Raphaël_Glucksmann_Voix_europeennes'] / (final_data['Marie_Toussaint_Voix_europeennes'] + final_data['Raphaël_Glucksmann_Voix_europeennes'] + final_data['Manon_Aubry_Voix_europeennes'])

final_data['force_relative_des_partis_LFI_LE_PS'] = final_data['Manon_Aubry_Voix_europeennes'] / (final_data['Marie_Toussaint_Voix_europeennes'] + final_data['Raphaël_Glucksmann_Voix_europeennes'] + final_data['Manon_Aubry_Voix_europeennes'])

final_data['Depertition'] = final_data['Piquemal_Voix_second_tour'] / (final_data['Piquemal_Voix_premier_tour'] + final_data['Briançon_Voix_premier_tour'])

final_data['report_vivre_mieux_a_moudenc'] = final_data['Moudenc_Voix_second_tour'] - (final_data['report_moudenc'] - final_data['Delta_Abstention'])

final_data['report_vivre_mieux_a_moudenc'] = final_data['report_vivre_mieux_a_moudenc'].apply(lambda x: x if x>0 else 0)

final_data['report_vivre_mieux_a_moudenc_%'] = 100 * final_data['report_vivre_mieux_a_moudenc'] / (final_data['report_vivre_mieux_a_moudenc'] - final_data['Delta_Abstention'])

final_data['report_vivre_mieux_a_moudenc_%'] = final_data['report_vivre_mieux_a_moudenc_%'].apply(lambda x: x if x>0 else 50)

final_data['gain_moudenc_participation_%'] = - 100 * final_data['Delta_Abstention'] / (final_data['report_vivre_mieux_a_moudenc'] - final_data['Delta_Abstention'])

final_data['gain_moudenc_participation_%'] = final_data['gain_moudenc_participation_%'].apply(lambda x: x if x<100 else 50)

colonnes_pourcentages_premier = ['blc_nuls_Voix_premier_tour', 'Briançon_Voix_premier_tour', 'Scalli_Voix_premier_tour', 'Adrada_Voix_premier_tour', 'Menendez_Voix_premier_tour', 
                                 'Moudenc_Voix_premier_tour', 'Leonardelli_Voix_premier_tour', 'Cottrel_Voix_premier_tour', 'Meilhac_Voix_premier_tour', 'Piquemal_Voix_premier_tour', 'Pedinotti_Voix_premier_tour', 'scores_gauche_Voix_premier_tour',
                                 'scores_union_Voix_premier_tour', 'scores_droite_Voix_premier_tour']

colonnes_pourcentages_second = ['blc_nuls_Voix_second_tour', 'Moudenc_Voix_second_tour', 'Piquemal_Voix_second_tour']

colonnes_pourcentages_europeennes = ['blc_nuls_europeennes_Voix', 'exprimes_europeennes', 
                                     'Léopold_Edouard_Deher_Lesaint_Voix_europeennes', 'Philippe_Ponge_Voix_europeennes', 'Marion_Maréchal_Voix_europeennes', 'Manon_Aubry_Voix_europeennes', 
                                     'Jordan_Bardella_Voix_europeennes', 'Marie_Toussaint_Voix_europeennes', 'Nagib_Azergui_Voix_europeennes', 'Hélène_Thouy_Voix_europeennes', 
                                     'Olivier_Terrien_Voix_europeennes', 'Caroline_Zorn_Voix_europeennes', 'Valérie_Hayer_Voix_europeennes', 'Audric_Alexandre_Voix_europeennes', 
                                     'Marine_Cholley_Voix_europeennes', 'Yann_Wehrling_Voix_europeennes',  'François_Asselineau_Voix_europeennes', 'Michel_Simonin_Voix_europeennes',
                                     'Jean_Marc_Fortané_Voix_europeennes', 'François_Xavier_Bellamy_Voix_europeennes', 'Nathalie_Arthaud_Voix_europeennes', 'Pierre_Larrouturou_Voix_europeennes', 
                                     'Georges_Kuzmanovic_Voix_europeennes', 'Selma_Labib_Voix_europeennes', 'Camille_Adou_Voix_europeennes', 'Florian_Philippot_Voix_europeennes', 
                                     'Édouard_Husson_Voix_europeennes',  'Pierre_Marie_Bonneau_Voix_europeennes', 'Raphaël_Glucksmann_Voix_europeennes', 'Charles_Hoareau_Voix_europeennes', 
                                     'Jean_Lassalle_Voix_europeennes', 'Francis_Lalanne_Voix_europeennes', 'Guillaume_Lacroix_Voix_europeennes', 'Lorys_Elmayan_Voix_europeennes', 'Léon_Deffontaines_Voix_europeennes', 
                                     'Gaël_Coste_Meunier_Voix_europeennes',  'Jean_Marc_Governatori_Voix_europeennes', 'Hadama_Traoré_Voix_europeennes', 'Laure_Patas_d_Illiers_Voix_europeennes','Patrice_Grudé_Voix_europeennes', 
                                     'vivre_mieux_europeennes', 'union_gauche_europeennes']

for col in colonnes_pourcentages_premier:
    
    nom_nouvelle_col = col + "_%"
    
    final_data[nom_nouvelle_col] = 100 * final_data[col] / final_data['exprimes_premier_tour']
    
for col in colonnes_pourcentages_second:
    
    nom_nouvelle_col = col + "_%"
    
    final_data[nom_nouvelle_col] = 100 * final_data[col] / final_data['exprimes_second_tour']

    
for col in colonnes_pourcentages_europeennes:
    
    nom_nouvelle_col = col + "_%"
    
    final_data[nom_nouvelle_col] = 100 * final_data[col] / final_data['exprimes_europeennes']

final_data['abstentions_premier_tour_%'] = 100 * final_data['abstentions_premier_tour'] / final_data['inscrits_premier_tour']
final_data['abstentions_second_tour_%'] = 100 * final_data['abstentions_second_tour'] / final_data['inscrits_second_tour']
final_data['abstentions_europeennes_%'] = 100 * final_data['abstentions_europeennes'] / final_data['inscrits_europeennes']

final_data.to_parquet('data/results/data_first_analysis.parquet')
final_data.to_csv('data/results/data_first_analysis.csv')
