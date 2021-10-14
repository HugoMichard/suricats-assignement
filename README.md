## Mission To Mars

This test was provided by Suricats. The test tasks are described in the MissionToMars.md file.

### Installation

This test is solved with Python3.

Prerequisites :
- Have Python3 installed (https://www.python.org/downloads/)
- Have pip installed

Install the project by running the following commands in your terminal :
```
git clone https://github.com/HugoMichard/suricats-assignement.git suricats-assignement
cd suricats-assignement
pip install -r requirements.txt
```

### Architecture

Main.py file contains a script to run the rover. It can be started with :
```
python3 main.py
```
In case of import errors, please verify your PYTHONPATH is correctly set to the project root.

Rover.py contains the implementation of the rover that solves the test tasks and the test.py file contains the tests 
implemented to check the code robustness.

### Tests

Tests are done with unittest and can be found in the test.py file.
