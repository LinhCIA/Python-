import os
directory = "nnlt"
parent_dir = "C:\CNTT\data"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)

