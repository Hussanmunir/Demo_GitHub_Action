# GitHub Actions Workflow for Calculator Functions

This repository demonstrates how to set up a GitHub Actions workflow to automate testing for a simple calculator application using Pytest. The workflow ensures that all test cases pass before merging any pull request.

## Features

- **Trigger**: The workflow runs on every pull request to the `main` branch.
- **Test Framework**: Uses Pytest to validate the functionality of the calculator.
- **Merge Restriction**: Code cannot be merged unless all tests pass.
- **Code Owner Approval**: Only the code owner can merge pull requests.

## File Structure

```
Demo_GitHub_Action/
    calculator.py          # Contains the Calculator class with basic mathematical operations
    LICENSE                # License information for the project
    README.md              # Documentation for the project
    test_calculator.py     # Pytest test cases for the Calculator class
    .github/workflows/pytest.yml  # GitHub Actions workflow configuration for running Pytest
```

## Requirements

- Python 3.8 or higher
- `pytest` (install using `pip install pytest`)

## How to Run Tests Locally

1. Install dependencies:

   ```bash
   pip install pytest
   ```
2. Run tests:

   ```bash
   pytest -v
   ```

## Example Output of Running Tests

When you run the tests using the `pytest -v` command, you will see an output similar to the following:

```
====================================== test session starts ======================================
platform win32 -- Python 3.12.5, pytest-8.3.5, pluggy-1.5.0 -- C:\Users\al6171\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\al6171\Box\Demo_Code_Workspace
plugins: cov-6.1.1
collected 12 items                                                                              

Demo_GitHub_Action/test_calculator.py::TestCalculator::test_add PASSED                     [  8%]
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_add_negative PASSED            [ 16%] 
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_subtract PASSED                [ 25%] 
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_subtract_negative PASSED       [ 33%] 
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_multiply PASSED                [ 41%] 
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_multiply_negative PASSED       [ 50%] 
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_divide PASSED                  [ 58%]
Demo_GitHub_Action/test_calculator.py::TestCalculator::test_divide_by_zero PASSED          [ 66%] 
Demo_UnitTest_Python/test_math_functions_pytest.py::test_add PASSED                        [ 75%] 
Demo_UnitTest_Python/test_math_functions_pytest.py::test_subtract PASSED                   [ 83%] 
Demo_UnitTest_Python/test_math_functions_pytest.py::test_multiply PASSED                   [ 91%] 
Demo_UnitTest_Python/test_math_functions_pytest.py::test_divide PASSED                     [100%] 

====================================== 12 passed in 0.82s ======================================= 
```

This output indicates that all test cases have passed successfully.

## How to Make a Pull Request

1. **Create a New Branch**:

   - Before making changes, create a new branch from the `main` branch.

   ```bash
   git checkout -b your-branch-name
   ```
2. **Make Changes**:

   - Add or modify files as needed.
3. **Commit Changes**:

   - Commit your changes with a meaningful message.

   ```bash
   git add .
   git commit -m "Your commit message"
   ```
4. **Push Changes**:

   - Push your branch to the remote repository.

   ```bash
   git push origin your-branch-name
   ```
5. **Create a Pull Request**:

   - Go to the repository on GitHub.
   - Click on the "Pull Requests" tab.
   - Click "New Pull Request" and select your branch.
   - Add a description and submit the pull request.

## Where to See Triggered Test Cases

- Once the pull request is created, the GitHub Actions workflow will automatically run the test cases.
- Navigate to the "Actions" tab in your GitHub repository to view the status of the triggered tests.
- You can also see the test results directly in the pull request under the "Checks" section.

## How to Use

1. **Create a Pull Request**: Push your changes to a new branch and create a pull request.
2. **Run Tests**: The workflow will automatically run all Pytest test cases.
3. **Review Results**: Ensure all tests pass. If any test fails, fix the issues and push the changes.
4. **Approval and Merge**: The code owner reviews and merges the pull request if all tests pass.
