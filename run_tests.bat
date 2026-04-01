@echo off

REM Activate virtual environment
call venv\Scripts\activate

REM Run tests
pytest

REM Check result
IF %ERRORLEVEL% EQU 0 (
    echo All tests passed
    exit /b 0
) ELSE (
    echo Tests failed
    exit /b 1
)