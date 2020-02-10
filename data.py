# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import functools

import numpy as np
import pandas as pd
import tensorflow as tf
from pathlib import Path
#import tensorflow_datasets as tfds
import os

def main():
    train_data = Path('data/2000-2018-short.csv')
    test_data = Path('')

    
    df = pd.read_csv(train_data)
    print(df.head())

if __name__ == "__main__":
    main()