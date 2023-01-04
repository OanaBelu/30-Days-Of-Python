
# Project Avocados

"""The brief

For this project we're going to be working with a data set on Kaggle, which is an awesome site if you're interesting
in doing data science with Python. It contains tonnes of real data sets for you to use, absolutely free.

The data we're going to be working with today can be found here.

It contains thousands of records of avocado prices across several years in different regions of the US.

For this project I want to know a few different things about this data in this data set:

I want to know which region had the lowest average price for conventionally grown avocados each year, and I want to
know the same information for organic avocados.
I want to know which region had the highest average price for both types of avocado for each given year.
I want to know the lowest all time price for both conventionally grown and organic avocados, and I want to know the
highest price as well.
pandas has some built in tools for calculating averages, so you may want to look in the documentation to see how to do
that. There are also methods for finding the minimum and maximum value for a Series.

As a final note, the source data has many fields we don't need. Consider trimming the data down to just the region,
the year, the type of avocado, and the price.

Good luck!

Our solution
First things first, we need to actually download our source data and place the CSV document in our project workspace.
I'm going to be leaving my avocado.csv file in the root folder alongside my app.py.

Now that we have the data, we need to import pandas and read the data from the file.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    pass

There are several ways we can get the data out of the file and into a DataFrame. We could parse the data manually, or
we could use the csv module to get everything for us, for example. However, this is such a common operation, that
pandas has some built in tools to create a DataFrame directly from a CSV document.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices)

Here the read_csv function is going to parse the data in avocado_prices and turn it into a DataFrame for us. There are
plenty of other read_ functions available in pandas for working with other formats too. The tutorial talks about this
in more depth.

Now that we have our data, the next step is going to be trimming off all the fields we don't need. We only have four
that we want to keep in this case, so we're not going to use drop here.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices)

df = df[["year", "region", "AveragePrice", "type"]]

One problem here is that the headings are not very nice. They don't follow the Python naming conventions we're used to,
so I'm going to rename AveragePrice to price when creating the initial DataFrame.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

Next I'm going to split df into two smaller DataFrame objects: one for conventionally grown avocados, and one for
organic avocados.

The reason I'm doing this is because all of the tasks we've been set treat organic and conventional avocados
differently, so we'd constantly be filtering one set out while working with the data.

In order to get the conventional avocados, I'm going to use the query method. Our query in this case is quite simple,
we want all of the rows where the type of the avocado has the value "conventional".

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

conventional = df.query("type == 'conventional'")

At this point we no longer really need the type column for this smaller DataFrame, since all the values are the same.
We can drop column all on the same line, or we can do an in place drop instead.

If we do an in place drop, we have to remember to call copy on the line where we assign to conventional.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

conventional = df.query("type == 'conventional'").copy()
conventional.drop(columns="type", inplace=True)

Now we can do the same for our organic avocados.

app.py
import pandas as pd

with open("avocado.csv", "r") as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

conventional = df.query("type == 'conventional'").copy()
conventional.drop(columns="type", inplace=True)

organic = df.query("type == 'organic'").copy()
organic.drop(columns="type", inplace=True)

Now we have to figure out a way to calculate and store the average prices for each year in each region. Since this is
likely to be a complex process, and we have to do it multiple times, it's probably best that we define some functions.

We're also going to need to know the years covered by our data set. We can write this manually, or we can grab this
information from our original df by looking for unique values in the year column.

We can do that using the following attributes and methods:

years = df.year.unique()

In order to easily store the averages, I'm going to be creating a dictionary. The keys of this dictionary are going to
be the different years in our data set, and the values associated with those keys will be DataFrame objects that
contain the data for that specific year.

These DataFrame objects are going to contain a single row for each region, with the price for that region reflecting
the average price for the whole year.

First things first, let's define a function that can grab us just the values for a given year, returning a new
DataFrame for that year.

app.py
def filter_by_year(df, year):
    return df.query("year == @year").drop(columns="year")

Next let's define a function which arranges yearly averages for each region into a dictionary.

app.py
def get_average_by_year(df):
    averages = {}
    years = df.year.unique()

    for year in years:
        averages_for_year = filter_by_year(df, year).groupby("region").mean()
        averages.update({year: averages_for_year})

    return averages

We can now plug these into our existing code like so:

app.py
import pandas as pd

def get_average_by_year(df):
    averages = {}
    years = df.year.unique()

    for year in years:
        averages_for_year = filter_by_year(df, year).groupby("region").mean()
        averages.update({year: averages_for_year})

    return averages

def filter_by_year(df, year):
    return df.query("year == @year").drop(columns="year")

with open("avocado.csv", "r")as avocado_prices:
    df = pd.read_csv(avocado_prices).rename(columns={"AveragePrice": "price"})

df = df[["year", "region", "price", "type"]]

conventional = df.query("type == 'conventional'").copy()
conventional.drop(columns="type", inplace=True)

organic = df.query("type == 'organic'").copy()
organic.drop(columns="type", inplace=True)

conventional_averages = get_average_by_year(conventional)
organic_averages = get_average_by_year(organic)

Now that we have all our data organised how we want it, we just need a few for loops to output all the information we
were asked for.

I would recommend writing a function or two for this, since we need to repeat the code a fair number of times, but the
basic loop structure here is going to be something like this:

app.py
...

for year, data in conventional_averages.items():
    highest_value = data.price.max()
    location = data.query("price == @highest_value").index[0]
    print(f"Highest price for conventional avocados in {year} was ${highest_value:.2f} in {location}.")

print()

for year, data in conventional_averages.items():
    lowest_value = data.price.min()
    location = data.query("price == @lowest_value").index[0]
    print(f"Lowest price for conventional avocados in {year} was ${lowest_value:.2f} in {location}.")

print()

Everything here we've seen before, but we do need to mention this .index[0]. When we performed out groupby operation
by region, the regions were turned into the row indices for the new DataFrame. We therefore have to use the index
attribute to get the region. This is going to give us a list of indices, and we're just grabbing the first item in
this case.

The final thing we need to do is calculate the overall lowest and highest values for both types of avocados.

app.py
highest_conventional = conventional.price.max()
print(f"The highest price for conventional avocados was ${highest_conventional:.2f}")

lowest_conventional = conventional.price.min()
print(f"The lowest price for conventional avocados was ${lowest_conventional:.2f}")

highest_organic = organic.price.max()
print(f"The highest price for organic avocados was ${highest_organic:.2f}")

lowest_organic = organic.price.min()
print(f"The lowest price for organic avocados was ${lowest_organic:.2f}")

"""

