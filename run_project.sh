#!/bin/bash

# Set up virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv env
source env/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the main Python script
echo "Running the bankruptcy prediction model..."
python main.py

# Check if outputs are generated
if [ -d "outputs" ]; then
    echo "Outputs generated successfully. Check the 'outputs' directory for results."
else
    echo "Error: Outputs not generated."
    exit 1
fi

# Deactivate virtual environment
deactivate
echo "Process completed. View the documentation for further steps."
