from sklearn import tree
clf = tree.DecisionTreeClassifier()
x=[
    [220,110,35],[290,60,15],[260,75,30],[210,140,15]
]
y=['yaxshi','yomon','o`rtacha','yaxshi']
clf=clf.fit(x,y)
taxmin=clf.predict([[221,105,29]])
print(taxmin)