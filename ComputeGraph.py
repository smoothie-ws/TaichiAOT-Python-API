from typing import List

from .Runtime import runtime
from .utils import *


class compute_graph:
    def __init__(self, compute_graph_instance: c_api.TiComputeGraph):
        self._compute_graph: c_api.TiComputeGraph = compute_graph_instance

    @staticmethod
    def from_aot_module(ti_aot_module, compute_graph_name: str):
        return ti_aot_module.get_compute_graph(compute_graph_name)

    def launch(self, ti_runtime: runtime, named_args: List[c_api.TiNamedArgument]) -> None:
        """Description placeholder"""

        c_api.ti_launch_compute_graph(ti_runtime, self._compute_graph, len(named_args), named_args)
