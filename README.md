# DataMatrix
# Introduction:
Data Matrix is a program is efficiently organize, visualize, and work with Secondary Array (or 2D Array)

This is completely written in [python](https://www.python.org/downloads/) , with custom made exceptions to guide through the errors made.

This script run most importantly on [tabulate](https://pypi.org/project/tabulate/) module,
can be installed by:
`pip install tabulate`

# Working with DataMatrix:
## Initialization of a DataMatrix

A DataMatrix can be created in the following ways:
* By a scalar value
* By a 1D array (*List*)
* By a 2D array.

**By an scalar value:**
```
>>> Obj = DataMatrix(1)
>>> print(Obj)
╭───╮
│ 1 │
╰───╯
```
**By a 1D array**
```
>>> Obj = DataMatrix([1,2,3,4])
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ 2 │ 3 │ 4 │
╰───┴───┴───┴───╯
```
**By a 2D array**
```
>>> Obj = DataMatrix([[1,2,3,4],[5,6,7,8]])
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
╰───┴───┴───┴───╯
```

## Amplitudes and Altitudes:

- Amplitude is the number of columns in the DataMatrix
- Altitude is the number of rows in the DataMatrix
It can retrieved by:  
```
>>> Obj = DataMatrix([[1,2,3],[4,5,6]])
>>> Obj.amp
3
>>> Obj.alt
2
>>> Obj.dim
'2x3'

```
The `.dim` attribute is the dimension of your DataMatrix Object.

## Attributes
There are 4 attributes you can change.
* Style: *Style of the table*
* Headers: *Define the headers of the table*
* Index: *Lists Indexes in the table*
* Axis: *Targeting Rows or Column*

### Style:
These Styles are completely based on the Tabulate module; The list of style this modules allows is;
- plain
- simple
- github
- grid
- simple_grid
- rounded_grid
- heavy_grid
- mixed_grid
- double_grid
- fancy_grid
- outline
- simple_outline
- rounded_outline
- heavy_outline
- mixed_outline
And much more, please visit [tabulate](https://pypi.org/project/tabulate/) docs to get all styles.

At Default, the style is set to 'rounded_grid', You can change the style like:
```
>>> Obj.style = 'fancy_grid'
>>> print(Obj)
╒═══╤═══╤═══╤═══╕
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
╘═══╧═══╧═══╧═══╛
>>> Obj.style = 'html'
>>> print(Obj)
<table>
<tbody>
<tr><td style="text-align: right;">1</td><td style="text-align: right;">2</td><td style="text-align: right;">3</td><td style="text-align: right;">4</td></tr>
<tr><td style="text-align: right;">5</td><td style="text-align: right;">6</td><td style="text-align: right;">7</td><td style="text-align: right;">8</td></tr>
</tbody>
</table>
```

### Headers:
The headers are list which always stays on top of the table.
The header list must be of the length of columns of the 2D array, else will raise an error.
To assign a header.
```
>>> Obj = DataMatrix([['July','09-01-2001'],['Marvin','18-07-2001']])
>>> Obj.headers = ['Name', 'DOB']
>>> print(Obj)
╭────────┬────────────╮
│ Name   │ DOB        │
├────────┼────────────┤
│ July   │ 09-01-2001 │
├────────┼────────────┤
│ Marvin │ 18-07-2001 │
╰────────┴────────────╯
```

### Index:

The index attribute will give list the indexes of both rows and columns.
Index is accept only Boolean values (`True` or `False`).
Any other value will raise an error.
For example:
```
>>> Obj = DataMatrix([['July','09-01-2001'],['Marvin','18-07-2001']])
>>> print(Obj)
╭────────┬────────────╮
│ July   │ 09-01-2001 │
├────────┼────────────┤
│ Marvin │ 18-07-2001 │
╰────────┴────────────╯
>>> Obj.index = True
>>> print(Obj)
╭─────┬────────┬────────────╮
│   0 │ 1      │ 2          │
├─────┼────────┼────────────┤
│   1 │ July   │ 09-01-2001 │
├─────┼────────┼────────────┤
│   2 │ Marvin │ 18-07-2001 │
╰─────┴────────┴────────────╯

```
So any cell, row or column can be accessed using the index.

### Axis
Axis can have only 2 values `1` or `0`.
This is will be useful later on. Any other value other `0 or 1`, will raise an Error:
```
>>> Obj.axis = 0
>>> Obj.axis = 1
```

### Also;
* With Headers and with Index:
```
>>> Obj = DataMatrix([['July','09-01-2001'],['Marvin','18-07-2001']])
>>> Obj.headers = ['Name','Dob']
>>> Obj.index = True
>>> print(Obj)
╭────────┬────────┬────────────╮
│   None │ Name   │ Dob        │
├────────┼────────┼────────────┤
│      0 │ 1      │ 2          │
├────────┼────────┼────────────┤
│      1 │ July   │ 09-01-2001 │
├────────┼────────┼────────────┤
│      2 │ Marvin │ 18-07-2001 │
╰────────┴────────┴────────────╯
```
* With Headers and with Non Index:
```
>>> Obj.headers = ['Name','Dob']
>>> Obj.index = False
>>> print(Obj)
╭────────┬────────────╮
│ Name   │ Dob        │
├────────┼────────────┤
│ July   │ 09-01-2001 │
├────────┼────────────┤
│ Marvin │ 18-07-2001 │
╰────────┴────────────╯
```
* Without Headers and with Index:
```
>>> Obj.headers = None
>>> Obj.index = True
>>> print(Obj)
╭─────┬────────┬────────────╮
│   0 │ 1      │ 2          │
├─────┼────────┼────────────┤
│   1 │ July   │ 09-01-2001 │
├─────┼────────┼────────────┤
│   2 │ Marvin │ 18-07-2001 │
╰─────┴────────┴────────────╯
```
* Without Headers and without Index
```
>>> Obj.headers = None
>>> Obj.index = False
>>> print(Obj)
╭────────┬────────────╮
│ July   │ 09-01-2001 │
├────────┼────────────┤
│ Marvin │ 18-07-2001 │
╰────────┴────────────╯
```

## Accessing, Setting and deleting.
### Skeletal System of Row and Column
There are some obvious things you should know before using the DataMatrix Module;
In a 2D list can be organized like this; Let us call this assignment of elements as Skeletal system.
```
[
	[<1st Column of 1st Row>,<2nd Column of 1st Row>, ...],
	[<1st Column of 2nd Row>,<2nd Column of 2nd Row>, ...],
	[...],...
]
```
This is needed while setting of elements.

For reference we will be having this DataMatrix;
```
>>> Obj = DataMatrix([['Q','R','S','T'],['U','V','W','X'],['Y','Z','A','B']])
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ R │ S │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
>>> Obj.index = True
>>> print(Obj)
╭─────┬─────┬─────┬─────┬─────╮
│   0 │ 1   │ 2   │ 3   │ 4   │
├─────┼─────┼─────┼─────┼─────┤
│   1 │ Q   │ R   │ S   │ T   │
├─────┼─────┼─────┼─────┼─────┤
│   2 │ U   │ V   │ W   │ X   │
├─────┼─────┼─────┼─────┼─────┤
│   3 │ Y   │ Z   │ A   │ B   │
╰─────┴─────┴─────┴─────┴─────╯
```

### Accessing the elements
#### Accessing an entire row:
Syntax: `<Object>[<Row Index>]`
```
>>> print(Obj[1])
╭───┬───┬───┬───╮
│ Q │ R │ S │ T │
╰───┴───┴───┴───╯
>>> print(Obj[2])
╭───┬───┬───┬───╮
│ U │ V │ W │ X │
╰───┴───┴───┴───╯
```

#### Accessing ranged rows:
Syntax: `<Object>[<Row Slice>]`
```
>>> print(Obj[1:2])
╭───┬───┬───┬───╮
│ Q │ R │ S │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
╰───┴───┴───┴───╯
```

#### Accessing a entire column:
Syntax: `<Object>[:,<Column Index>]`
```
>>> print(Obj[:,1])
╭───╮
│ Q │
├───┤
│ U │
├───┤
│ Y │
╰───╯
```

#### Accessing ranged columns:
Syntax: `<Object>[:, <Column Slice>]`

```
>>> print(Obj[:,1:2])
╭───┬───╮
│ Q │ R │
├───┼───┤
│ U │ V │
├───┼───┤
│ Y │ Z │
╰───┴───╯
```

#### Accessing a ranged rows of single column:
Syntax: `<Object>[<Row Slice>, <Column Index>]`
```
>>> print(Obj[1:2,2])
╭───╮
│ R │
├───┤
│ V │
╰───╯
```

#### Accessing a single row of ranged column:
Syntax: `<Object>[<Row Index>, <Column Index>]`
```
>>> print(Obj[1,2:3])
╭───┬───╮
│ R │ S │
╰───┴───╯
```


#### Accessing ranged rows of ranged columns:
Syntax: `<Object>[<Row Slice>, <Column Slice>]`

```
>>> print(Obj[1:2,2:3])
╭───┬───╮
│ R │ S │
├───┼───┤
│ V │ W │
╰───┴───╯
```

#### Accessing a single cell
Syntax: `<Object>[<Row Index>,<Column Index>]`
```
>>> print(Obj[1,2])
╭───╮
│ R │
╰───╯
```


### Setting of elements
Points to remember in this session:
* You can assign either arrayed values or a scalar value.
* To assign the setter value, those values must follow skeletal assignment.
#### Setting a value for entire entire Row
##### Arrayed Value:
Syntax: `<Object>[<Row Index>] = <Values of dimension 1x(amplitude)>`
```
>>> Obj[1] = [[1,2,3,4]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
##### Scalar Value:
Syntax: `<Object>[<Row Index>] = <Scalar Value>`
```
>>> Obj[1] = 'X'
```

#### Setting a value for ranged Rows
##### Arrayed Value
Syntax: `<Object>[<Row Slice>] = <Values of dimension (Length of Row Slice)x(Amplitude)>`
```
>>> Obj[1:2] = [[1,2,3,4],[5,6,7,8]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

##### Scalar Value
Syntax: `<Object>[<Row Slice>] = <Value>`

```
>>> Obj[1:2] = 'X'
>>> print(Obj)
╭───┬───┬───┬───╮
│ X │ X │ X │ X │
├───┼───┼───┼───┤
│ X │ X │ X │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

#### Setting a value for entire column
##### Arrayed Value
Syntax: `<Object>[:,<Column Index>] = <Values of dimension (Altitude)x1>`
```
>>> Obj[:,1] = [[1],[2],[3]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ R │ S │ T │
├───┼───┼───┼───┤
│ 2 │ V │ W │ X │
├───┼───┼───┼───┤
│ 3 │ Z │ A │ B │
╰───┴───┴───┴───╯
```

##### Scalar Value
Syntax: `<Object>[:,<Column Index>] = <Value>`
```
>>> Obj[:,1] = 'X'
>>> print(Obj)
╭───┬───┬───┬───╮
│ X │ R │ S │ T │
├───┼───┼───┼───┤
│ X │ V │ W │ X │
├───┼───┼───┼───┤
│ X │ Z │ A │ B │
╰───┴───┴───┴───╯
```


#### Setting a value for ranged column
##### Arrayed Value
Syntax: `<Object>[:, <Column Slice>] = <Values of dimension (Altitude)x(Slice length)>`
```
>>> Obj[:,2:3] = [[1,2],[3,4],[5,6]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ 2 │ T │
├───┼───┼───┼───┤
│ U │ 3 │ 4 │ X │
├───┼───┼───┼───┤
│ Y │ 5 │ 6 │ B │
╰───┴───┴───┴───╯
```
##### Scalar Value
Syntax: `<Object>[:, <Column Slice>] = <Value>`
```
>>> Obj[:,2:3] = 1
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ 1 │ T │
├───┼───┼───┼───┤
│ U │ 1 │ 1 │ X │
├───┼───┼───┼───┤
│ Y │ 1 │ 1 │ B │
╰───┴───┴───┴───╯
```

#### Setting a value for ranged rows through a column

##### Arrayed Values
Syntax: `<Object>[<Row Slice>,<Column Index>] = <Values of dimensions (Slice lenth)x1>`
```
>>> Obj[1:2,1] = [[1],[2]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ 1 │ R │ S │ T │
├───┼───┼───┼───┤
│ 2 │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

##### Scalar Value
Syntax: `<Object>[<Row Slice>,<Column Index>] = <Value>`
```
>>> Obj[1:2,1] = 5
>>> print(Obj)
╭───┬───┬───┬───╮
│ 5 │ R │ S │ T │
├───┼───┼───┼───┤
│ 5 │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

#### Setting a value for a row through ranged column
##### Arrayed Value
Syntax: `<Object>[<Row Index>,<Column Slice>] = <Values of dimension (1)x(Slice length)>`

```
>>> Obj[1,2:3] = [[1,2]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ 2 │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
##### Scalar Value
Syntax: `<Object>[<Row Index>,<Column Slice>] = <Value>`
```
>>> Obj[1,2:3] = 0
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 0 │ 0 │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```


#### Setting a value for ranged Row and ranged Column
##### Arrayed Values
Syntax: `<Object>[<Row Slice>,<Column Slice>] = <Values of dimension (Row slice length)x(Column slice length)>`

```
>>> Obj[1:2,2:3] = [[1,2],[3,4]]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ 2 │ T │
├───┼───┼───┼───┤
│ U │ 3 │ 4 │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
##### Scalar Values
Syntax: ``<Object>[<Row Slice>,<Column Slice>] = <Value>`
```
>>> Obj[1:2,2:3] = 1
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ 1 │ T │
├───┼───┼───┼───┤
│ U │ 1 │ 1 │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```


#### Setting a value for a single cell
Syntax: `<Object>[<Row Index>,<Column Index>] = Val`
```
>>> Obj[1,2] = 1
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ 1 │ S │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

#### Setting with DataMatrix Object
The setter value need not to be a list but can also be DataMatrix Object, example:
```
>>> Obj = DataMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
>>> print(Obj)
╭────┬────┬────┬────╮
│  1 │  2 │  3 │  4 │
├────┼────┼────┼────┤
│  5 │  6 │  7 │  8 │
├────┼────┼────┼────┤
│  9 │ 10 │ 11 │ 12 │
├────┼────┼────┼────┤
│ 13 │ 14 │ 15 │ 16 │
╰────┴────┴────┴────╯
>>> Obj2 = DataMatrix([['Q','R','S','T']])
>>> Obj[1] = Obj2
>>> print(Obj)
╭────┬────┬────┬────╮
│ Q  │ R  │ S  │ T  │
├────┼────┼────┼────┤
│ 5  │ 6  │ 7  │ 8  │
├────┼────┼────┼────┤
│ 9  │ 10 │ 11 │ 12 │
├────┼────┼────┼────┤
│ 13 │ 14 │ 15 │ 16 │
╰────┴────┴────┴────╯
```
### Deleting element
You can remove a segment from the DataMatrix using,
#### Deleting a Row
Syntax: `del <Object>[<Row Index>]`
```
>>> del Obj[1]
>>> print(Obj)
╭───┬───┬───┬───╮
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
#### Deleting a ranged Rows
Syntax: `del <Object>[<Row slice>]`
```
>>> del Obj[1:2]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
#### Deleting a Column
Syntax: `del <Object>[<Column Index>]`
```
>>> del Obj[:,1]
>>> print(Obj)
╭───┬───┬───╮
│ R │ S │ T │
├───┼───┼───┤
│ V │ W │ X │
├───┼───┼───┤
│ Z │ A │ B │
╰───┴───┴───╯
```
#### Deleting a ranged Columns
Syntax: `del <Object>[<Column slice>]`
```
>>> del Obj[:,1:2]
>>> print(Obj)
╭───┬───╮
│ S │ T │
├───┼───┤
│ W │ X │
├───┼───┤
│ A │ B │
╰───┴───╯
```
#### Deleting a ranged column through a row
Syntax: `del <Object>[<Row Index>,<Column slice>]`
```
>>> del Obj[1,1:2]
>>> print(Obj)
╭───┬───┬───┬───╮
│   │   │ S │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```
#### Deleting a ranged row through a column
Syntax: `del <Object>[<Row Slice>,<Column Index>]`
```
>>> del Obj[1:2,1]
>>> print(Obj)
╭───┬───┬───┬───╮
│   │ R │ S │ T │
├───┼───┼───┼───┤
│   │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

#### Deleting a ranged row through a ranged column
Syntax: `del <Object>[<Row slice>,<Column Slice>]`
```
>>> del Obj[1:2,2:3]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │   │   │ T │
├───┼───┼───┼───┤
│ U │   │   │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```

#### Deleting a cell
Syntax: `del <Object>[<Row Index>,<Column Index>]`
```
>>> del Obj[1,3]
>>> print(Obj)
╭───┬───┬───┬───╮
│ Q │ R │   │ T │
├───┼───┼───┼───┤
│ U │ V │ W │ X │
├───┼───┼───┼───┤
│ Y │ Z │ A │ B │
╰───┴───┴───┴───╯
```


## Arithmetic Operations
Arithmetic Operation carried out by two DataMatrix Object should be of same dimensions.
Arithmetic Operation can be also carried out by a DataMatrix Object and a scalar value.
In that case, the scalar will applied to every element of the object.

For reference, we will be using these two DataMatrix. 

```
>>> Obj1 = DataMatrix([[1,2,3],[4,5,6],[7,8,9]])
>>> Obj2 = DataMatrix([[15,12,14],[19,20,89],[23,6,90]])
```
### Addition
```
>>> print(Obj1+Obj2)
╭────┬────┬────╮
│ 16 │ 14 │ 17 │
├────┼────┼────┤
│ 23 │ 25 │ 95 │
├────┼────┼────┤
│ 30 │ 14 │ 99 │
╰────┴────┴────╯
>>> print(Obj1+2)
╭───┬────┬────╮
│ 3 │  4 │  5 │
├───┼────┼────┤
│ 6 │  7 │  8 │
├───┼────┼────┤
│ 9 │ 10 │ 11 │
╰───┴────┴────╯
```
### Subtraction
```
>>> print(Obj1-Obj2)
╭─────┬─────┬─────╮
│ -14 │ -10 │ -11 │
├─────┼─────┼─────┤
│ -15 │ -15 │ -83 │
├─────┼─────┼─────┤
│ -16 │   2 │ -81 │
╰─────┴─────┴─────╯
>>> print(Obj1-2)
╭────┬───┬───╮
│ -1 │ 0 │ 1 │
├────┼───┼───┤
│  2 │ 3 │ 4 │
├────┼───┼───┤
│  5 │ 6 │ 7 │
╰────┴───┴───╯
```
### Multiplication
```
>>> print(Obj1*Obj2)
╭─────┬─────┬─────╮
│  15 │  24 │  42 │
├─────┼─────┼─────┤
│  76 │ 100 │ 534 │
├─────┼─────┼─────┤
│ 161 │  48 │ 810 │
╰─────┴─────┴─────╯
>>> print(Obj1*3)
╭────┬────┬────╮
│  3 │  6 │  9 │
├────┼────┼────┤
│ 12 │ 15 │ 18 │
├────┼────┼────┤
│ 21 │ 24 │ 27 │
╰────┴────┴────╯
```

### Division
```
>>> print(Obj1/Obj2)
╭───────────┬──────────┬───────────╮
│ 0.0666667 │ 0.166667 │ 0.214286  │
├───────────┼──────────┼───────────┤
│ 0.210526  │ 0.25     │ 0.0674157 │
├───────────┼──────────┼───────────┤
│ 0.304348  │ 1.33333  │ 0.1       │
╰───────────┴──────────┴───────────╯
>>> print(Obj1/4)
╭──────┬──────┬──────╮
│ 0.25 │ 0.5  │ 0.75 │
├──────┼──────┼──────┤
│ 1    │ 1.25 │ 1.5  │
├──────┼──────┼──────┤
│ 1.75 │ 2    │ 2.25 │
╰──────┴──────┴──────╯
```
### Floor division
```
>>> print(Obj1//Obj2)
╭───┬───┬───╮
│ 0 │ 0 │ 0 │
├───┼───┼───┤
│ 0 │ 0 │ 0 │
├───┼───┼───┤
│ 0 │ 1 │ 0 │
╰───┴───┴───╯
>>> print(Obj1//4)
╭───┬───┬───╮
│ 0 │ 0 │ 0 │
├───┼───┼───┤
│ 1 │ 1 │ 1 │
├───┼───┼───┤
│ 1 │ 2 │ 2 │
╰───┴───┴───╯
```
### Modulus
```
>>> print(Obj1%Obj2)
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 2 │ 9 │
╰───┴───┴───╯
>>> print(Obj1%4)
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 0 │ 1 │
╰───┴───┴───╯
```

## Comparison Operations
Comparison Operation carried out by two DataMatrix Object should be of same dimensions.
Comparison Operation can be also carried out by a DataMatrix Object and a scalar value.
In that case, the scalar will applied to every element of the object.

For reference, we will be using these two DataMatrix. 

```
>>> Obj1 = DataMatrix([[1,2,3],[4,5,6],[7,8,9]])
>>> Obj2 = DataMatrix([[15,12,14],[19,5,89],[23,6,90]])
```
### Equality
```
>>> print(Obj1 == Obj2)
╭───────┬───────┬───────╮
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ True  │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
╰───────┴───────┴───────╯
>>> print(Obj1 == 2)
╭───────┬───────┬───────╮
│ False │ True  │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
╰───────┴───────┴───────╯
```
### Greater Than
```
>>> print(Obj1 > Obj2)
╭───────┬───────┬───────╮
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ True  │ False │
╰───────┴───────┴───────╯
>>> print(Obj1 > 2)
╭───────┬───────┬──────╮
│ False │ False │ True │
├───────┼───────┼──────┤
│ True  │ True  │ True │
├───────┼───────┼──────┤
│ True  │ True  │ True │
╰───────┴───────┴──────╯
```
### Lesser Than
```
>>> print(Obj1 < Obj2)
╭──────┬───────┬──────╮
│ True │ True  │ True │
├──────┼───────┼──────┤
│ True │ False │ True │
├──────┼───────┼──────┤
│ True │ False │ True │
╰──────┴───────┴──────╯
>>> print(Obj1 < 4)
╭───────┬───────┬───────╮
│ True  │ True  │ True  │
├───────┼───────┼───────┤
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
╰───────┴───────┴───────╯
```
### Greater Than or Equal to
```
>>> print(Obj1 >= Obj2)
╭───────┬───────┬───────╮
│ False │ False │ False │
├───────┼───────┼───────┤
│ False │ True  │ False │
├───────┼───────┼───────┤
│ False │ True  │ False │
╰───────┴───────┴───────╯
>>> print(Obj1 >= 4)
╭───────┬───────┬───────╮
│ False │ False │ False │
├───────┼───────┼───────┤
│ True  │ True  │ True  │
├───────┼───────┼───────┤
│ True  │ True  │ True  │
╰───────┴───────┴───────╯
```
### Lesser Than or Equal to
```
>>> print(Obj1 <= Obj2)
╭──────┬───────┬──────╮
│ True │ True  │ True │
├──────┼───────┼──────┤
│ True │ True  │ True │
├──────┼───────┼──────┤
│ True │ False │ True │
╰──────┴───────┴──────╯
>>> print(Obj1 <= 4)
╭───────┬───────┬───────╮
│ True  │ True  │ True  │
├───────┼───────┼───────┤
│ True  │ False │ False │
├───────┼───────┼───────┤
│ False │ False │ False │
╰───────┴───────┴───────╯
```
### Not equal to
```
>>> print(Obj1 != Obj2)
╭──────┬───────┬──────╮
│ True │ True  │ True │
├──────┼───────┼──────┤
│ True │ False │ True │
├──────┼───────┼──────┤
│ True │ True  │ True │
╰──────┴───────┴──────╯
>>> print(Obj1 != 4)
╭───────┬──────┬──────╮
│ True  │ True │ True │
├───────┼──────┼──────┤
│ False │ True │ True │
├───────┼──────┼──────┤
│ True  │ True │ True │
╰───────┴──────┴──────╯
```

## Bool value
`bool(<DM-Object>)` will return `True` if all the elements are `True`, or having the value `True`, else return `False`.

```
>>> Obj = DataMatrix([[True, True],[True, True]])
>>> bool(Obj)
True
>>> Obj = DataMatrix([[True, False],[True, True]])
>>> bool(Obj)
False
```
## Length parameter
Here is the axis part comes in,
The length attribute differs on the axis, that is.
```
>>> Obj = DataMatrix([[1,2,3],[4,5,6]])
>>> print(Obj)
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
╰───┴───┴───╯
>>> Obj.axis = 1
>>> Obj.__len__()
2
>>> Obj.axis = 0
>>> Obj.__len__()
3
```
The axis `1`, represents the rows and the axis `0` represent the columns.
That is
* When the axis is `1`,length param will give you number of rows, that is `Altitude`.
* When the axis is `0`,length param will give you number of columns, that is `Amplitude`.

## Transpose
It is just transposing the grid.
```
>>> Obj = DataMatrix([[1,2,3],[4,5,6]])
>>> print(Obj.transpose)
╭───┬───╮
│ 1 │ 4 │
├───┼───┤
│ 2 │ 5 │
├───┼───┤
│ 3 │ 6 │
╰───┴───╯
>>> print(Obj)
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
╰───┴───┴───╯
```
## Applying functions
You can apply a specific function to all the elements in the DataMatrix, as example:
```
>>> Obj = DataMatrix([[1,2,3],[4,5,6]])
>>> from math import sin
>>> print(Obj.apply(sin))
╭───────────┬───────────┬───────────╮
│  0.841471 │  0.909297 │  0.14112  │
├───────────┼───────────┼───────────┤
│ -0.756802 │ -0.958924 │ -0.279415 │
╰───────────┴───────────┴───────────╯

```

## Append, Insert
### Append
Append is used to add a DataMatrix to a another DataMatrix.
In this case the axis is set to 1
```
>>> Obj1 = DataMatrix([[1,2,3],[4,5,6]])
>>> Obj2 = DataMatrix([[2,3,4],[5,6,7]])
>>> Obj1.axis = 1
>>> Obj1.append(Obj2)
>>> print(Obj1)
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 2 │ 3 │ 4 │
├───┼───┼───┤
│ 5 │ 6 │ 7 │
╰───┴───┴───╯
```

In this case the axis is set to 0
```
>>> Obj1 = DataMatrix([[1,2,3],[4,5,6]])
>>> Obj2 = DataMatrix([[2,3,4],[5,6,7]])
>>> Obj1.axis = 0
>>> Obj1.append(Obj2)
>>> print(Obj1)
╭───┬───┬───┬───┬───┬───╮
│ 1 │ 2 │ 3 │ 2 │ 3 │ 4 │
├───┼───┼───┼───┼───┼───┤
│ 4 │ 5 │ 6 │ 5 │ 6 │ 7 │
╰───┴───┴───┴───┴───┴───╯
```

**Note:
* If you have axis 1, then the appending object must have same `amplitude` with the one you're appending with.
* If you have axis 0, then the appending object must have same `altitude`, with the one you're appending with.
### Insert
Syntax: `<DM-Object>.insert(<Index>, <Other DM-Object>)`

**On axis 1**
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj2 = DataMatrix([[6,7],[8,9]])
>>> Obj1.insert(2,Obj2)
>>> print(Obj1)
╭───┬───╮
│ 1 │ 2 │
├───┼───┤
│ 6 │ 7 │
├───┼───┤
│ 8 │ 9 │
├───┼───┤
│ 3 │ 4 │
╰───┴───╯
```

**On axis 0**
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj2 = DataMatrix([[6,7],[8,9]])
>>> Obj1.axis = 0
>>> Obj1.insert(2, Obj2)
>>> print(Obj1)
╭───┬───┬───┬───╮
│ 1 │ 6 │ 7 │ 2 │
├───┼───┼───┼───┤
│ 3 │ 8 │ 9 │ 4 │
╰───┴───┴───┴───╯
```

## Representation
The DataMatrix Is represented as
```
>>> Obj = DataMatrix([[1,2],[3,4]])
>>> Obj
DataMatrix(2x2)
```
## Raw
`__raw__` method will return you the raw 2D array
```
>>> Obj = DataMatrix([[1,2],[3,4]])
>>> Obj.__raw__
[[1, 2], [3, 4]]
```

# Errors

## Error #1
When you Add, subtract, or do any arithmetic or comparison operation between any two DataMatrix object, both the objects have to be in same dimension, or else will raise error:
Let us say we add Objects of dimension `3x4` and `1x4`
Then this error will be raised, flagged as `Error #1`

```
>>> Obj1 = DataMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]
... )
>>> Obj2 = DataMatrix([[1,2,3,4]])
>>> print(Obj1+Obj2)
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    print(Obj1+Obj2)
          ~~~~^~~~~
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 269, in __add__
    def __add__(self, Val):return DataMatrix(Comp_Operators(self, Val, '+'))
                                             ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 69, in Comp_Operators
    if other_instance.dim != instance.dim: raise ValueError(f'[Error #1] To opertions to carry, both the Object should have same dimension, but rather different here; {instance.dim} and {other_instance.dim}')
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: [Error #1] To opertions to carry, both the Object should have same dimension, but rather different here; 3x4 and 1x4
```
## Error #2
When you try to convert a illegal array to a DataMatrix, you will get this error
```
>>> Obj1 = DataMatrix([[1,2,3],[5,6],[7]])
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    Obj1 = DataMatrix([[1,2,3],[5,6],[7]])
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 84, in __init__
    raise ValueError('[Error #2] Illegally nested array.')
ValueError: [Error #2] Illegally nested array.
```
Here I have tried with `[[1,2,3],[5,6],[7]]`, but gave rise to error flagged as `Error #2`

## Error #3
This is an `TypeError` occurs when the `headers` attribute is not given as list.
```
>>> Obj1.headers = 5
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    Obj1.headers = 5
    ^^^^^^^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 102, in headers
    raise TypeError(f'[Error #3] The headers argument must be a \'list\', but rather given as {type(val).__name__}.')
TypeError: [Error #3] The headers argument must be a 'list', but rather given as int.
```
## Error #4
This Error occurs when the headers argument is not in the length of the amplitude of the array;
In the example below, the amplitude of the array is 2.
```
>>> Obj1.headers = [1,2,3]
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    Obj1.headers = [1,2,3]
    ^^^^^^^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 104, in headers
    raise ValueError(f'[Error #4] Length of header should be same as the amplitude of the array!, the length of th headers are in {len(val)}.')
ValueError: [Error #4] Length of header should be same as the amplitude of the array!, the length of the headers are in 3.
```

## Error #5
This error occurs when the index is set to neither of True or False, but has to be a Boolean value.
```
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    Obj1.index = 5
    ^^^^^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 113, in index
    raise TypeError(f'[Error #5] The index argument must be a \'boolean\', but rather given as {type(val).__name__}.')
TypeError: [Error #5] The index argument must be a 'boolean', but rather given as int.
```

## Error #6
This error occurs when the axis is neither set `0` or `1`.
```
>>> Obj1.axis = 5
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    Obj1.axis = 5
    ^^^^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 122, in axis
    raise ValueError(f'[Error 6] The axis must be either 1 or 0; given as {val}.')
ValueError: [Error 6] The axis must be either 1 or 0; given as 5.
```

## Error #7
This nothing but index error when trying to get an item
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj1[3]
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    Obj1[3]
    ~~~~^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 174, in __getitem__
    if Error_occured: raise IndexError(f'[Error #7] The provided is index is either out of range or illegal for the given array; provided index:{index}.')
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: [Error #7] The provided is index is either out of range or illegal for the given array; provided index:3.
```

## Error #8
This error is raised when your setter value is in illegal dimensions
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj1[2] = [[1,2,3]]
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    Obj1[2] = [[1,2,3]]
    ~~~~^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 216, in __setitem__
    else: raise ValueError(f'[Error #8] The dimensions of the setter value is illegal for the index {index}, required:{self.amp}x1.')
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: [Error #8] The dimensions of the setter value is illegal for the index 2, required:2x1.
```

## Error #9
This error is same as `Error #7`, but when setting a value.
```
>>> Obj1[3] = [['Q','R']]
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    Obj1[3] = [['Q','R']]
    ~~~~^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 229, in __setitem__
    if Error_occured: raise IndexError(f'[Error #9] The provided is index is either out of range or illegal for the given array; provided index:{index}.')
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: [Error #9] The provided is index is either out of range or illegal for the given array; provided index:3.
```

## Error #10
This error is same as `Error #7`, but when deleting a value.
```
>>> del Obj1[3]
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    del Obj1[3]
        ~~~~^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 264, in __delitem__
    if Error_occured: raise IndexError(f'[Error #10] The provided is index is either out of range or illegal for the given array; provided index:{key}.')
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: [Error #10] The provided is index is either out of range or illegal for the given array; provided index:3.
```

## Error #11
This error is raised when appending a non DataMatrix Object to a DataMatrix Object
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj2 = [[5,6],[7,8]]
>>> Obj1.append(Obj2)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    Obj1.append(Obj2)
    ~~~~~~~~~~~^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 295, in append
    if not isinstance(val, DataMatrix):raise TypeError('[Error #11] The value you going to append but be also a DataMatrix Object.')
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: [Error #11] The value you going to append but be also a DataMatrix Object.
```

## Error #12
This error is raised when the amplitude is not matched with the DataMatrix you're appending with while the axis is equal to 1.
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj2 = DataMatrix([[5,6,'q'],[7,8,'r']])
>>> Obj1.axis = 1
>>> Obj1.append(Obj2)
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    Obj1.append(Obj2)
    ~~~~~~~~~~~^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 297, in append
    if self.amp != val.amp:raise ValueError('[Error #12] The amplitude of the main array and the ampliude of appending array is not equal')
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: [Error #12] The amplitude of the main array and the ampliude of appending array is not equal
```

## Error #13
This error is raised when the altitude is not matched with the DataMatrix you're appending with while the axis is equal to 0,
```
>>> Obj1 = DataMatrix([[1,2],[3,4]])
>>> Obj2 = DataMatrix([[5,6],[7,8],[9,10]])
>>> Obj1.axis = 0
>>> Obj1.append(Obj2)
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    Obj1.append(Obj2)
    ~~~~~~~~~~~^^^^^^
  File "/mnt/d/PYDB/Pydb-core/pydb_.py", line 300, in append
    if self.alt != val.alt:raise ValueError('[Error #13] The altitude of the main array and the altitude of appending array is not equal')
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: [Error #13] The altitude of the main array and the altitude of appending array is not equal
```

## Error #14
Same as `Error 11`, but while inserting

## Error #15
Same as `Error 12`, but while inserting

## Error #16
Same as `Error 13`, but while inserting

## Error #17
While inserting, if the index is out of range or illegal for the array, this error is raised.

# Finally.

If you have read this entire document, thank you very much. Also, this DataMatrix program is still in development and want to achieve even more complex situation, please be patient until that. Your issues and your recommendation are really welcomed. Thank you.

