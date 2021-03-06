import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='BayesianClustering663',  
     version='0.3',
     author="Azucena Morales<lm348@duke.edu>, Alan Zhou<zz161@duke.edu>",
     author_email="alanazu@googlegroups.com",
     description="Bayesian Hierachichal Clustering using Heller's article",
     long_description = long_description,
     url="https://github.com/AzucenaMV/STAT-663",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
