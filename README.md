# Calculating the cumulative distribution for the data

What you have just plotted is almost a graph of the so-called cumulative probability distribution, ![](https://render.githubusercontent.com/render/math?math=P(X\le\x)).  As we will learn throughout the rest of the course the cumulative probability distribution is very important.  It is thus worth expending some additional effort now and plotting this distribution.  Watching [the video](https://www.youtube.com/watch?v=VaZTKmcxLvY) will help you to better understand this exercise.  

I have started writing the code to calculate the cumulative distribution for you in the file `main.py`.  As you can see I have loaded the data set from the file data.dat saved it in a list called `x`.  The two lines at the end of the script that read:

````
plt.plot( x, y, 'k-' )
plt.savefig("cumulative-pdf.png")
````

Are then going to plot our cumulative probability distribution function.  You will notice that the list called `y` that we are plotting with the plot command is not defined anywhere in the code.  One of your tasks is, therefore, to write the code that calculates this variable.  

Recall from the video that calculating the cumulative distribution for a dataset involves two steps:

1. Sorting the data (you know from the last exercise how to do this)
2. Plotting a graph in which the x-coordinates give the sorted data values and the y-coordinates are the index of the corresponding x coordinate in the sorted list divided by the total number of points in the list. .

Once you have sorted `x` you just need to create the list called `y` that you are going to plot.  This list is going to contain the numbers between 1 and the number of data points in your list divided by the total number of data points.  If you had four data points `y` would thus be:

````
y = [1/4, 2/4, 3/4, 4/4]
````

Try to write the rest of the code to plot your cumulative probability distribution now.
