"""This module is designed to seamlessly integrate with Taichi's
Ahead-of-Time (AOT) compilation capabilities, enabling users to leverage the
performance benefits of precompiled Taichi kernels.

Key Features:

- **AOT Compilation Support:** AOT-Taichi-Pybind facilitates the compilation
of Taichi kernels ahead of runtime, optimizing performance by eliminating
the need for just-in-time compilation during execution.

- **Seamless Python Integration:** The module ensures smooth
interoperability between Python and Taichi, allowing users to harness the
power of Taichi's C-API directly from their Python scripts.

- **Efficient Kernel Launching:** Users can launch Taichi kernels with the
provided Python bindings, passing runtime, kernel, and arguments seamlessly.
The module ensures that the provided arguments match the expected count and
types defined in the source code.

"""

from .utils import *

from .ComputeGraph import compute_graph
from .AotModule import AotModule
from .Kernel import kernel
from .Runtime import runtime
from .c_api import *
