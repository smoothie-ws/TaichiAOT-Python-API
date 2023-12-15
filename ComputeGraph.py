from typing import List

from .c_api import *
from . import AotModule
from . import Runtime


class compute_graph:
    def __init__(self, compute_graph_instance: TiComputeGraph):
        self._compute_graph: TiComputeGraph = compute_graph_instance

    @staticmethod
    def from_aot_module(aot_module: AotModule, compute_graph_name: str):
        return aot_module.get_compute_graph(compute_graph_name)

    def launch(self, runtime: Runtime, named_args: List[TiNamedArgument]) -> None:
        """Description placeholder"""

        ti_launch_compute_graph(runtime, self._compute_graph, len(named_args), named_args)
