# Common Code General Template

In this document, you will find common code snippets and best practices that are essential throughout your codebase.

## Purpose

The purpose of this document is to provide guidance on the use of common code practices and to ensure consistency across all modules within your project.

## Inclusion in Support Scripts/Modules

It is recommended to include the following code snippet at the end of every support script or module. This code serves as a reminder to users or script runners that the module is not meant to be run directly and instructs them to execute the `main.py` script to launch the application.

```python
if __name__ == "__main__":
    input("This script is not intended to be run directly. Please run 'main.py' to start the application.")
```
