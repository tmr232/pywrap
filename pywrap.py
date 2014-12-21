import ctypes


def _wrap(functype, name, library, restype, params, errcheck=None):
    prototype = functype(restype, *(param.type for param in params))
    paramflags = tuple(param.paramflags for param in params)
    wrapper = prototype((name, library), paramflags)
    if errcheck:
        wrapper.errcheck = errcheck

    return wrapper


def wrap_winapi(name, library, restype, params, errcheck=None):
    return _wrap(ctypes.WINFUNCTYPE, name, library, restype, params, errcheck=errcheck)


def wrap_cdecl(name, library, restype, params, errcheck=None):
    return _wrap(ctypes.CFUNCTYPE, name, library, restype, params, errcheck=errcheck)


class Parameter(object):
    def __init__(self, name, type_, default=None, out=False):
        self._name = name
        self._type = type_
        self._out = out
        self._default = default

    @property
    def flag(self):
        if self._out:
            return 2
        else:
            return 1

    @property
    def type(self):
        return self._type

    @property
    def paramflags(self):
        paramflags = (self.flag, self._name, self._default)
        if self._default is None:
            return paramflags[:-1]
        else:
            return paramflags


class Errcheck(object):
    @staticmethod
    def expect_true(result, func, args):
        if not result:
            raise ctypes.WinError()
        return result

    @staticmethod
    def expect_null(result, func, args):
        if result:
            raise ctypes.WinError()
        return result

    @staticmethod
    def expect_not_null(result, func, args):
        if not result:
            raise ctypes.WinError()
        return result

    @staticmethod
    def expect_value(value):
        def errcheck(result, func, args):
            if result != value:
                raise ctypes.WinError()
            return result

        return errcheck


    @staticmethod
    def expect_lasterror(value):
        def errcheck(result, func, args):
            if ctypes.get_last_error() != value:
                raise ctypes.WinError()
            return result

        return errcheck

    @staticmethod
    def expect_no_error(result, func, args):
        if ctypes.get_last_error():
            raise ctypes.WinError()
        return result

    @staticmethod
    def print_all(result, func, args):
        print result, func, args
        return result
