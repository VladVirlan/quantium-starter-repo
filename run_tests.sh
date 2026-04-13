# Must be run in Git Bash terminal

#!/usr/bin/env bash

set -e

echo "Activating virtual environment..."

# Windows virtualenv path
source venv/Scripts/activate

echo "Virtual environment activated."

echo "Running test suite..."
pytest

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi
