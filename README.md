# CSE251 Library
The package that contains common classes for the CSE 251 course.

It provides:
* setting the current working directory
* convenient logging to stdout and file
* load json files
* provides plot support from matplotlib

Using pip has the following advantages:
* more flexible running experience (working directory)
* includes Intellisense instead of showing unknown function
* able to be updated without modifying other repositories

## Instructions

Run in the console
```bash
python -m install https://github.com/yeskindofday/cse251-library.git
```

And to use it

```python
from cse251 import *
set_working_directory(__file__)
```