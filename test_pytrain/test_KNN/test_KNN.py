#
# test KNN
#
# @ author becxer
# @ email becxer87@gmail.com
#
from test_pytrain import test_Suite
from pytrain.KNN import KNN
from pytrain.lib import fs
from pytrain.lib import batch


class test_KNN(test_Suite):

    def __init__(self, logging = True):
        test_Suite.__init__(self, logging)

    def test_process(self):
        sample_mat = [[1.0,1.1] , [1.0,1.0], [0,0], [0,0.1]]
        sample_label = ['A','A','B','B']
        
        knn = KNN(sample_mat, sample_label, 3)

        f1 = knn.predict([0.9,0.9])
        f2 = knn.predict([0.1,0.4])

        self.tlog("predict [0.9,0.9] to " + f1)
        self.tlog("predict [0.1,0.4] to " + f2)

        assert f1 == 'A'
        assert f2 == 'B'


class test_KNN_digit(test_Suite):

    def __init__(self, logging = True):
        test_Suite.__init__(self, logging)

    def test_process(self):
        dg_mat_train, dg_label_train = fs.f2mat("sample_data/digit/digit-train.txt",0)
        dg_mat_test, dg_label_test = fs.f2mat("sample_data/digit/digit-test.txt",0)
        knn_digit = KNN(dg_mat_train, dg_label_train, 3)
        error_rate = batch.eval_predict(knn_digit, dg_mat_test, dg_label_test, False)
        self.tlog("digit predict (with basic knn) error rate :" + str(error_rate))

