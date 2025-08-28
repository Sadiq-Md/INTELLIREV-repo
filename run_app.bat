@echo off
echo Launching IntelliRev Dashboard...
call venv\Scripts\activate
streamlit run dashboard.py
pause
