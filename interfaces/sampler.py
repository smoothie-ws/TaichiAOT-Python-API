from .runtime import Runtime
from taichiAOT._utils import *


class Sampler:
    def __init__(self, ti_runtime: Runtime, ti_sampler: TiSampler, create_info: TiSamplerCreateInfo = None):
        if create_info is not None:
            self.create(ti_runtime, create_info)
        else:
            self._runtime = ti_runtime
            self._sampler = ti_sampler

    @staticmethod
    def create(ti_runtime: Runtime,
               create_info: TiSamplerCreateInfo) -> 'Sampler':
        """Create a sampler on the TiRuntime."""

        sampler_instance = ti_create_sampler(ti_runtime.runtime_instance, create_info)

        get_last_error()
        return Sampler(ti_runtime=ti_runtime, ti_sampler=sampler_instance)

    def destroy(self) -> None:
        """Destroy a sampler on the TiRuntime."""

        ti_destroy_sampler(self._runtime.runtime_instance, Sampler)
