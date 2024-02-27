from ctypes.util import find_library
from ctypes import cdll, c_int, c_char_p

__library = load_fluidsynth_library()


def load_fluidsynth_library():
    c_fluidsynth_lib_name = find_library("fluidsynth")
    if c_fluidsynth_lib_name is None:
        raise Exception("Fluidsyth lib is nowhere to be found!")
    return cdll.LoadLibrary(c_fluidsynth_lib_name)

