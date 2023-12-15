from ctypes import c_void_p

from .c_api import *
from .ComputeGraph import compute_graph
from .Kernel import kernel
from .Runtime import runtime


class aot_module:
    def __init__(self, aot_module_instance: TiAotModule):
        self._aot_module: TiAotModule = aot_module_instance

    @staticmethod
    def load(ti_runtime: runtime,
             filepath: str) -> 'aot_module':
        """Description placeholder"""

        aot_module_instance = ti_load_aot_module(ti_runtime.runtime_instance, filepath)
        return aot_module(aot_module_instance)

    @staticmethod
    def create(ti_runtime: runtime,
               data: c_void_p,
               size: int) -> 'aot_module':
        """Description placeholder"""

        aot_module_instance = ti_create_aot_module(ti_runtime.runtime_instance, data, size)
        return aot_module(aot_module_instance)

    def destroy(self) -> None:
        """Description placeholder"""

        ti_destroy_aot_module(self._aot_module)

    def get_kernel(self, kernel_name: str) -> kernel:
        """Description placeholder"""

        kernel_instance = ti_get_aot_module_kernel(self._aot_module, kernel_name)
        return kernel(kernel_instance)

    def get_compute_graph(self, graph_name: str) -> compute_graph:
        """Description placeholder"""

        compute_graph_instance = ti_get_aot_module_compute_graph(self._aot_module, graph_name)
        return compute_graph(compute_graph_instance)
