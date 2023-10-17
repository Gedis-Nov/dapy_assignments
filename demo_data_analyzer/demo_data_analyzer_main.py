# This entrypoint file to be used in development. Start by reading README.md
import demo_data_analyzer
from unittest import main

# Test your function by calling it here
demo_data_analyzer.calc_demo_data()

# Run unit tests automatically
main(module='demo_data_analyzer_test', exit=False)
