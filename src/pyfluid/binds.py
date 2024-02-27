from ctypes.util import find_library
from ctypes import cdll, c_int, c_char_p

__library = None


def load_fluidsynth_library():
    c_fluidsynth_lib_name = find_library("fluidsynth")
    if c_fluidsynth_lib_name is None:
        raise Exception("Fluidsyth lib is nowhere to be found!")
    return cdll.LoadLibrary(c_fluidsynth_lib_name)


# Fluidsynth log bind for testing purposes
def fluid_log(message: bytes):
    # Fluid log has this defenition fluid_log(int LOG_LEVEL, char* message)
    __library.fluid_log(c_int(3), c_char_p(message))

## TODO: Fix this hackey way of loading libraries
__library = load_fluidsynth_library()