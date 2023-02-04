import time
import numpy
import pytesseract
from scan import get_image
from PIL import Image
from sewar.full_ref import scc as sewar_compare

pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR-5/tesseract.exe'

E_LEFT = numpy.array(Image.open("samples/E-left.png"))
Q_LEFT = numpy.array(Image.open("samples/Q-left.png"))
R_LEFT = numpy.array(Image.open("samples/R-left.png"))

E_RIGHT = numpy.array(Image.open("samples/E-right.png"))
Q_RIGHT = numpy.array(Image.open("samples/Q-right.png"))
R_RIGHT = numpy.array(Image.open("samples/R-right.png"))

LEFT_SAMPLE_KEY = {
    'Q': Q_LEFT,
    'R': R_LEFT,
    'E': E_LEFT
}

RIGHT_SAMPLE_KEY = {
    'Q': Q_RIGHT,
    'R': R_RIGHT,
    'E': E_RIGHT
}


def which_keybind_is(keybind_to_check, samples):
    my_keybind = None

    for key in samples:
        confidence: int = sewar_compare(keybind_to_check, samples[key])
        if confidence > 0.6:
            my_keybind = key

    return my_keybind


def cooldown_number():
    print('wow')


def identify():
    keybind_l, keybind_r, cd = get_image()

    left_keybind = which_keybind_is(keybind_l, LEFT_SAMPLE_KEY)
    right_keybind = which_keybind_is(keybind_r, RIGHT_SAMPLE_KEY)

    keybinds = ['Q', 'E', 'R']
    current_keybind = None

    if left_keybind == None or right_keybind == None:
        current_keybind = None
    else:
        # Get current keybind
        for keybind in keybinds:
            if keybind not in [left_keybind, right_keybind]:
                current_keybind = keybind

    # Get cooldown number
    num = pytesseract.image_to_string(
        cd, config='--psm 7 -c tessedit_char_whitelist=0123456789')

    try:
        cd = (int(num))
        return current_keybind, cd
    except ValueError as e:
        cd = None

    return current_keybind, cd


if __name__ == '__main__':
    t_start = time.perf_counter()
    identify()
    t_end = time.perf_counter()
    t_elapsed = round((t_start - t_end) * -1000, 2)

    print("Identify took", str(t_elapsed) + 'ms')
