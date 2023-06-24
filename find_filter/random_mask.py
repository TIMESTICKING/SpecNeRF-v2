import numpy as np
import scipy.io as sio


num = 160
shape = (9, 19)


total = shape[1] * shape[0]


maskv = np.array([0] * (total - num) + [1] * num)
np.random.shuffle(maskv)
mask = maskv.reshape(shape)

print(mask)
print(np.sum(mask))
sio.savemat(f'./find_filter_res/random_{str(shape).replace(" ", "")}_{num}.mat', {'mask': mask})
