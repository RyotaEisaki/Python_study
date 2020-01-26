from matplotlib import pyplot as plt 
from sklearn.datasets import load_iris
import numpy as np

data= load_iris()

features = data['data']
features_names=data['feature_names']
target=data['target']
target_names=data['target_names']
labels=target_names[target]

for t,marker,c in zip(range(3),">ox","rgb"):
    plt.scatter(features[target==t,0],
                features[target==t,1],
                marker=marker,
                c=c)