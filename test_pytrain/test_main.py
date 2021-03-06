#
# Dev test for pytrain library
#
# @ author becxer
# @ email becxer87@gmail.com
# --------------------------------------------
import sys
from test_lib import *
from test_KNN import *
from test_DecisionTreeID3 import *
from test_NaiveBayes import *
from test_GaussianNaiveBayes import *
from test_Apriori import *
from test_LinearRegression import *
from test_LogisticRegression import *
from test_NeuralNetwork import *
from test_Kmeans import *
from test_DBSCAN import *
from test_HierarchicalClustering import *
from test_SVM import *
from test_HMM import *
from test_CRF import *

# Toggle dataset
IRIS = False # Toggle for IRIS dataset testing
MNIST = False # Toggle for MNIST dataset testing
WORD_SPACE = False # Toggle for WORD_SPACE dataset testing

# 0. Test lib modules
test_dataset(logging = False).process()
test_fs(logging = False).process()
test_normalize(logging = False).process()
test_autotest(logging = False).process()
test_nlp(logging = False).process()

# 1. Supervised learning
# 1-1. Categorical variables
# - Test Decision Tree
test_DecisionTreeID3(logging = False).process()
test_DecisionTreeID3_lense(logging = False).process()
# - Test NaiveBayes
test_NaiveBayes(logging = False).process()
test_NaiveBayes_email(logging = False).process()

# 1-2. Continuous variables
# - Test GaussianNaiveBayes
test_GaussianNaiveBayes(logging = False).process()
test_GaussianNaiveBayes_rssi(logging = False).process()

# - Test KNN
if IRIS :
    test_KNN_iris(logging = False).process()
if MNIST :
    test_KNN_mnist(logging = False).process()
# - Test LinearRegression
test_LinearRegression(logging = False).process()
if IRIS :
    test_LinearRegression_iris(logging = False).process()
if MNIST :
    test_LinearRegression_mnist(logging = False).process()
# - Test LogisticRegression
test_LogisticRegression(logging = False).process()
if IRIS :
    test_LogisticRegression_iris(logging = False).process()
if MNIST :
    test_LogisticRegression_mnist(logging = False).process()
# - Test FNN
test_FNN(logging = False).process()
if IRIS :
    test_FNN_iris(logging = False).process()
if MNIST:
    test_FNN_mnist(logging = False).process()
# - Test SVM
test_SVM(logging = False).process()
test_SVC(logging = False).process()
if IRIS:
    test_SVC_iris(logging = False).process()
if MNIST:
    test_SVC_mnist(logging = False).process()

# 1-3. Sequential variables
# - Test HMM
test_HMM(logging = False).process()
test_HMM_BaumWelch(logging = False).process()
if WORD_SPACE:
    # TODO : add word spacing test
    pass

# - Test CRF
test_CRF(logging = True).process()
if WORD_SPACE:
    # TODO : add word spacing test
    pass

# 2. Unsupervised learning
# 2-1. Association
# - Test Apriori
test_Apriori(logging = False).process()
test_Apriori_mushroom(logging = False).process()
# 2-2. Clustering
# - Test Kmeans
test_Kmeans(logging = False).process()
# - Test DBSCAN
test_DBSCAN(logging = False).process()
# - Test HierarchicalClustering
test_HierarchicalClustering(logging = False).process()

