from taichiAOT._utils import *


class Runtime:
    def __init__(self, arch: TiArch = TiArch.TI_ARCH_VULKAN,
                 device: int = 0):
        self._runtime: TiRuntime = ti_create_runtime(arch, device)
        self.arch: TiArch = arch
        self.device: int = device

    @property
    def runtime_instance(self) -> TiRuntime:
        if self._runtime is None:
            self.create()

        return self._runtime

    @staticmethod
    def create(arch: TiArch = TiArch.TI_ARCH_VULKAN,
               device: int = 0) -> 'Runtime':
        """Creates a Taichi Runtime with the specified TiArch.

            Args:
                arch: specified TiArch.
                device: the index of device to create Taichi Runtime on.

            Returns:
                The :class:`runtime` instance.
            """

        return Runtime(arch, device)

    def destroy(self) -> None:
        """Destroys a Taichi Runtime."""

        ti_destroy_runtime(self._runtime)
        self.arch = None
        self.device = None

    def flush(self) -> None:
        """Submits all previously invoked device commands to the offload
        device for execution."""

        ti_flush(self._runtime)

    def wait(self) -> None:
        """Waits until all previously invoked device commands are executed.

         Any invoked command that has not been submitted is submitted first."""

        ti_wait(self._runtime)
