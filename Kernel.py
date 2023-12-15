from ctypes import POINTER, cast
from typing import Any, List

import numpy as np

from .c_api import *
from .utils import ctypes_datatype
from .KernelArgument import kernel_argument
from .Runtime import runtime


class kernel:
    def __init__(self, kernel_instance: TiKernel):
        self._kernel: TiKernel = kernel_instance
        self.arguments = None

    def launch(self, ti_runtime: runtime, *args) -> list[Any]:
        params = []
        kernel_args = []
        for arg in args:
            argument = kernel_argument(ti_runtime, arg)
            params.append(argument)
            kernel_args.append(argument.get_ti_argument)

        ti_launch_kernel(ti_runtime.runtime_instance, self._kernel, len(kernel_args), kernel_args)

        ti_runtime.wait()

        return_args = []
        for parameter in params:
            if parameter.type == TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY:
                mapped_data = parameter.allocated_memory.map()
                data_array = cast(mapped_data, POINTER(ctypes_datatype(parameter.og) * parameter.og.size)).contents
                return_args.append(np.array(data_array).reshape(parameter.og.shape))
                parameter.allocated_memory.unmap()
                parameter.allocated_memory.free()

        return return_args
