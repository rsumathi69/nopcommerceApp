pytest -m venv env1
env1/Scripts/activate.bat
pip install -r requirements.txt
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
pause
