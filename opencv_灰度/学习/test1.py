import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url = "./data/iris.data"
names = ['sepal-length(萼片长度)', 'sepal-width(萼片宽度)', 'petal-length(花瓣长度)', 'petal-width(花瓣宽度)', 'class(名)']
dataset = pandas.read_csv(url, names=names)
print(dataset)
print('dataset.shape = ',dataset.shape)
print('dataset.head() = ',str(dataset.iloc[-1]).replace('\n',''))
print('dataset.describe() = ',dataset.describe())
print('*'*100)
print(dataset.groupby("class(名)").size())
print('*'*100)
print(dataset.groupby("sepal-length(萼片长度)").size())
print('*'*100)

# dataset.plot(kind='line',subplots=True,layout=(2,2),sharex=False,sharey=False)
# plt.show()

# dataset.hist('petal-length(花瓣长度)')
# plt.show()

# scatter_matrix(dataset)
# plt.show()
print('dataset.index=',dataset.index)
print('*'*100)
array = dataset.values
print(array)
print('*'*100)

X = array[:,0:4]
print(X)
print('*'*100)
Y = array[:,4]
print(Y)
print('*'*100)
validation_size = 0.2
seed = 7
scoring = 'accuracy'
X_train,X_validation,Y_train,Y_validation = model_selection.train_test_split(X,Y)
print(X_train)
print('*'*100)
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed,shuffle=True)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    # print('*' * 100)
    # print(cv_results)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

print(help(pandas))