# Coding Standard
The coding standards for this project follows the guidelines in [python's pep 8](https://peps.python.org/pep-0008/#function-and-variable-names). This document will cover only sections considered to be crucial in maintaining the consistency of code throughout the project. If more clarification is needed referring to the [pep 8's](https://peps.python.org/pep-0008/#function-and-variable-names) official documentation is advised.

## [Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

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

### [Constants](https://peps.python.org/pep-0008/#constants)

Constants must be in uppercase. Words are separated by an underscore.

Example: `MAX_OVERFLOW`

## [Whitespace in Expressions and Statements](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)

### Spacing Inside Brackets

The code after the opening bracket and before the closing bracket must be adjacent the brackets, no space in between. For example: 
```python 3 
def print_names(
```

Undecided
