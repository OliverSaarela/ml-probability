# coding=utf-8

import tensorflow as tf
import data

# This is a file that contains functions that server uses to get its data.

# Returns a prediction for the server
def get_prediction(p1, p2, surface):
    model = tf.keras.models.load_model('./data/saved_model.h5')
    prediction = data.make_prediction(model, p1, p2, surface)
    return prediction

# Get's all player names for the server
def get_players():
    players = data.get_all_players()
    return players