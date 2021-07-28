# 479-Project-2

#### Group members:

* Naoki Atkins naokishami@csu.fullerton.edu

* Luke Duggan luke.duggan@csu.fullerton.edu

* Madison Jordan madisonjordan@csu.fullerton.edu

***

**KNN Parallelization in Author Classification**

In this project, we created a program that will classify an unknown book to an author given a dataset that contains already known books with labels to their authors. 

*** 

#### Text Preprocessing
run each time a new dataset needs to be generated (if a new book is added).

* input folder (book text files): `\books`
* output folder (dataset files): `\data`

First run top.py to find the "bag of words" from each book. After that, you'll need to run set.py so that each "bag of words" can be combined into a single table. 

1. `python3 top.py`
2. `python3 set.py`

#### Compiling

`mpic++ -fopenmp main.cpp`


#### Run Program
`mpirun -n 4 ./a.out`

note: n processes should be the number of books in the set. (used in cosine calculation before finding KNN). k is a separate value from n. k is defined within the code at this time (k=3). 


