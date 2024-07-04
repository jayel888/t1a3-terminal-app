#!/bin/bash
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the main application
python3 ./src/main.py

# Deactivate virtual environment
deactivate