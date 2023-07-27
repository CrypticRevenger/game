import pickle
from os import path
import numpy as np

for level in range(0, 8):
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        data = pickle.load(pickle_in)
        data = np.array(data)

        (il, jl) = data.shape

        write = open(f'lv{level}', 'w')

        new_data = ""
        for i in range(il):
            for j in range(jl):
                new_data = new_data + str(data[i, j]) + " "
            new_data = new_data + "\n"

        write.write(new_data)


