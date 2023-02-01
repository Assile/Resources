# Pandas
> **Note**: Right now this page is still quite a stub. There is more knowledge in my head on pandas, however I don't have the time to jot it all down at once.

# Methods

## General overview of the data
- `df.describe()`: Get a statistical overview of numeric columns. To also include non-numeric columns use `df.describe(include='all')`.
- `df.info()`: Shows the number of filled rows, so you can guage the amount of `NaN`/Null/`None` values in a column. Also shows the **type** of the column, which is very useful to check whether columns have the type you expect. String columns are marked with type **object**.

## Selection
- `df.head()` / `df.tail()`: Selects the first/last five rows of the data or as much as was given as a parameter (`df.head(10)` for ten rows).
- *Rows by name*: `df[row_name]` for a single row or `df[iterable_of_row_names]` to select multiple. The order of the row names in the iterable (list, tuple, etc.) is also the order of rows that are returned. Duplicate selections are possible.
- *Columns by name*: `df['column']` to select a single **Series** or `df[['column1', 'column2']]` to select multiple columns, which results in a **DataFrame**. The order of the column names in the list is also the order in which they appear in the resulting dataset. Duplicate selections are possible.
- *Rows and columns by name*: `df.loc[rows, columns]` to select on both rows and columns. To select all rows, or all columns use `:` (`df.loc[:, columns]` or `df.loc[rows, :]`). Ranges are inclusive (`df.loc[5:10]` results in rows names 5 through and inclusing 10 being selected).
- *Rows and columns by index*: `df.iloc[]` with the same rules as `.loc` with the exception that for `.iloc` the range is not inclusive.
> Two subsets pf methods are less known to beginning users of Pandas. However, using them speeds up common operations such as `.str.split()`, `.str.replace()`, or `.dt.date`, which is why I want to highlight the whole categories here:
- [String related](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html?highlight=str#pandas.Series.str.split)
- [Datetime related](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html?highlight=dt)
