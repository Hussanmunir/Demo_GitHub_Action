# GitHub Actions Workflow for Calculator Functions

This repository demonstrates how to set up a complete **CI/CD pipeline** using GitHub Actions with automated testing and deployment stages. The workflow validates code on pull requests (CI), then deploys to staging and production environments after merge (CD).

## Features

- **CI Phase**: Automated tests run on every pull request to validate code before merge
- **CD Phase**: Automated deployment to staging and production environments on merge
- **Test Framework**: Uses Pytest to validate the functionality of the calculator
- **Deployment Pipeline**: Sequential deployment to staging → production with dependency gates
- **Merge Restriction**: Code cannot be merged unless all tests pass
- **Code Owner Approval**: Only the code owner can merge pull requests

## File Structure

```
Demo_GitHub_Action/
    calculator.py              # Contains the Calculator class with basic mathematical operations
    test_calculator.py         # Pytest test cases for the Calculator class
    requirements.txt           # Python dependencies (pytest)
    LICENSE                    # License information for the project
    README.md                  # Documentation for the project
    .github/workflows/pytest.yml  # GitHub Actions workflow configuration for CI/CD pipeline
```

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## How to Run Tests Locally

1. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
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

## CI/CD Pipeline Overview

The workflow consists of **4 jobs** that run automatically:

### **CI Phase (Continuous Integration)**
- **Job 1 — Build & Test**: Runs on every pull request
  - Validates code by running all tests
  - Ensures code quality before merge
  - Blocks merge if tests fail

### **CD Phase (Continuous Deployment)**
- **Job 2 — Ready for Deployment**: Notifies after merge to main
- **Job 3 — Deploy to Staging**: Deploys to staging environment
  - Tests performance, configuration, and security
  - Acts as a pre-production environment
- **Job 4 — Deploy to Production**: Deploys to production **after staging succeeds**
  - Only runs if staging deployment is successful
  - Ensures code has been tested in staging first

**Workflow Flow:**
```
Pull Request → Run Tests (CI) → Merge to main → Deploy Staging → Deploy Production (CD)
```

## How to Fork the Repository

Forking creates a personal copy of the repository under your GitHub account. Follow these steps:

1. **Navigate to the Repository**:
   - Go to the main repository page on GitHub.

2. **Click the Fork Button**:
   - In the top-right corner of the page, click the **Fork** button.
   - This will create a copy of the repository under your GitHub account.

3. **Wait for the Fork to Complete**:
   - GitHub will redirect you to your forked repository once the process is complete.
   - You should now see your username in the repository path (e.g., `your-username/Demo_GitHub_Action`).

4. **Clone Your Forked Repository**:
   - Copy the HTTPS or SSH URL of your forked repository.
   - Open your terminal and run:

   ```bash
   git clone https://github.com/your-username/Demo_GitHub_Action.git
   ```

5. **Add the Upstream Remote** (Optional but Recommended):
   - This allows you to keep your fork synchronized with the original repository.

   ```bash
   cd Demo_GitHub_Action
   git remote add upstream https://github.com/original-owner/Demo_GitHub_Action.git
   ```

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

## Delete Your Branch After Merging (Best Practice)

After your pull request has been successfully merged, it's important to delete your branch. Here's why and how:

**Why Delete the Branch?**
- **Clean Repository**: Keeps the repository clean and free from unnecessary branches.
- **Reduce Confusion**: Prevents confusion about which branches are active and current.
- **Easier Maintenance**: Makes it easier for team members to navigate and manage the repository.
- **Better Collaboration**: Reduces clutter and makes the workflow clearer for all contributors.


**How to Delete Your Branch**:

**Update your local `main` branch (Important step before deleting your branch)**:

1. **Switch to your `main` branch**:

   ```bash
   git checkout main
   ```

2. **Pull the latest merged changes**:

   - Pull from your fork's remote:

     ```bash
     git pull origin main
     ```

3. **Delete the Remote Branch on GitHub** (Recommended):
   - After merging, GitHub will typically offer a "Delete branch" button on the pull request page.
   - Alternatively, you can delete it from the command line:

   ```bash
   git push origin --delete your-branch-name
   ```

4. **Delete the Local Branch**:
   - Delete the branch from your local machine:

   ```bash
   git branch -d your-branch-name
   ```

   - If the branch hasn't been merged locally, use the force flag:

   ```bash
   git branch -D your-branch-name
   ```

## Where to See Triggered Test Cases

- Once the pull request is created, the GitHub Actions workflow will automatically run the test cases.
- Navigate to the "Actions" tab in your GitHub repository to view the status of the triggered tests.
- You can also see the test results directly in the pull request under the "Checks" section.

## Workflow

1. **Create a Pull Request**: Push your changes to a new branch and create a pull request
2. **Run Tests**: The workflow automatically runs all Pytest test cases (CI phase)
3. **Review Results**: Ensure all tests pass
   - If tests fail, fix the issues and push changes
   - The workflow will re-run automatically
4. **Approval and Merge**: The code owner reviews and merges the pull request if all tests pass
5. **Automatic Deployment**: After merge, the deployment pipeline runs (CD phase)
   - Code deploys to staging first
   - Then to production (if staging succeeds)
