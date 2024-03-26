# Contributing to Smart Manager

Welcome to the Smart Manager project! We greatly value your interest in contributing to this endeavor.

## How to Contribute

1. **Fork the Repository:** Begin by clicking the "Fork" button located in the upper right corner of the repository's page. This action creates a duplicate of the repository within your GitHub account.

2. **Clone Your Fork:** Clone the forked repository to your local machine. Replace `YourUsername` with your GitHub username:

   ```bash
   git clone https://github.com/YourUsername/Smart_Manager.git
   ```

3. **Create a New Branch:** Create a new branch for your contributions:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes:** Implement your feature or fix.

5. **Test Your Changes:** Ensure that your modifications do not disrupt current functionality. If applicable, add pertinent tests to cover your changes.

6. **Commit Your Changes:** Commit your changes along with a descriptive message:

   ```bash
   git commit -m 'Add your feature'
   ```

7. **Push to Your Branch:** Push your changes to your GitHub repository:

   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request:** On the GitHub page of your fork, create a pull request. Provide comprehensive details about your changes and proceed to submit the pull request.

## Reporting Issues

If you come across any issues or have suggestions for improvement, kindly [create an issue](https://github.com/JeelDobariya38/Smart-Manager/issues) on GitHub. Ensure to provide meticulous information about the problem and steps to reproduce it.

## Code Style

Maintain consistency with the code style employed in the project, including uniform indentation and formatting. When in doubt, refer to the existing codebase for guidance.

<!-- ## Code of Conduct

Please be mindful that this project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold these principles. -->

## Running the Smart Manager App Locally

To run the Smart Manager app on your local environment, employ the provided Python script. Ensure Python is installed and that you are in the repository's root directory, then execute:

```bash
python SmartManager/main.py
```

## Contributing Code

For code contributions, adhere to the coding conventions and encompass relevant tests.

### Example Code

Here is an example Python script. Feel free to provide your feedback or contribute to enhance the repository's style:

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

**Notable Code Elements for Reference**

1. **Indentation:**
   - Consistently use 4 spaces for indentation, a widely accepted convention in Python, to maintain uniformity.

2. **Whitespace:**
   - Ensure consistency in spacing around operators and after commas, as observed in the existing codebase.

3. **Imports:**
   - Organize imports and follow the standard Python style. Group third-party imports at the top, preceded by a blank line, followed by built-in module imports.

4. **Function and Method Naming:**
   - Keep function and method names in lowercase with words separated by underscores (`snake_case`), in adherence to Python's recommended convention.

5. **Use of Type Hints:**
   - Continue using type hints for function arguments and return types to enhance code clarity and maintain readability.

Remember, these guidelines are flexible, with the primary emphasis on maintaining consistency within the codebase.

## Feature Suggestions

Should you possess ideas for new features or improvements, we encourage you to discuss them in the [GitHub Discussions](https://github.com/JeelDobariya38/Smart-Manager/discussions) section.

Thank you for your valuable contributions to Smart Manager!
