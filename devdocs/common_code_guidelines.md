# Common Code Best Practices

This document serves as a guide to uphold common coding best practices, fostering consistency and clarity throughout every module within our project.

## Purpose

The purpose of this document is to establish a framework for excellence in coding practices, elevating the quality and maintainability of our codebase.

## Incorporating Support Scripts/Modules

We strongly recommend the inclusion of the following code snippet at the beginning of each support script or module. This practice not only serves as a gentle reminder but also contributes to a well-structured project hierarchy.

```python
# Ensure that this code follows any imports statements


if __name__ == "__main__":
    print("This script is not intended for direct execution,")
    input("Please use 'main.py' to launch the application.")
    quit()


# Include any other supporting functions, classes, or constants below this line.
```

## Simulating Input for Testing

In the context of testing code reliant on standard input (stdio) functions, the integration of the `pytest` testing framework, coupled with the `monkeypatch` fixture, can replicate input values effectively.

```python
def test_function_using_stdio_input():
    input_values = ['mocked_input_1', 'mocked_input_2', 'mocked_input_3']
    
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    
    result = your_function()
    
    assert result == expected_result
```

## Testing Console Output

For verifying console output during testing, the `pytest` framework provides the `capfd` fixture. You can use it to capture and assert the printed output.

```python
def test_console_output(capfd):
    your_function_to_print_to_console()
    
    # Capture the printed output.
    out, _ = capfd.readouterr()
    
    # Assert the content you expect to be printed.
    assert "Expected output text" in out
```

## Testing Code with Input and Output

When testing code that depends on both standard input (stdio) and console output, you can combine the usage of `pytest`, the `monkeypatch` fixture for input, and the `capfd` fixture for capturing console output.

```python
def test_function_using_stdio_input_and_console_output(monkeypatch, capfd):
    input_values = ['mocked_input_1', 'mocked_input_2', 'mocked_input_3']
    
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    
    result = your_function()
    
    # Capture the printed output.
    out, _ = capfd.readouterr()
    
    # Assert the content you expect to be printed.
    assert "Expected output text" in out
    
    assert result == expected_result
```
