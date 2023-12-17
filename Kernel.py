import time
from ctypes import POINTER, cast
from typing import Any

import numpy as np

from .KernelArgument import kernel_argument
from .Runtime import runtime
from .c_api import *
from .utils import ctypes_datatype, get_last_error


class kernel:
    def __init__(self, kernel_instance: TiKernel):
        self._kernel: TiKernel = kernel_instance
        self.arg_params = []
        self.kernel_params = []

    def set_arguments(self, ti_runtime: runtime, *args):
        for arg in args:
            argument = kernel_argument(ti_runtime, arg)
            self.arg_params.append(argument)
            self.kernel_params.append(argument.get_ti_argument)

        get_last_error()

    def launch(self, ti_runtime: runtime, *args) -> list[Any]:
        if args is not None:
            self.set_arguments(ti_runtime, *args)

        ti_launch_kernel(ti_runtime.runtime_instance, self._kernel, len(self.kernel_params), self.kernel_params)
        ti_runtime.wait()

        res_params = []
        for param in self.arg_params:
            if param.type == TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY:
                data_array = cast(param.allocated_memory.map(), POINTER(ctypes_datatype(param.og) * param.og.size)).contents
                res_params.append(np.array(data_array).reshape(param.og.shape))
                param.allocated_memory.unmap()
                param.allocated_memory.free()

        get_last_error()
        return res_params
