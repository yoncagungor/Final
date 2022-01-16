# MBG_6133 Final <a name="final"></a> 

>This repository includes the python code that is written for the final of MBG_6133.

### Q1: In python, by using Jupyter Notebook:

> To use the Jupyter Notebook, first the [Anaconda](https://www.anaconda.com/products/individual) software should be downloaded.

1. Create a 100x100 numpy array (100x100 matrix), composed of random numbers. The random numbers should be integers and vary between [0, 100].


    #### Calling the required packages:

    ```python
    import numpy as np
    import matplotlib.pylab as plt
    import seaborn as sns
    ```

    #### Creating a 100x100 matrix with 100 columns and 100 rows containing random integers with max value of 100.

     ```python
    ary = np.random.randint(100, size=(100,100))  
     ```
    #### To show the dimensions I've used the below code. 

     ```python
    ary.shape
     ```
     > (100, 100)
    #### The number in the first position shows the row number while the number in the second position shows the column number.
    
2. Make a heatmap of your 100x100 array

    #### To produce a heatmap of my 100X100 matrix, I have used plt.imshow().interpolation= 'nearest' option creates a heatmap with higher resolution.

     ```python
    plt.imshow(ary, interpolation= 'nearest')
    plt.show()
      ```
