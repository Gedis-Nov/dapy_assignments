# This entrypoint file to be used in development. Start by reading README.md
import med_data_visualizer
from unittest import main

# Test your function by calling it here
med_data_visualizer.draw_cat_plot()
med_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='med_data_visualizer_test', exit=False)
