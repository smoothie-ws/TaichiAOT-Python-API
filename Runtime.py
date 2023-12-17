from .utils import *


class runtime:
    def __init__(self, arch: c_api.TiArch = c_api.TiArch.TI_ARCH_VULKAN,
                 device: int = 0):
        self._runtime: c_api.TiRuntime = c_api.ti_create_runtime(arch, device)
        self.arch: c_api.TiArch = arch
        self.device: int = device

    @property
    def runtime_instance(self):
        return self._runtime

    @staticmethod
    def create(arch: c_api.TiArch = c_api.TiArch.TI_ARCH_VULKAN,
               device: int = 0) -> 'runtime':
        """Creates a Taichi Runtime with the specified TiArch.

            Args:
                arch: specified TiArch.
                device: the index of device to create Taichi Runtime on.

            Returns:
                The `runtime` instance.
            """

        return runtime(arch, device)

    def destroy(self) -> None:
        """Destroys a Taichi Runtime."""

        c_api.ti_destroy_runtime(self._runtime)
        self.arch = None
        self.device = None

    def flush(self) -> None:
        """Submits all previously invoked device commands to the offload device for execution."""

        c_api.ti_flush(self._runtime)

    def wait(self) -> None:
        """Waits until all previously invoked device commands are executed.

         Any invoked command that has not been submitted is submitted first."""

        c_api.ti_wait(self._runtime)
