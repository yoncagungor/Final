<a name="final"></a> 
# MBG_6133 Final 

>This repository includes the python code that is written for the final of MBG_6133.

## Direct Links to Questions

- [Question 1.1](#q1.1) : Create 100 x 100 Numpy array.

- [Question 1.2](#q1.2) : Make a heatmap from your matrix.

- [Question 2.1](#q2.1) : Select even numbers, make them logical operators and show them as integers.

- [Question 2.2](#q2.2) : Make another heatmap from your new array.
- [Question 3](#q3) : Relevant Jupyter Notebook

## Q1: In python, by using Jupyter Notebook:
[back to top](#final)
<a name="q1.1"></a>
> To use the Jupyter Notebook, first the [Anaconda](https://www.anaconda.com/products/individual) software should be downloaded.


### 1.1. Create a 100x100 numpy array (100x100 matrix), composed of random numbers. The random numbers should be integers and vary between [0, 100].


   Calling the required packages:

   ```python
    import numpy as np
    import matplotlib.pylab as plt
    import seaborn as sns
   ```

   Creating a 100x100 matrix with 100 columns and 100 rows containing random integers with max value of 100.

   ```python
    ary = np.random.randint(100, size=(100,100))  
   ```
  To show the dimensions `.shape` can be used.

   ```python
    ary.shape
   ```
       (100, 100)
   <a name="q1.2"></a>
   > The number in the first position shows the row number while the number in the second position shows the column number.
    
### 1.2. Make a heatmap of your 100x100 array.


   To produce a heatmap of my 100X100 matrix, I have used `plt.imshow()`.

   ```python
    plt.imshow(ary, interpolation= 'nearest')
    plt.show()
    
    #interpolation= 'nearest' option creates a heatmap with higher resolution.
   ```
      
      The resulting plot:
     
  ![output](https://github.com/yoncagungor/Final/blob/main/ary_plot?raw=true)
  
 <a name="q2.1"></a>  
 
## Q2: By using the same matrix:
[back to top](#final)
### 2.1. Filter out the odd numbers. Then, if present, convert True/False statements into [0,1] values. Preserve the 100x100 array shape.

 To filter out the odd numbers (or select the even ones in other words), I created a logical vector that returns True for even numbers.

   ```python
       even = (ary % 2 == 0 )
       print(even)
   ```
       
       [[False False False ...  True  True False]
        [ True False False ... False False False]
        [False  True  True ...  True False  True]
        ...
        [ True  True False ... False  True False]
        [ True  True  True ... False False  True]
        [False  True  True ... False  True False]]
              
   If I want to see the numbers as they are, I need to use  `ary[even] `.
   
  ```python
     print(ary[even])
   ```
        [76, 22, 26, ..., 10, 14, 96]
        
 I have used the `.astype` option and called it `ary_even_int`.
  ```python
    ary_even_int = even.astype(int)
    print(ary_even_int)
   ```
        [[0 0 0 ... 1 1 0]
         [1 0 0 ... 0 0 0]
         [0 1 1 ... 1 0 1]
         ...
         [1 1 0 ... 0 1 0]
         [1 1 1 ... 0 0 1]
         [0 1 1 ... 0 1 0]]
         
 To show that the shape of the array is preserved:     
   ```python
   ary.shape 
   ```
        (100,100) 
   ```python
    ary_even_int.shape
   ```
        (100,100)
    
    
  <a name="q2.2"></a> 
  
  ### 2.2. Make a heatmap of your new 100x100 array (20 points)

  
   To create the heatmap of my new array, I have used the below code.
    
  ```python
    plt.imshow(ary_even_int, interpolation='nearest')
    plt.show()
   ```
     The resulting plot:
     
   ![output](https://github.com/yoncagungor/Final/blob/main/ary_even_int?raw=true)
   
   <a name="q3"></a>
   ## Q3. Create a Github repo, explaining your code, the usage of your code, its outputs, and the relevant Jupyter Notebook. 
   [back to top](#final)
   
   - [Here](https://github.com/yoncagungor/Final/blob/35cf3f938f0c7fb5647c013954732473d172509f/MBG6133_Final_YoncaGu%CC%88ngo%CC%88r/MBG6133_Final_YoncaG%C3%BCng%C3%B6r.md) you can find the file that includes the raw input and outputs.
   
   - Also, [here](https://github.com/yoncagungor/Final/blob/49a37a10d43c8ca8de7e32b16ca160f0af46225b/Jupyter%20Notebook.ipynb) you can find the jupyter notebook code as it is.
