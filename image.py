import numpy as np
import matplotlib.pyplot as plt
#建立图像处理类
class imageProcessing:
    #初始化类属性
    def __init__(self, origin_image, reserve_rate):
        self.origin_image = origin_image
        self.reserve_rate =  reserve_rate 
        self.result = np.zeros(self.origin_image.shape)
    #SVD图像压缩
    def zip_image_by_svd(self):
    
        print("\n\n======starting zip======")

        #self.result = np.zeros(self.origin_image.shape)
        u_shape = 0
        s_shape = 0
        vT_shape = 0
        size_used = 0
        result_data_size = 0
        for chan in range(3):
            #对图像矩阵进行SVD分解，返回的奇异值sigma以降序排列
            U, sigma, V = np.linalg.svd(self.origin_image[:, :, chan])
            print(sigma)
            self.n_sigmas = int(self.reserve_rate * sigma.size)
            #self.n_sigmas = 0
            #temp = 0
            ##设置一个阈值，按照奇异值之和占比来确定保留奇异值的个数
            #while (temp / np.sum(sigma)) < self.reserve_rate:
            #    temp += sigma[self.n_sigmas]
            #    self.n_sigmas += 1

            S = np.zeros((self.n_sigmas, self.n_sigmas))

            for i in range(self.n_sigmas):
                S[i, i] = sigma[i]
            #进行图像压缩
            self.result[:, :, chan] = (U[:, 0:self.n_sigmas].dot(S)).dot(V[0:self.n_sigmas, :])
            u_shape = U[:, 0:self.n_sigmas].shape
            s_shape = S.shape
            vT_shape = V[0:self.n_sigmas, :].shape


        for i in range(3):
            MAX = np.max(self.result[:, :, i])
            MIN = np.min(self.result[:, :, i])
            self.result[:, :, i] = (self.result[:, :, i] - MIN) / (MAX - MIN)


        self.result  = np.round(self.result * 255).astype('int')
        size_used += u_shape[0] * u_shape[1] + s_shape[0] * s_shape[1] + vT_shape[0] * vT_shape[1]
        
        #计算压缩比
        self.zip_rate = self.origin_image.size/ size_used
        
        #print("matix size used：     3 x ({} + {} + {})". format(u_shape, s_shape, vT_shape))


