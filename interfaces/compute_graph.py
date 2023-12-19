from typing import List

from .runtime import Runtime
from taichiAOT._utils import *


class ComputeGraph:
    def __init__(self, compute_graph_instance: TiComputeGraph):
        self._compute_graph: TiComputeGraph = compute_graph_instance

    @staticmethod
    def from_aot_module(ti_aot_module, compute_graph_name: str):
        return ti_aot_module.get_compute_graph(compute_graph_name)

    def launch(self, ti_runtime: Runtime, named_args: List[TiNamedArgument]) -> None:
        """Description placeholder"""

        ti_launch_compute_graph(ti_runtime, self._compute_graph, len(named_args), named_args)
