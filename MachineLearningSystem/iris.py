from matplotlib import pyplot as plt 
from sklearn.datasets import load_iris

data= load_iris()

features = data['data']
features_names=data['feature_names']
target=data['target']
target=names=data['target_name']
labels=tarbet_name[target]

for t,marker,c, in zip(xrange(3),">ox","rgb"):
    plt.scatter(features[target==t,0],
                features[target==t,1],
                marker=marker,
                c=c)