# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

def main():
    update = input('Do you want to update data? Default n. y/n: ')
    if update is 'y':
        download_and_save()
        save_fulldata()

    train_and_save_model()

def get_compiled_model():
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                        metrics=['accuracy']
                    )
        return model

def train_and_save_model():
    full_df = pd.read_csv('./data/full_data.csv')

    # Splitting dataframe to train and test data
    train, test = train_test_split(full_df, test_size = 0.1)

    target = train.pop('winner')
    dataset = tf.data.Dataset.from_tensor_slices((train.values, target.values))

    test_target = test.pop('winner')
    dataset_2 = tf.data.Dataset.from_tensor_slices((test.values, test_target.values))

    for feat, targ in dataset.take(5):
        print ('Features: {}, Target: {}'.format(feat, targ))

    train_dataset = dataset.shuffle(len(train)).batch(50)
    test_dataset = dataset_2.shuffle(len(test)).batch(5)

    # Training the model
    model = get_compiled_model()
    model.fit(train_dataset, epochs=5)

    test_loss, test_accuracy = model.evaluate(test_dataset)

    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

    # Pick players to test
    VALUES = []
    for i in range(len(full_df.columns)):
        VALUES.append(0)

    VALUES = np.array(VALUES)

    picked_df = pd.DataFrame(columns=full_df.columns)
    picked_df.loc[0] = VALUES
    print(picked_df)

    #pd.to_numeric(picked_df)

    p1 = str(input('Name Player 1: '))
    p2 = str(input('Name Player 2: '))
    surface = str(input('Name surface: '))
    picked_df[p1].loc[0] = 1
    picked_df[p2].loc[0] = 1
    picked_df['surface_' + surface].loc[0] = 1

    print(picked_df)

    for i in picked_df.columns:
        picked_df[i] = pd.to_numeric(picked_df[i], downcast = 'integer')


    pick_target = picked_df.pop('winner')
    picked_dataset = tf.data.Dataset.from_tensor_slices((picked_df.values, pick_target.values))

    picked_dataset = picked_dataset.shuffle(len(picked_df)).batch(1)

    predictions = model.predict(picked_dataset)

    #Show results
    print(p1, 'Win chance against', p2, 'on', surface, 'court: {:.2%}'.format(predictions[0][0]))

