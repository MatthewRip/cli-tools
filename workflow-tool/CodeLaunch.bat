@echo off
setlocal

REM Set the flag to true or false
set "START_VENV=false"

REM Check if the flag is true
if "%START_VENV%"=="true" (
    echo Starting virtual environment...
    call venv\Scripts\activate
)

REM Run the main.py script
echo Running main.py...
python main.py

REM Deactivate the virtual environment if it was activated
if "%START_VENV%"=="true" (
    echo Deactivating virtual environment...
    deactivate
)

endlocal