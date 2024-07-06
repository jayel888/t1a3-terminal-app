#!/bin/bash

# Function to check if Python is installed
check_python() {
    if command -v python3 &> /dev/null; then
        echo "Python3 is already installed."
        return 0
    else
        return 1
    fi
}

# Function to install Python
install_python() {
    echo "Python3 is not installed. Installing now..."
    # Update the package list
    sudo apt-get update
    # Install Python
    sudo apt-get install -y python3
    echo "Python3 installation complete."
}

# Check if Python is installed, if not, install it
if ! check_python; then
    install_python
fi