def download_and_save():
    all_games_path = 'https://query.data.world/s/hwr7vh7cfuhbbr3xmddeyc4di2jk5r' # Url for games data

    all_players_path = 'https://query.data.world/s/ywfgaydmlp4lha4dlitbpf3f3npppd' # Url for players data

    games_df = pd.read_csv(all_games_path, dtype = {'wrank': object, 'lrank': object, 'w2': object, 'l2': object, 'w3': object, 'l3': object})
    players_df = pd.read_csv(all_players_path)


    # Changing all names to be correct between dataframes because there is no consistency in the data.
    # Removing . from names
    games_df['winner'] = games_df['winner'].str.replace('.', '')
    games_df['loser'] = games_df['loser'].str.replace('.', '')
    #Changing double space to single space
    players_df['full_name'] = players_df['full_name'].str.replace('  ', ' ')
    # Removing whitespace
    games_df['winner'] = games_df['winner'].str.strip()
    games_df['loser'] = games_df['loser'].str.strip()
    # Changing NaN to 0
    games_df.fillna(0, inplace=True)
    players_df.fillna(0, inplace=True)

    # Changing values in games_df
    games_df.replace(
        # Old values
        to_replace=['Lisnard J', 'Lopez-Moron A', 'Alvarez E', 'di Pasquale A', 'Viloca JA', 'Burrieza O', 'van Scheppingen D', 'Arnold L', 'Yoon Y', 'Bogomolov JrA', 'de Chaunac S', 'Wang Y', 'Al Khulaifi NG', 'Nadal-Parera R', 'Vassallo-Arguello M', 'Kunitcin I', 'Van Lottum J' ,'Hantschek M', 'Bogomolov Jr A', 'Gambill J M', 'Gallardo Valles M', 'Mathieu P', 'Schuttler P', 'de Voest R', 'Ramirez-Hidalgo R', 'Bogomolov A', 'di Mauro A', 'Scherrer J', 'Chela J', 'Ferrero J', 'Hippensteel K', 'Al Ghareeb M', 'Matos-Gil I', 'Qureshi A', 'Navarro-Pastor I', 'van der Meer N', 'van Gemerden M', 'Lu Y', 'Gimeno D', 'Gruber K', 'Wang Y Jr', 'Sanchez de Luna JA', 'Sultan-Khalfan A', 'Del Potro JM', 'Querry S', 'Van der Dium A', 'Granollers-Pujol M', 'Salva B', 'Luque D', 'Vicente M', 'De Bakker T', 'Haider-Mauer A', 'Dev Varman S', 'Wang YJr', 'Fish A', 'Robredo R', 'Jun W', 'Fornell M', 'Stepanek M', 'Guzman J', 'Guccione A', 'Ruevski P', 'Gard C', 'Matsukevitch D', 'Chekov P', 'Haji A', 'Podlipnik H', 'Al-Ghareeb M', 'Lopez-Jaen MA', 'Trujillo G', 'Sanchez De Luna J', 'Del Potro J', 'Estrella V', 'De Heart R', 'Silva D', 'Munoz de La Nava D', 'Riba-Madrid P', 'Munoz-De La Nava D', 'Del Bonis F', 'Bautista R', 'Van Der Merwe I', 'Saavedra Corvalan C', 'Deheart R', 'Kuznetsov Al', 'Awadhy O', 'Granollers Pujol G', 'Kuznetsov An', 'Ramos A', 'Carreno-Busta P' ,'Granollers-Pujol G', 'Dutra Da Silva R', 'Al Mutawa J', 'Viola Mat', 'Van D Merwe I', 'Mcclune M', 'Deen Heshaam A', 'Stebe C-M', 'Ali Mutawa JM', 'Zayed M S', 'Mcdonald M', 'Nedovyesov O', 'Struff J-L', 'Mcgee J', 'Herbert P-H', 'Prashanth V', 'Silva F', 'Zhang Ze', 'Zhang Zh', 'Zayid M S', 'Munoz De La Nava D', 'De Minaur A', 'Silva FF', 'Del Potro J M', 'Aragone JC', 'Monteiro J', 'Mukund S', 'Meligeni Rodrigues F', ' '],
        # New Values
        value=['Lisnard JR', 'Lopez Moron A', 'Perez-Alvarez E', 'Di Pasquale A', 'Viloca-Puig JA', 'Burrieza-Lopez O', 'Van Scheppingen D', 'Arnold Ker L', 'Yoon YI', 'Bogomolov Jr. A', 'De Chaunac S', 'Wang YJ', 'Al-Khulaifi NG', 'Nadal R', 'Vassallo Arguello M', 'Kunitsyn I' ,'van Lottum J', 'Hantschk M', 'Bogomolov Jr. A', 'Gambill JM', 'Gallardo-Valles M', 'Mathieu PH', 'Schuettler P', 'De Voest R', 'Ramirez Hidalgo R', 'Bogomolov Jr. A', 'Di Mauro A', 'Scherrer JC', 'Chela JI', 'Ferrero JC', 'Hippensteel KJ', 'Ghareeb M', 'Matos Gil I' ,'Qureshi AUH', 'Navarro I', 'Van Der Meer N', 'Van Gemerden M', 'Lu YH', 'Gimeno-Traver D', 'Gruber KD', 'Wang YJ', 'Sanchez-de Luna JA', 'Khalfan S', 'del Potro JM', 'Querrey S', 'Van Der Duim A', 'Granollers M', 'Salva-Vidal B', 'Luque-Velasco D', 'Vicente F', 'de Bakker T', 'Haider-Maurer A', 'Devvarman S', 'Wang YJ', 'Fish M', 'Robredo T', 'Jun WS', 'Fornell-Mestres M', 'Stepanek R', 'Guzman JP', 'Guccione C', 'Rusevski P', 'Gard CI', 'Matsukevich D', 'Chekhov P', 'Hajji A', 'Podlipnik-Castillo H', 'Ghareeb M', 'Lopez Jaen MA' ,'Trujillo-Soler G', 'Sanchez-de Luna JA', 'del Potro JM', 'Estrella Burgos V', 'DeHeart R', 'Dutra da Silva D', 'Munoz de la Nava D', 'Riba P', 'Munoz de la Nava D', 'Delbonis F', 'Bautista Agut R', 'Van der Merwe I', 'Saavedra-Corvalan C', 'DeHeart R', 'Kuznetsov A' ,'Alawadhi O', 'Granollers G', 'Kuznetsov A', 'Ramos-Vinolas A', 'Carreno Busta P', 'Granollers G', 'Dutra Silva R', 'Al-Mutawa J', 'Viola M', 'Van der Merwe I', 'McClune M', 'Deen Heshaam AE', 'Stebe CM', 'Al-Mutawa J', 'Zayed MS', 'McDonald M', 'Nedovyesov A', 'Struff JL', 'McGee J', 'Herbert PH', 'Prashanth NVS', 'Cunha-Silva F', 'Zhang Z', 'Zhang Z', 'Zayid MS', 'Munoz de la Nava D', 'de Minaur A', 'Ferreira Silva F', 'del Potro JM', 'Aragone J', 'Monteiro T', 'Mukund SK', 'Meligeni F', 0],

        inplace=True)

    print(games_df)
    games_df.to_csv('./data/game_data.csv', index=False)
    players_df.to_csv('./data/player_data.csv', index=False)

