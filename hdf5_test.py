'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: hdf5使用方法
@Date: 2019-07-24 16:17:08
@LastEditors: AnakinJiang
@LastEditTime: 2019-07-24 16:51:32
'''

import h5py
import numpy as np
import pickle
import os

def compare_size():

    # HDF5的写入：
    imgData = np.zeros((30, 3, 128, 256))
    with h5py.File('HDF5_FILE.h5', 'w') as f:
        f['data'] = imgData  # 将数据写入文件的主键data下面
        f['labels'] = range(100)  # 将数据写入文件的主键labels下面

    # HDF5的读取：
    with h5py.File('HDF5_FILE.h5', 'r') as f:
        f.keys()  # 可以查看所有的主键
        a = f['data'][:]  # 取出主键为data的所有的键值
        print(a)

    # 测试pkl保存
    with open('test.pkl', 'wb') as f:
        pickle.dump(imgData, f)

    # 测试txt保存
    np.savetxt('test.txt', imgData.reshape(2, -1))

def save_hdf5():

    file_name = 'test.hdf5'
    with h5py.File(file_name) as f:
        f.create_group('/grp1') 
        f.create_group('/grp1/grp2') 
        data = np.arange(6).reshape(2, 3)
        f.create_dataset('dset1', data=data)
        f.create_dataset('grp1/dset2', data=data)
        f.attrs['a'] = 1 
        f['grp1'].attrs['b'] = 'xyz'
        f['grp1/dset2'].attrs['c'] = np.array([1, 2])
    with h5py.File(file_name, 'r') as f: 
        print(list(f.keys()))
        print(list(f['grp1'].keys()))
        print('/dset1 = %s' % f['dset1'][:])
        print('/grp1/dset2 = %s' % f['/grp1/dset2'][:])
        print(f.attrs['a'])
        print(f['grp1'].attrs['b'])
        print(f['grp1/dset2'].attrs['c'])
    os.remove(file_name)
    
if __name__ == "__main__":
    # compare_size()
    save_hdf5()
    