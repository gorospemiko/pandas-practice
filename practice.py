import pandas as pd
print(pd.__version__)

mydataset = {
    'cars': ["bmw", 'volvo'],
    'passing': [2, 3]
}
myvar = pd.DataFrame(mydataset)

myvar.info()
print(myvar)