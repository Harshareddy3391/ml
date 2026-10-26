#imports
import pandas as pd
import numpy as np

from  sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline  import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



#Load data set
