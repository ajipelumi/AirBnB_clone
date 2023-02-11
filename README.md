<img src="https://github.com/ajipelumi/AirBnB_clone/blob/e5f82d5734c63db477609b57303de523e75837cd/images/hbnb.png" alt="hbnb logo" width="400">
Image Credit: ALX Africa

##

**The AirBnB Clone**

The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.com/).

Only some features of the website will be implemented to cover all fundamental concepts of the higher level programming track.
The web application will be composed of:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and our data (retrieve, create, delete, update them).

## Command Interpreter
Our command interpreter is the first part of the AirBnB clone. It is like a shell and it will help us manage objects.

Our shell would work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Files and Directories
- `models` directory contains all classes used for the entire project.
- `tests` directory contains all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - attributes: `id`, `created_at` and `updated_at`
  - methods: `save()` and `to_dict()`
- `models/engine` directory contains all storage classes.
