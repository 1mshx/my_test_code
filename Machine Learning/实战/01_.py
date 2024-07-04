import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

listings = pd.read_csv(r'D:\OneDrive\桌面\房间数据集\listings.csv.gz')

listings['price'] = listings['price'].str.replace('$', '')
listings['price'] = listings['price'].str.replace(',', '')
listings['price'] = listings['price'].astype(float)
listings = listings.loc[(listings['price'] <= 600) & (listings['price'] > 0)]

listings.amenities = listings.amenities.str.replace('[', '').str.replace('"', '').str.replace(']', '')

colums = ['host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'has_availability', 'instant_bookable']

for c in colums:
    listings[c] = listings[c].replace('f', 0, regex=True)
    listings[c] = listings[c].replace('t', 1, regex=True)

new_listings = listings[
    ['host_is_superhost', 'host_identity_verified', 'host_has_profile_pic', 'instant_bookable', 'host_listings_count',
     'host_total_listings_count', 'minimum_nights', 'bathrooms_text', 'bedrooms', 'number_of_reviews',
     'review_scores_rating', 'price']]

new_listings['bedrooms'] = new_listings['bedrooms'].fillna(value=0)

for cat_feature in ['property_type', 'room_type']:
    new_listings = pd.concat([new_listings, pd.get_dummies(listings[cat_feature])], axis=1)

new_listings.dropna(subset='bathrooms_text', inplace=True)

for col in new_listings.columns[new_listings.isnull().any()]:
    new_listings[col] = new_listings[col].fillna(new_listings[col].median())

listings_new = new_listings.reset_index(drop=True)

import re

listings_new['bathrooms'] = 0
listings_new['bathrooms_type'] = 0
for i in range(len(listings_new)):
    pattern = r"(\d\.5|\d)"
    pattern1 = r"[a-z]+\b"
    a = re.findall(pattern1, listings_new['bathrooms_text'][i])
    b = re.findall(pattern, listings_new['bathrooms_text'][i])
    if a[0] == 'shared':
        listings_new['bathrooms_type'][i] = 1
    elif a[0] == 'private':
        listings_new['bathrooms_type'][i] = 2
    else:
        listings_new['bathrooms_type'][i] = 3

    if len(b) == 0:
        listings_new['bathrooms'][i] = 1
    else:
        listings_new['bathrooms'][i] = b[0]

listings_new['bathrooms'] = listings_new['bathrooms'].astype(float)

new_listings = listings_new.drop(columns='bathrooms_text')

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

y = new_listings['price']
X = new_listings.drop('price', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100)

from sklearn.preprocessing import StandardScaler

std = StandardScaler()
X_fit = std.fit(X_train)
X_train = X_fit.transform(X_train)
X_test = X_fit.transform(X_test)

rf = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
rf.fit(X_train, y_train)
y_train_predict = rf.predict(X_train)
y_test_predict = rf.predict(X_test)
rmse_rf = mean_squared_error(y_test, y_test_predict) ** (1 / 2)
r2_rf = r2_score(y_test, y_test_predict)

print(r2_rf)
print(rmse_rf)

from lightgbm import LGBMRegressor

fit_params = {
    # 'early_stopping_rounds': 10,
              'eval_metric': 'rmse',
              'eval_set': [(X_test, y_test)],
              'eval_names': ['valid'],
              # 'verbose': 1
              }

lgb = LGBMRegressor(max_depth=20, learning_rate=0.01, n_estimators=1000)
# max_depth=20  最大深度,learning_rate=0.01 学习率，一般很小，防止过拟合,n_estimators=1000 轮数，看往里加多少个数
lgb.fit(X_train, y_train, **fit_params)
