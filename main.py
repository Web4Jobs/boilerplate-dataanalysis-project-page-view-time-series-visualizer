import capture_results  # ✅ new
capture_results.start()  # ✅ new (start capture)

import time_series_visualizer
from unittest import main
import traceback

program = None
runtime_error = None

try:
    time_series_visualizer.draw_line_plot()
    time_series_visualizer.draw_bar_plot()
    time_series_visualizer.draw_box_plot()

    program = main(module="test_module", exit=False)

except Exception as e:
    runtime_error = e
    traceback.print_exc()

finally:
    capture_results.finish(program, runtime_error)