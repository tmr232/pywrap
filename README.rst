pywrap
======

Simple function-wrapping API with ctypes.

Usage
-----

Replace this:

.. code:: python

    prototype = ctypes.WINFUNCTYPE(wintypes.HANDLE, wintypes.UINT, wintypes.HANDLE)
    paramflags = (1, "uFormat"), (1, "hMem")
    SetClipboardData = prototype(("SetClipboardData", user32), paramflags)
    SetClipboardData.errcheck = null_errcheck

With this:

.. code:: python

    SetClipboardData = pywrap.wrap_winapi(name="SetClipboardData",
                                            library=user32,
                                            restype=wintypes.BOOL,
                                            params=[
                                                Parameter("uFormat", wintypes.UINT),
                                                Parameter("hMem", wintypes.HANDLE)
                                            ],
                                            errcheck=null_errcheck)
