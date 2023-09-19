

rem Create a virtual environment
python -m venv venv

rem Activate the virtual environment (Windows)
call venv\Scripts\activate

rem Install required packages
pip install -r requirements.txt

rem Deactivate the virtual environment
deactivate
