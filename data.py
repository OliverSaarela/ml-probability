# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

def main():
    all_games_path = 'https://query.data.world/s/hwr7vh7cfuhbbr3xmddeyc4di2jk5r' # Url for games data

    all_players_path = 'https://query.data.world/s/ywfgaydmlp4lha4dlitbpf3f3npppd' # Url for players data

    games_df = pd.read_csv(all_games_path, dtype = {'wrank': object, 'lrank': object, 'w2': object, 'l2': object, 'w3': object, 'l3': object})
    players_df = pd.read_csv(all_players_path)

    # train_df = pd.read_csv(all_games_path) <--- Poista joskus kun on valmista

    #print(games_df.dtypes)
    #print(players_df.dtypes)
    # Making one dataframe with all the data for making predictions
    all_columns = list(players_df['full_name'] + '.')

    all_columns.extend(['Al-Alawi S.K.', 'Bahrouzyan O.', 'Marin L.', 'Srichaphan N.', 'Schuttler P.', 'Prpic A.', 'Youzhny A.', 'Ascione A.', 'Kucera V.', 'Ancic I.', 'Verdasco M.', 'p1_weight_kg','p2_weight_kg', 'p1_height_cm', 'p2_height_cm', 'p1_handedness', 'p2_handedness', 'p1_backhand', 'p2_backhand', 'p1_rank', 'p2_rank', 'p1_game1', 'p2_game1', 'p1_game2', 'p2_game2', 'p1_game3', 'p2_game3', 'p1_game4', 'p2_game4', 'p1_game5', 'p2_game5', 'p1_sets', 'p2_sets', 'winner'])

    all_columns = np.unique(all_columns)


    # Making all rows empty
    BASE_VALUES = []
    for i in range(len(all_columns)):
        BASE_VALUES.append(0)

    BASE_VALUES = np.array(BASE_VALUES)
    LISTED_VALUES = []
    
    #print(BASE_VALUES)

    for i in range(games_df.shape[0]):
        LISTED_VALUES.append(BASE_VALUES)

    LISTED_VALUES = np.array(LISTED_VALUES)

    #print(LISTED_VALUES)


    full_df = pd.DataFrame(LISTED_VALUES, columns = all_columns)
    
    # Changing all names to be correct between eachother
    full_df.rename(columns={'Gambill JM.': 'Gambill J.M.', 'Lisnard JR.': 'Lisnard J.', 'Lopez Moron A.': 'Lopez-Moron A.', 'Marin JA.': 'Marin J.A.', 'Ferrero JC.': 'Ferrero J.C.', 'Perez-Alvarez E.': 'Alvarez E.', 'Chela JI.': 'Chela J.I.', 'Viloca-Puig JA.': 'Viloca J.A.', 'Burrieza-Lopez O.': 'Burrieza O.', 'Goellner MK.': 'Goellner M.K.', 'Van Scheppingen D.': 'van Scheppingen D.', 'Arnold Ker L.': 'Arnold L.', 'Mathieu PH.': 'Mathieu P.H.', 'Lee HT.': 'Lee H.T.', 'Yoon YI.': 'Yoon Y.', 'Zhu BQ.': 'Zhu B.Q.', 'Andersen JF.': 'Andersen J.F.', 'Wang YJ.': 'Wang Y.', 'Al-Khulaifi NG.': 'Al Khulaifi N.G.', 'Vassallo Arguello M.': 'Vassallo-Arguello M.', 'Guzman JP.': 'Guzman J.P.', 'Lisnard JR.': 'Lisnard J.R.', 'Gallardo-Valles M.': 'Gallardo Valles M.', 'Scherrer JC.': 'Scherrer J.C.', 'Zeng SX.': 'Zeng S.X.', 'Hippensteel KJ.': 'Hippensteel K.', 'Faurel JC.': 'Faurel J.C.', 'Matos Gil I.': 'Matos-Gil I.', 'Lu YH.': 'Lu Y.H.', 'Qureshi AUH.': 'Qureshi A.', 'Navarro I.': 'Navarro-Pastor I.', 'Wang YJ.': 'Wang Y.T.', 'Tsonga JW.': 'Tsonga J.W.'}, inplace=True)

    games_df.replace(
        to_replace=['di Pasquale A.', 'de Chaunac S.', 'Nadal-Parera R.', 'Kunitcin I.', 'Lisnard J.', 'Van Lottum J.', 'Hantschek M.', 'Bogomolov Jr.A.', 'Gambill J. M.', 'Bachelot J.F', 'Marin J.A', 'Mathieu P.', 'Schuettler P.', 'de Voest R.', 'Ramirez-Hidalgo R.', 'Bogomolov A.', 'di Mauro A.', 'Scherrer J.', 'Chela J.', 'Ferrero J.', 'Al Ghareeb M.', 'Al-Ghareeb M.', 'Qureshi A.U.H.', 'Wang Y.', 'van der Meer N.', 'van Gemerden M.', 'Lu Y.', 'Gimeno D.'],
        value=['Di Pasquale A.', 'De Chaunac S.', 'Nadal R.', 'Kunitsyn I.', 'Lisnard J.R.', 'van Lottum J.', 'Hantschk M.', 'Bogomolov Jr. A.', 'Gambill J.M.', 'Bachelot JF.', 'Marin J.A.', 'Mathieu P.H.', 'Schuttler P.', 'De Voest R.', 'Ramirez Hidalgo R.', 'Bogomolov Jr. A.', 'Di Mauro A.', 'Scherrer J.C.', 'Chela J.I.', 'Ferrero J.C.', 'Ghareeb M.', 'Ghareeb M.', 'Qureshi A.', 'Wang Y.T.', 'Van Der Meer N.', 'Van Gemerden M.', 'Lu Y.H.', 'Gimeno-Traver D.'],
        inplace=True)

    print(full_df)
    print(full_df.dtypes)


    for i, winner, loser in zip(range(games_df.shape[0]), games_df['winner'], games_df['loser']):
        full_df[winner].loc[i] = 1
        full_df[loser].loc[i] = 1

    print(full_df.head(30))
    # If Player 1 wins winner = 1 and if Player 2 wins winner = 0
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_1']] = 1
    train_df['Winner'].loc[train_df['Winner'] == train_df['Player_2']] = 0

    
    
    # Change Player_1, Player_2 and surface to onehotencoding
    numeric_train_df = pd.get_dummies(train_df, prefix=['Player_1', 'Player_2', 'Surface'], columns=['Player_1', 'Player_2', 'Surface'])

    # Make Winner int from object
    numeric_train_df['Winner'] = pd.to_numeric(train_df['Winner'], downcast = 'integer')
    print(numeric_train_df)

    # Splitting dataframe to train and test data
    train, test = train_test_split(numeric_train_df, test_size = 0.1)


    target = train.pop('Winner')
    dataset = tf.data.Dataset.from_tensor_slices((train.values, target.values))

    test_target = test.pop('Winner')
    dataset_2 = tf.data.Dataset.from_tensor_slices((test.values, test_target.values))

    for feat, targ in dataset.take(5):
        print ('Features: {}, Target: {}'.format(feat, targ))

    train_dataset = dataset.shuffle(len(train)).batch(5)
    test_dataset = dataset_2.shuffle(len(test)).batch(5)

    # Building the model
    def get_compiled_model():
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                        metrics=['accuracy']
                    )
        return model

    model = get_compiled_model()
    model.fit(train_dataset, epochs=1)

    test_loss, test_accuracy = model.evaluate(test_dataset)

    print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))


    # Pick players to test
    # Making an empty dataframe for the pick and filling it with 0
    COLUMN_NAMES = list(numeric_train_df.columns)
    BASE_VALUES = list()
    for i in range(len(COLUMN_NAMES)):
        BASE_VALUES.append(0)

    BASE_VALUES = np.array(list(BASE_VALUES))

    picked_df = pd.DataFrame(columns = COLUMN_NAMES)
    picked_df.loc[0] = BASE_VALUES
    print(picked_df)

    p1 = str(input('Name Player 1: '))
    p2 = str(input('Name Player 2: '))
    surface = str(input('Name surface: '))
    picked_df['Player_1_' + p1].loc[picked_df['Player_1_' + p1] == picked_df['Player_1_' + p1]] = 1
    picked_df['Player_2_' + p2].loc[picked_df['Player_2_' + p2] == picked_df['Player_2_' + p2]] = 1
    picked_df['Surface_' + surface].loc[picked_df['Surface_' + surface] == picked_df['Surface_' + surface]] = 1

    print(picked_df)

    for i in picked_df.columns:
        picked_df[i] = pd.to_numeric(picked_df[i], downcast = 'integer')


    pick_target = picked_df.pop('Winner')
    picked_dataset = tf.data.Dataset.from_tensor_slices((picked_df.values, pick_target.values))

    picked_dataset = picked_dataset.shuffle(len(picked_df)).batch(1)

    predictions = model.predict(picked_dataset)

    #Show results
    print(p1, 'Win chance against', p2, 'on', surface, 'court: {:.2%}'.format(predictions[0][0]))

if __name__ == "__main__":
    main()