# Contributing to Smart Manager

Welcome to Smart Manager! We appreciate your interest in contributing.

## How to Contribute

1. **Fork the repository:** Click on the "Fork" button on the top right corner of the repository page. This creates a copy of the repository in your GitHub account.

2. **Clone your fork:** Clone the forked repository to your local machine. Replace `YourUsername` with your GitHub username:

   ```bash
   git clone https://github.com/YourUsername/Smart_Manager.git
   ```

3. **Create a new branch:** Create a new branch for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes:** Implement your feature or fix.

5. **Test your changes:** Ensure your changes do not break existing functionality. If applicable, add relevant tests to cover your changes.

6. **Commit your changes:** Commit your changes with a descriptive message:

   ```bash
   git commit -m 'Add your feature'
   ```

7. **Push to your branch:** Push your changes to your GitHub repository:

   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a pull request:** On the GitHub page of your fork, create a pull request. Provide details about your changes and submit the pull request.

## Reporting Issues

If you encounter any issues or have suggestions, please [create an issue](https://github.com/JeelDobariya38/smart-manager/issues) on GitHub. Ensure to provide detailed information about the problem and steps to reproduce it.

## Code Style

Follow the code style used in the project. Use consistent indentation and formatting. If you are unsure, refer to the existing codebase.

## Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Running the Smart Manager App Locally

To run the Smart Manager app locally, use the provided Python script. Make sure you have Python installed and you are at the root of repository, then execute:

```bash
python src/main.py
```

## Contributing Code

If you wish to contribute code, make sure to follow the coding conventions and include relevant tests.

### Example Code

Below is an example Python script. Feel free to provide your feedback or contribute to give repository a better styling:

```python
def greet(name: str) -> None:
    message = f"Hello, {name}!"
    print(message)

def calculate_sum(a: int | float, b: int | float) -> int | float:
    result = a + b
    return result

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = calculate_sum(num1, num2)
    print(f"The sum is: {total}")

```

**Here are some key elements that you can remember while coding in this codebase**

1. **Indentation:**
   - The code uses 4 spaces for indentation, which is a common and widely accepted convention in Python. Stick to this for consistency.

2. **Whitespace:**
   - The code has consistent spacing around operators and after commas, which is good. Continue to maintain this consistency.

3. **Imports:**
   - The imports are organized and follow the standard Python style. Make sure to group your imports and have a clear separation between standard library imports and third-party imports.
   
   - third-part imports should be on the top that a balk line and the other built in module should imported.

4. **Function and Method Naming:**
   - Function and method names are in lowercase with words separated by underscores (`snake_case`), which is the recommended convention in Python.

5. **Use of Type Hints:**
   - Good use of type hints! Continue to provide type hints for function arguments and return types, as this enhances code readability.

Remember, these are general guidelines, and the most important thing is to maintain consistency within the codebase.

## Feature Suggestions

If you have ideas for new features or improvements, please feel free to discuss them in the [GitHub Discussions](https://github.com/JeelDobariya38/smart-manager/discussions) section.

Thank you for contributing to Smart Manager!
