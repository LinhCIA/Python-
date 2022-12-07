import os
directory = "Bye"
parent = "C:/Hello/"
path = os.path.join(parent, directory)
os.rmdir(path)
