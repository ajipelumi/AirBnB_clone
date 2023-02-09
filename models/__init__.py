#!/usr/bin/python3
""" Creates a unique FileStorage instance for our application. """
from models.engine.file_storage import FileStorage


# Create variable
storage = FileStorage()

# Call reload() method
storage.reload()
