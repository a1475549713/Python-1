import os

import sys

import multiprocessing

# Module multiprocessing is organized differently in Python 3.4+

try:
    if sys.platform.startswith('win'):
    # Python 3.4+
        import multiprocessing.popen_spawn_win32 as forking
    else:

        import multiprocessing.popen_fork as forking
except ImportError:

    import multiprocessing.forking as forking
if sys.platform.startswith('win'):

    # First define a modified version of Popen.
    class _Popen(forking.Popen):

        def __init__(self, *args, **kw):
            if hasattr(sys, 'frozen'):
                # We have to set original _MEIPASS2 value from sys._MEIPASS                # to get --onefile mode working.                os.putenv('_MEIPASS2', sys._MEIPASS)
                os.putenv('_MEIPASS2', sys._MEIPASS)

            try:
                super(_Popen, self).__init__(*args, **kw)
            finally:

                if hasattr(sys, 'frozen'):
                    if hasattr(os, 'unsetenv'):
                        os.unsetenv('_MEIPASS2')
                    else:

                        os.putenv('_MEIPASS2', '')
forking.Popen = _Popen