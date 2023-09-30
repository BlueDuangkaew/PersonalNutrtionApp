# Coding Standard
The coding standards for this project follows the guidelines in [python's pep 8](https://peps.python.org/pep-0008/#function-and-variable-names).

## Naming Conventions


### [Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names)

Names should be all lowercase. Words separated by underscores.
```python 3
# Example
def print_names()

first_name = "first name"
```
### [Method Names and Instance Variables](https://peps.python.org/pep-0008/#method-names-and-instance-variables)

[Use the function naming rules](###Function-and-Variable-Names): lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named  `__a`, it cannot be accessed by  `Foo.__a`. (An insistent user could still gain access by calling  `Foo._Foo__a`.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).
### [Function and Method Arguments](https://peps.python.org/pep-0008/#function-and-method-arguments)

>Always use  `self`  for the first argument to instance methods.
>Always use  `cls`  for the first argument to class methods.
