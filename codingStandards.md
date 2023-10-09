# Coding Standard
The coding standards for this project follows the guidelines in python's [PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names). This document will cover only sections considered to be crucial in maintaining the consistency of code throughout the project. If more clarification is needed referring to the [PEP 8's](https://peps.python.org/pep-0008/#function-and-variable-names) official documentation is advised.

## [Code Lay-out](https://peps.python.org/pep-0008/#code-lay-out)

### [Indentation](https://peps.python.org/pep-0008/#indentation)

Use 4 spaces per indentation level.

### [Maximum Line Length](https://peps.python.org/pep-0008/#maximum-line-length)

Limit all lines to a maximum of 79 characters.

## [Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

### [Constants](https://peps.python.org/pep-0008/#constants)

Constants must be in uppercase. Words are separated by an underscore.

Example: `MAX_OVERFLOW`

### [Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names)

Function and variable names must be all lowercase. Words separated by an underscore.

```python 3
# Example
def print_names()
    pass
	
first_name = "first name"
```
### [Method Names and Instance Variables](https://peps.python.org/pep-0008/#method-names-and-instance-variables)

[Use the function naming rules](#function-and-variable-names): names must be all lowercase. Words separated by an underscore.

Public methods must not start with an underscore.

Note: there is some controversy about the use of __names (see below).
### [Function and Method Arguments](https://peps.python.org/pep-0008/#function-and-method-arguments)

 `self`  must be the first argument in instance methods.
 
`cls`  must be the first argument in class methods.

### [Class Names](https://peps.python.org/pep-0008/#class-names)

Class names use the CapsWords style, capitalized at only the first letter of each word and. Words are not separated.

```python 3
# Example
class MovieStars:
    pass
```

### [Package and Module Names](https://peps.python.org/pep-0008/#package-and-module-names)

Module names must be all-lowercase. Use underscores to sperate words. Refrain for using long names.

Packages names all-lowercase names. No characters should be used to sperate words. Package names should also be concise.

## [Comments](https://peps.python.org/pep-0008/#comments)

Comments should use proper English. Comments for code that requires a lot of explaining should use full sentences.

### [Block Comments](https://peps.python.org/pep-0008/#block-comments)

Use block comments to explain a group of code following it.

Each line of the block is preceded by a `#` followed by whitespace and are indented to the same level as code it explains.

```python 3
def example_function(X, y):
	# This comment should explain the group of code below.
	for x in X:
		if x == y:
			print(f"Found {y}!")
	print(f"{y} not found")
```

### [Inline Comments](https://peps.python.org/pep-0008/#inline-comments)

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a `#` and a single space.

Use inline comments sparingly, only when the line is obscure to explain the intention of that line. Don't point out the obvious.

Good usage:
```python 3
x = x + 1                 # Compensate for border
```
Bad usage:
```python 3
x = x + 1                 # Increment x
```
### [Documentation Strings](https://peps.python.org/pep-0008/#documentation-strings)
 
Documentation strings or docstrings are explanations attributed to a code component (i.e. modules, functions, classes, and methods). Docstrings must be included for all public components. For further details refer to [PEP 257](https://peps.python.org/pep-0257/ "PEP 257 – Docstring Conventions").

Docstrings must start with a one-line summary explaining of what the component does. One blank line must come after the summary.

Docstrings must be the first line within the documented code component. For classes, methods, and functions this means docstrings start the line after name is declared.

#### Function and Methods Docstrings

Must contain and explain the following in order, unless the function/method doesn't contain them:
1. Summary
2. Arguments
3. Return value
4. Exceptions

The summary should note the behavior and how to use the function/methods. All arguments, return values, and exceptions should be briefly explained. 

#### Classes Docstrings

Must contain the following in order, unless the class doesn't contain them:
1. Summary
2. List of public:
	1. Methods
	3. Class variables
	2. Instance variables

Only the class variables have to be explained in the class variables. Public methods and instance variables only need to be listed in the class docstring. Details on the methods should be in their respective docstrings, and instance variables in the `__new__` or  `__init__` methods where they are initialized.

#### Module Docstrings
Must contain the following in order, unless the module doesn't contain them:
1. Summary
2. List of public:
	1. Classes
	3. Functions

## [Whitespace in Expressions and Statements](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)

### Brackets

***Note:*** bracket is used here as a general term for refer to parenthesis "()", square brackets "[]", and curly braces "{}".

#### Space Within Brackets

The code after the opening bracket and before the closing bracket must be adjacent the brackets, no space in between. For example: 
```python 3 
# Correct:
spam(ham[1], {eggs: 2})
```
```python 3 
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
```
#### Space Before Brackets

Functions names must not be spaced from the parenthesis holing the arguments.

The brackets used for indexing for slicing must not be spaced from the variable name as well.
```python 3 
# Correct:
spam(1)
dct['key'] = lst[index]
```
```python 3 
# Wrong:
spam (1)
dct ['key'] = lst [index]
```

### Commas, Semicolons, and Colons

Commas, semicolons and colons must be spaced only after it. With two exceptions that don't have any space around them. 
Exceptions: 
1.  [when colons are used in splicing](#exception-1-colons-for-splicing)
2. [trailing commas in parenthesis](#exception-2-trailing-commas)
```python 3 
# Correct:
if x == 4: print(x, y); x, y = y, x
```
```python 3 
# Wrong:
if x == 4 : print(x , y) ; x , y = y , x
```
#### Exception 1: Colons for Splicing

However, when splicing, colons must be spaced equally on both sides and follows the spacing rules of a [binary operator](#binary-operators) of lowest priority. 

#### Exception 2: Trailing Commas
Use trailing commas only when necessary, i.e. single element tuple.

### Binary Operators

All binary operators must have an equal amount of space on both sides either 0 or 1.

The following binary operators must always have one space on both sides:
- Augmented Assignment (`+=`, `-=` etc.)
- Comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not  in`, `is`, `is  not`)
- Booleans (`and`, `or`, `not`)

The assignment operator (`=`) follows this for all cases except when used to indicate keyword arguments *where the type is not specified*. No space is used for this case.
```python 3
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
    
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```
```python 3
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
    
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```
When dealing with different levels of priority the higher the priority the less space surrounding the binary operator but no more than one on either side.
```python 3
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
```python 3
# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```
### Function Annotation

The colons for argument type specification follows the general standard for [colons](#commas-semicolons-and-colons).

The return type specifier `->` must have one space on both sides.
```python 3
# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```
```python 3
# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```
