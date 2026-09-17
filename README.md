# chmod-770-team-wiut-hackathon-2026 Working dummy prototype 



How to run this on your machine?

## Prerequisites

- Git
Python 3.10 or higher

## 1. Clone the repository

```bash
git clone <YOUR-REPO-URL>
cd <REPO-NAME>
```

## 2. Set up the venv

#### **Linux/MacOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### **Windows**

```PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

Ensure your terminal prompt starts with (.venv) before running:

```Bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Run the Application

```Bash

streamlit run app.py
```

## 5. All done

Streamlit is now running on your local machine and you can access it by visiting http://localhost:8501 in your web browser.

Technically, it shall be opened automatically.
