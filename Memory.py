from ctypes import c_void_p

from .Runtime import runtime
from .c_api import *


class memory:
    def __init__(self, ti_runtime: runtime, memory_instance: TiMemory) -> None:
        self._memory = memory_instance
        self._runtime = ti_runtime

    @property
    def memory_instance(self) -> TiMemory:
        return self._memory

    @staticmethod
    def allocate(ti_runtime: runtime, allocate_info: TiMemoryAllocateInfo) -> 'memory':
        memory_instance = ti_allocate_memory(ti_runtime.runtime_instance, allocate_info)
        return memory(ti_runtime, memory_instance)

    def free(self) -> None:
        ti_free_memory(self._runtime.runtime_instance, self._memory)

    def map(self) -> c_void_p:
        return ti_map_memory(self._runtime.runtime_instance, self._memory)

    def unmap(self) -> None:
        ti_unmap_memory(self._runtime.runtime_instance, self._memory)
