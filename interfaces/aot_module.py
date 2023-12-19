from ctypes import c_void_p

from taichiAOT._utils import *

from .compute_graph import ComputeGraph
from .kernel import Kernel
from .runtime import Runtime


class AotModule:
    def __init__(self, aot_module_instance: TiAotModule):
        self._aot_module: TiAotModule = aot_module_instance

    @staticmethod
    def load(ti_runtime: Runtime,
             filepath: str) -> 'AotModule':
        """Load an AOT module from a file on the TiRuntime."""

        aot_module_instance = ti_load_aot_module(ti_runtime.runtime_instance, filepath)

        get_last_error()
        return AotModule(aot_module_instance)

    @staticmethod
    def create(ti_runtime: Runtime,
               data: c_void_p,
               size: int) -> 'AotModule':
        """Create an AOT module on the TiRuntime from data."""

        aot_module_instance = ti_create_aot_module(ti_runtime.runtime_instance, data, size)

        get_last_error()
        return AotModule(aot_module_instance)

    def destroy(self) -> None:
        """Destroy an AOT module on the TiRuntime."""

        ti_destroy_aot_module(self._aot_module)

    def get_kernel(self, kernel_name: str) -> Kernel:
        """Get a kernel from an AOT module on the TiRuntime."""

        kernel_instance = ti_get_aot_module_kernel(self._aot_module, kernel_name)

        get_last_error()
        return Kernel(kernel_instance)

    def get_compute_graph(self, graph_name: str) -> ComputeGraph:
        """Get a compute graph from an AOT module on the TiRuntime."""

        compute_graph_instance = ti_get_aot_module_compute_graph(self._aot_module, graph_name)

        get_last_error()
        return ComputeGraph(compute_graph_instance)
