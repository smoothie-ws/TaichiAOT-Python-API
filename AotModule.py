from .utils import *

from .ComputeGraph import compute_graph
from .Kernel import kernel
from .Runtime import runtime


class AotModule:
    def __init__(self, aot_module_instance: c_api.TiAotModule):
        self._aot_module: c_api.TiAotModule = aot_module_instance

    @staticmethod
    def load(ti_runtime: runtime,
             filepath: str) -> 'AotModule':
        """Load an AOT module from a file on the TiRuntime."""

        aot_module_instance = c_api.ti_load_aot_module(ti_runtime.runtime_instance, filepath)

        get_last_error()
        return AotModule(aot_module_instance)

    @staticmethod
    def create(ti_runtime: runtime,
               data: c_api.c_void_p,
               size: int) -> 'AotModule':
        """Create an AOT module on the TiRuntime from data."""

        aot_module_instance = c_api.ti_create_aot_module(ti_runtime.runtime_instance, data, size)

        get_last_error()
        return AotModule(aot_module_instance)

    def destroy(self) -> None:
        """Destroy an AOT module on the TiRuntime."""

        c_api.ti_destroy_aot_module(self._aot_module)

    def get_kernel(self, kernel_name: str) -> kernel:
        """Get a kernel from an AOT module on the TiRuntime."""

        kernel_instance = c_api.ti_get_aot_module_kernel(self._aot_module, kernel_name)

        get_last_error()
        return kernel(kernel_instance)

    def get_compute_graph(self, graph_name: str) -> compute_graph:
        """Get a compute graph from an AOT module on the TiRuntime."""

        compute_graph_instance = c_api.ti_get_aot_module_compute_graph(self._aot_module, graph_name)

        get_last_error()
        return compute_graph(compute_graph_instance)
