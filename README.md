# GUVI Task 18 - Behave, Selenium and Allure

## Objective

Automate the GUVI Zen Portal authentication scenarios using Python Behave,
Selenium WebDriver, Page Object Model (POM), and Allure reporting.

Portal: https://v2.zenclass.in/login

## Technology stack

- Python
- Behave (BDD)
- Selenium WebDriver
- Allure Behave adapter
- Allure command-line report generator

## Project structure

```text
GUVI_Task18_Behave_Allure/
├── features/
│   ├── steps/
│   │   └── login_steps.py
│   ├── environment.py
│   └── zen_portal.feature
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── reports/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup (Windows / PyCharm)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Google Chrome. Selenium 4 uses Selenium Manager to locate/download
a compatible ChromeDriver when possible.

## Configure credentials

Do not hard-code your personal Zen Portal credentials in the repository.
Set them in the current PowerShell session:

```powershell
$env:ZEN_VALID_USERNAME="your_zen_username_or_email"
$env:ZEN_VALID_PASSWORD="your_zen_password"
```

Optional portal URL override:

```powershell
$env:ZEN_PORTAL_URL="https://v2.zenclass.in/login"
```

Optional headless execution:

```powershell
$env:HEADLESS="true"
```

## Scenarios

1. Successful login - valid credentials and dashboard navigation.
2. Unsuccessful login - invalid credentials and remain on login page.
3. Username/password input validation - both inputs are visible.
4. Submit button validation - Sign in button is visible and enabled.
5. Logout - open profile menu, click Log out and verify login form returns.

## Run Behave and create Allure JSON results

From the project root:

```powershell
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

If the `behave.exe` launcher is blocked by Windows Application Control,
run it through Python:

```powershell
python -m behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

The `reports/allure-results` directory contains Allure result JSON files
and attachments. Preserve this directory when generating the HTML report.

## Generate Allure HTML report

Install the Allure Commandline tool separately. One option on Windows is:

```powershell
winget install --id QametaSoftware.Allure
```

Close and reopen the terminal after installation if the `allure` command
is not yet available. Then run:

```powershell
allure generate reports/allure-results -o reports/allure-html --clean
allure open reports/allure-html
```

The generated HTML report is in `reports/allure-html`. The JSON result
files remain in `reports/allure-results`.

## Implementation notes

- `pages/login_page.py` implements the Page Object Model and encapsulates
  Selenium locators and browser interactions.
- `features/zen_portal.feature` contains the BDD scenarios in Gherkin.
- `features/steps/login_steps.py` maps Gherkin steps to Python functions.
- `features/environment.py` manages browser setup and teardown.
- Python classes and methods demonstrate OOP.
- Selenium `TimeoutException`, `NoSuchElementException`, and
  `WebDriverException` are handled in the page object.
- Dashboard popups are closed when present; absent popups are optional.

## GitHub submission

Create a separate public repository named `GUVI_Task18_Behave_Allure`.
Do not commit credentials, virtual environments, or local report output
unless GUVI specifically asks for the generated report files.
