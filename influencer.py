#Robert

import pandas as pd



data = pd.read_csv('influencer.csv')

level = data['Month'].tolist()
level = data['Views'].tolist()
level = data['Dislikes'].tolist()
level = data['Subscriber(+-)'].tolist()
level = data['Revenue'].tolist()

#Find all videos with 2000 views or under
lowviews = []

def low_views(views):
    for index, row in data.iterrows():
        if row["Views"] <= views:
            lowviews.append(row["Month"])

    print(lowviews)
    lowviews.clear()

low_views(2000)
print(data.loc[0:10])

#Find all videos with 50000+ views
highviews = []

def high_views(views):
    for index, row in data.iterrows():
        if row["Views"] >= views:
            highviews.append(row["Month"])

    print(highviews)
    highviews.clear

high_views(50000)
print(data.loc[62:103])

#Find all videos that lost subscribers
subscriber_decline = []

def scandal(subs):
    for index, row in data.iterrows():
        if row["Subscriber(+-)"] <= subs:
            subscriber_decline.append(row["Month"])

    print(subscriber_decline)
    subscriber_decline.clear

scandal(0)
print(data.loc[98:133])
