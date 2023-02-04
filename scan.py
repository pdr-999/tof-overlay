import time
import os
import numpy
import mss.tools
import mss

TRACE_PERFORMANCE = True
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Can be optimized
def get_image() -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    with mss.mss() as sct:
        # The screen part to capture
        region_r = {'left': 1859, 'top': 1029, 'width': 13, 'height': 13}
        region_l = {'left': 1734, 'top': 912, 'width': 13, 'height': 13}
        region_c = {'left': 1740, 'top': 970, 'width': 45, 'height': 29}

        # Grab the data
        img_r = sct.grab(region_r)
        img_l = sct.grab(region_l)
        img_c = sct.grab(region_c)

        pix_r = numpy.array(img_r)
        pix_l = numpy.array(img_l)
        pix_c = numpy.array(img_c)

        return pix_l,pix_r,pix_c

if __name__ == '__main__':
    if TRACE_PERFORMANCE:
        execute_x_times = 1
        lowest = 0
        highest = 0
        total_ms = 0
        for i in range(execute_x_times):
            t_start = time.perf_counter()
            get_image()
            t_end = time.perf_counter()
            t_elapsed = round((t_start - t_end) * -1000, 2)

            if i == 0:
                lowest = t_elapsed
                highest = t_elapsed
            
            if t_elapsed < lowest:
                lowest = t_elapsed

            if t_elapsed > highest:
                highest = t_elapsed

            total_ms += t_elapsed
        
        average = total_ms / execute_x_times

        print("Lowest: ", str(lowest) + 'ms', " Highest: ", str(highest) + 'ms', " Average: ", str(average) + 'ms')
    else:
        get_image()