def save_fulldata():

    games_df = pd.read_csv('./data/game_data.csv')
    players_df = pd.read_csv('./data/player_data.csv')

    # Making final dataframe column names from players_df
    all_columns = list(players_df['full_name'])

    # Adding rest of columns needed for predictions
    # Includes players who aren't in players_df
    # Mostly new players or players with low amount of games
    all_columns.extend(['Al-Alawi SK', 'Bahrouzyan O', 'Marin L', 'Srichaphan N', 'Schuettler P', 'Prpic A', 'Youzhny A', 'Ascione A', 'Kucera V', 'Ancic I', 'Verdasco M', 'Rascon T', 'March O', 'Wang YT', 'Kutac R', 'Nader M', 'Statham J', 'Dolgopolov O', 'Yuksel A', 'Berrettini M', 'Altmaier D', 'Bonzi B', 'Muller A', 'Harris L', 'Majchrzak K', 'Molleker R', 'Leshem E', 'Koepfer D', 'Aragone J', 'Kypson P', 'Wu Y', 'Safiullin R', 'Ojeda Lara R', 'Caruana L', 'Popyrin A', 'Donski A', 'Korda S', 'Gaston H', 'Seyboth Wild T', 'Kecmanovic M', 'Hurkacz H', 'Piros Z', 'Baldi F', 'Coria F', 'Benchetrit E', 'Otte O', 'Kolar Z', 'Reinberg E', 'Huesler MA', 'Rodionov J', 'Gojo B', 'Humbert U', 'Brooksby J', 'Tseng CH', 'Hoang A', 'Cerundolo F', 'Nava E', 'Davidovich Fokina A', 'Sinner J', 'Valkusz M', 'Basso A', 'Kirkin E', 'Jubb P', 'Gray A', 'Gromley C', 'Moroni G', 'Torpegaard M', 'Lee DH', 'Svajda Z', 'Roumane R', 'Dubrivnyy A', 'Avidzba A', 'Kachmazov A', 'Tabilo A', 'Ficovich JP', 'Ruusuvuori E', 'Diaz Acosta F', 'Shi B', 'Nakashima B', 'Mayot H', 'Alcaraz C', 'Musetti L', 'Barrios Vera MT', 'Varillas JP',
    'p1_weight_kg', 'p2_weight_kg', 'p1_height_cm', 'p2_height_cm', 'p1_handedness', 'p2_handedness', 'p1_backhand', 'p2_backhand', 'p1_game1', 'p2_game1', 'p1_game2', 'p2_game2', 'p1_game3', 'p2_game3', 'p1_game4', 'p2_game4', 'p1_game5', 'p2_game5', 'p1_sets', 'p2_sets', 'winner'])

    # Combining people with same name as 1 person since we can't differentiate them easily
    # Example 'Bell A' and 'Bell A'
    # We would need a better database if we would want to get rid of this problem
    all_columns = np.unique(all_columns)

    # Making all cell values 0 for a row
    BASE_VALUES = []
    for i in range(len(all_columns)):
        BASE_VALUES.append(0)

    BASE_VALUES = np.array(BASE_VALUES)
    LISTED_VALUES = []
    
    # Adding rows to final df for each game
    for i in range(games_df.shape[0]):
        LISTED_VALUES.append(BASE_VALUES)

    LISTED_VALUES = np.array(LISTED_VALUES)

    # Making the dataframe and filling it with value 0 in all
    full_df = pd.DataFrame(LISTED_VALUES, columns = all_columns)
    

    # Adding players for games
    for i, winner, loser in zip(range(games_df.shape[0]), games_df['winner'], games_df['loser']):
        full_df[winner].loc[i] = 1
        full_df[loser].loc[i] = 1

        # Making player 1 be player who comes aplhabetically first and player 2 is the alphabetically second
        # Player 1 will be 1 on winner column and player 2 is 0
        if winner < loser:
            full_df['winner'].loc[i] = 1

            # Game points
            full_df['p1_game1'].loc[i] = games_df['w1'].loc[i]
            full_df['p2_game1'].loc[i] = games_df['l1'].loc[i]
            full_df['p1_game2'].loc[i] = games_df['w2'].loc[i]
            full_df['p2_game2'].loc[i] = games_df['l2'].loc[i]
            full_df['p1_game3'].loc[i] = games_df['w3'].loc[i]
            full_df['p2_game3'].loc[i] = games_df['l3'].loc[i]
            full_df['p1_game4'].loc[i] = games_df['w4'].loc[i]
            full_df['p2_game4'].loc[i] = games_df['l4'].loc[i]
            full_df['p1_game5'].loc[i] = games_df['w5'].loc[i]
            full_df['p2_game5'].loc[i] = games_df['l5'].loc[i]

            # Won sets
            full_df['p1_sets'].loc[i] = int(games_df['wsets'].loc[i])
            full_df['p2_sets'].loc[i] = int(games_df['lsets'].loc[i])

            # Adding player data to full_df from players_df

            # Player 1
            if winner in list(players_df['full_name']):
                full_df['p1_weight_kg'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'weight_kg'].iloc[0]
                full_df['p1_height_cm'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'height_cm'].iloc[0]
                full_df['p1_handedness'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'handedness'].iloc[0]
                full_df['p1_backhand'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'backhand'].iloc[0]
            
            # Player 2
            if loser in list(players_df['full_name']):
                full_df['p2_weight_kg'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'weight_kg'].iloc[0]
                full_df['p2_height_cm'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'height_cm'].iloc[0]
                full_df['p2_handedness'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'handedness'].iloc[0]
                full_df['p2_backhand'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'backhand'].iloc[0]

        else:
            full_df['winner'].loc[i] = 0

            # Game points
            full_df['p1_game1'].loc[i] = games_df['l1'].loc[i]
            full_df['p2_game1'].loc[i] = games_df['w1'].loc[i]
            full_df['p1_game2'].loc[i] = games_df['l2'].loc[i]
            full_df['p2_game2'].loc[i] = games_df['w2'].loc[i]
            full_df['p1_game3'].loc[i] = games_df['l3'].loc[i]
            full_df['p2_game3'].loc[i] = games_df['w3'].loc[i]
            full_df['p1_game4'].loc[i] = games_df['l4'].loc[i]
            full_df['p2_game4'].loc[i] = games_df['w4'].loc[i]
            full_df['p1_game5'].loc[i] = games_df['l5'].loc[i]
            full_df['p2_game5'].loc[i] = games_df['w5'].loc[i]

            # Won sets
            full_df['p2_sets'].loc[i] = int(games_df['wsets'].loc[i])
            full_df['p1_sets'].loc[i] = int(games_df['lsets'].loc[i])

            # Player 1
            if loser in list(players_df['full_name']):
                full_df['p1_weight_kg'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'weight_kg'].iloc[0]
                full_df['p1_height_cm'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'height_cm'].iloc[0]
                full_df['p1_handedness'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'handedness'].iloc[0]
                full_df['p1_backhand'].loc[i] = players_df.loc[players_df['full_name'] == loser, 'backhand'].iloc[0]
            
            # Player 2
            if winner in list(players_df['full_name']):
                full_df['p2_weight_kg'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'weight_kg'].iloc[0]
                full_df['p2_height_cm'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'height_cm'].iloc[0]
                full_df['p2_handedness'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'handedness'].iloc[0]
                full_df['p2_backhand'].loc[i] = players_df.loc[players_df['full_name'] == winner, 'backhand'].iloc[0]

    # Adding surface types for matches
    full_df['surface'] = games_df['surface']
    
    # Converting all text to numbers
    full_df.replace(to_replace=['Right-Handed', 'Left-Handed', 'Ambidextrous', 'One-Handed Backhand', 'Two-Handed Backhand'],
                    value=[1, 2, 3, 1, 2],
                    inplace=True)

    full_df = pd.get_dummies(full_df, columns=['surface'])

    # Changing object dtypes to numeric
    full_df[['p1_game2', 'p1_game3', 'p2_game2', 'p2_game3']] = full_df[['p1_game2', 'p1_game3', 'p2_game2', 'p2_game3']].apply(pd.to_numeric)

    print(full_df)

    full_df.to_csv('./data/full_data.csv', index=False)


if __name__ == "__main__":
    main()