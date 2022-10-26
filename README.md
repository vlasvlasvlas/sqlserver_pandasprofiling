# Whats this
- data profiling from sql server tables and views

# Structures
- data-profiles: pandas profiling html exports
- scripts: python based script

# Scripts
- dataprofile.py: connects to db, get list of tables and views, and for each one it generates and export pandas profiling html on output folder

# Instructions
- create virtualenv (python -m venv venv)
- access / activate virtualenv (source venv/scripts/activate)
- install libraries from requirements.txt (pip install -r requirements.txt)
- execute script (pip scripts/dataprofile.py)
- enjoy
