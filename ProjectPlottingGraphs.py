
# Project Plotting Graphs
"""The brief

As we develop this application, remember that to plot a scatter chart we just need the x and y values we want to plot.
Most of the code we'll write will be concerned with getting that data, so we can chart it easily with just a few lines
of code.

First of all, you may want to create a file and call it iris.csv. Make it contain the following data:
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5,3.6,1.4,0.2,Iris-setosa
7,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
6.9,3.1,4.9,1.5,Iris-versicolor
5.5,2.3,4,1.3,Iris-versicolor
6.5,2.8,4.6,1.5,Iris-versicolor
6.3,3.3,6,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
7.1,3,5.9,2.1,Iris-virginica
6.3,2.9,5.6,1.8,Iris-virginica
6.5,3,5.8,2.2,Iris-virginica

After we've completed this project, feel free to experiment with other data sets too!

For this project users should be able to:

    Create a scatter plot where the x axis is the species and the y axis is one of the other columns.
    Via a user menu, tell us the column they would like to plot in the y axis.
    Also via the menu, tell us the name of the file they would like to create to contain the final plot image.

I would recommend tackling this project this way:

    Use the file [main.py](<http://main.py>) to contain the user menu.
    Create a file, such as data_storage.py, that contains functions to read the iris.csv data file.
    Create a third file, graphing.py, that contains a function that creates the scatter plot given the x and y values.
"""