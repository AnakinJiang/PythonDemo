'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: pickle的用法
@Date: 2019-07-24 15:34:06
@LastEditors: AnakinJiang
@LastEditTime: 2019-07-24 15:45:55
'''

import pickle

def data_test():
    var_a = {'a':'str', 'c': True, 'e': 10, 'b': 11.1, \
        'd': None, 'f': [1, 2, 3], 'g':(4, 5, 6)}
    var_b = pickle.dumps(var_a) # 序列化
    var_c = pickle.loads(var_b) # 反序列化
    with open('data_pickle.pkl', 'wb') as f1: # 持久化到文件
        pickle.dump(var_a,f1)
    with open('data_pickle.pkl', 'rb') as f2: # 从文件中读取
        var_d = pickle.load(f2)
    print(var_a)
    print(var_b)
    print(var_c)
    print(var_d)

def custom_data_test():
    class Student(object):
        def __init__(self, name, age, sno):
            self.name = name
            self.age = age
            self.sno = sno

        def test(self):
            print(self.name)
        
        def __repr__(self):
            return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

    var_a = Student('Tom', 19, 1)
    var_b = pickle.dumps(var_a)
    var_c = pickle.loads(var_b)
    with open('custom_data_pickle.pkl', 'wb') as f1: # 持久化到文件
        pickle.dump(var_a,f1)
    with open('custom_data_pickle.pkl', 'rb') as f2: # 从文件中读取
        var_d = pickle.load(f2)
    print(var_a)
    print(var_b)
    print(var_c)
    print(var_d)
    var_d.test()

def read_pt():
    filename = '/media/jinpengjiang/DataSet/MNIST/processed/test.pt'
    with open(filename, 'rb') as f:
        var_a = pickle.load(f)
    print(var_a)

if __name__ == "__main__":
    # data_test()
    # custom_data_test()
    read_pt()