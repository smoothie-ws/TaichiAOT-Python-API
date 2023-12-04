# TaichiAOT-Python-API

### function `get_version`()
> *Get the current version of Taichi C API.*
> 
> >**Parameters:** `None`
> >
> > **Returns:** `c_uint32` - the current version of Taichi C API

### function `get_last_error`()
> *Get the last error raised by Taichi C-API invocations.*
> 
> >**Parameters:** `None`
> >
> > **Returns:** `str` - the last error message

### function `create_runtime`(`arch: TiArch`, `device: int`)
> *Create a Taichi runtime.*
> 
> >**Parameters:**
> >
> > - `arch` (Type: `TiArch`): The architecture for the runtime.
> > - `device` (Type: `int`): The device index.
> >
> > **Returns:** `TiRuntime` - the created Taichi runtime

### function `get_available_archs`(None) -> **`Tuple[List[c_uint32], List[TiArch]]`**
> *Get the available architectures.*
> 
> >**Parameters:** `None`
> >
> > **Returns:** Tuple(`List[c_uint32]`, `List[TiArch]`) - available architectures

### function `destroy_runtime`(`runtime: TiRuntime`)
> *Destroy a Taichi runtime.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime to be destroyed.
> >
> > **Returns:** `None`

### function `set_last_error`(`error: TiError, message: str`) -> **`None`**
> *Set the last error in Taichi C-API.*
> 
> >**Parameters:**
> >
> > - `error` (Type: `TiError`): The error code.
> > - `message` (Type: `str`): The error message.
> >
> > **Returns:** `None`

### function `allocate_memory`(`runtime: TiRuntime, allocate_info: TiMemoryAllocateInfo`) -> **`TiMemory`**
> *Allocate memory and return a TiMemory pointer.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which memory will be allocated.
> > - `allocate_info` (Type: `TiMemoryAllocateInfo`): Memory allocation parameters.
> >
> > **Returns:** `TiMemory` - Pointer to the allocated memory

### function `free_memory`(`runtime: TiRuntime, memory: TiMemory`) -> **`None`**
> *Free the allocated memory.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which memory was allocated.
> > - `memory` (Type: `TiMemory`): Pointer to the allocated memory.
> >
> > **Returns:** `None`

### function `map_memory`(`runtime: TiRuntime, memory: TiMemory`) -> **`c_void_p`**
> *Map device memory to host-addressable space.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which memory is mapped.
> > - `memory` (Type: `TiMemory`): Pointer to the allocated memory.
> >
> > **Returns:** `c_void_p` - Mapped host-addressable space

### function `unmap_memory`(`runtime: TiRuntime, memory: TiMemory`) -> **`None`**
> *Unmap device memory, making host-side changes visible to the device.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which memory is unmapped.
> > - `memory` (Type: `TiMemory`): Pointer to the allocated memory.
> >
> > **Returns:** `None`

### function `allocate_image`(`runtime: TiRuntime, allocate_info: TiImageAllocateInfo`) -> **`c_void_p`**
> *Allocate an image and return a pointer.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the image will be allocated.
> > - `allocate_info` (Type: `TiImageAllocateInfo`): Image allocation parameters.
> >
> > **Returns:** `c_void_p` - Pointer to the allocated image

### function `free_image`(`runtime: TiRuntime, image: TiImage`) -> **`None`**
> *Free the allocated image.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the image was allocated.
> > - `image` (Type: `TiImage`): Pointer to the allocated image.
> >
> > **Returns:** `None`

### function `create_sampler`(`runtime: TiRuntime, create_info: TiSamplerCreateInfo`) -> **`TiSampler`**
> *Create a sampler.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the sampler will be created.
> > - `create_info` (Type: `TiSamplerCreateInfo`): Sampler creation parameters.
> >
> > **Returns:** `TiSampler` - Created sampler

### function `destroy_sampler`(`runtime: TiRuntime, sampler: TiSampler`) -> **`None`**
> *Destroy a sampler.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the sampler was created.
> > - `sampler` (Type: `TiSampler`): The sampler to be destroyed.
> >
> > **Returns:** `None`

### function `copy_memory_device_to_device`(`runtime: TiRuntime, src: TiMemorySlice, dst: TiMemorySlice`) -> **`None`**
> *Copy device memory from source to destination.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime for the memory copy operation.
> > - `src` (Type: `TiMemorySlice`): Source memory slice.
> > - `dst` (Type: `TiMemorySlice`): Destination memory slice.
> >
> > **Returns:** `None`

### function `copy_image_device_to_device`(`runtime: TiRuntime, src: TiImageSlice, dst: TiImageSlice`) -> **`None`**
> *Copy device image from source to destination.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime for the image copy operation.
> > - `src` (Type: `TiImageSlice`): Source image slice.
> > - `dst` (Type: `TiImageSlice`): Destination image slice.
> >
> > **Returns:** `None`

### function `launch_kernel`(`runtime: TiRuntime, kernel: TiKernel, num_args: int, args: List[TiArgument]`) -> **`None`**
> *Launch a Taichi kernel with provided arguments.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the kernel will be launched.
> > - `kernel` (Type: `TiKernel`): The kernel to be launched.
> > - `num_args` (Type: `int`): Number of kernel arguments.
> > - `args` (Type: `List[TiArgument]`): List of kernel arguments.
> >
> > **Returns:** `None`

### function `launch_compute_graph`(`runtime: TiRuntime, graph: TiComputeGraph, num_args: int, named_args: List[TiNamedArgument]`) -> **`None`**
> *Launch a Taichi compute graph with provided arguments.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the compute graph will be launched.
> > - `graph` (Type: `TiComputeGraph`): The compute graph to be launched.
> > - `num_args` (Type: `int`): Number of compute graph arguments.
> > - `named_args` (Type: `List[TiNamedArgument]`): List of compute graph arguments.
> >
> > **Returns:** `None`

### function `flush`(`runtime: TiRuntime`) -> **`None`**
> *Flush pending operations on the runtime.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime to be flushed.
> >
> > **Returns:** `None`

### function `wait`(`runtime: TiRuntime`) -> **`None`**
> *Wait for all operations on the runtime to complete.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime to wait for.
> >
> > **Returns:** `None`

### function `load_aot_module`(`runtime: TiRuntime, filepath: str`) -> **`TiAotModule`**
> *Load an Ahead-of-Time (AOT) module from a file.*
> 
> >**Parameters:**
> >
> > - `runtime` (Type: `TiRuntime`): The runtime on which the AOT module will be loaded.
> > - `filepath` (Type: `str`): The path to the AOT module file.
> >
> > **Returns:** `TiAotModule` - Loaded AOT module

### function `destroy_aot_module`(`module: TiAotModule`) -> **`None`**
> *Destroy an Ahead-of-Time (AOT) module.*
> 
> >**Parameters:**
> >
> > - `module` (Type: `TiAotModule`): The AOT module to be destroyed.
> >
> > **Returns:** `None`

### function `get_aot_module_kernel`(`module: TiAotModule, kernel_name: str`) -> **`TiKernel`**
> *Get a kernel from an Ahead-of-Time (AOT) module by name.*
> 
> >**Parameters:**
> >
> > - `module` (Type: `TiAotModule`): The AOT module containing the kernel.
> > - `kernel_name` (Type: `str`): The name of the kernel.
> >
> > **Returns:** `TiKernel` - Kernel from the AOT module

### function `get_aot_module_compute_graph`(`module: TiAotModule, graph_name: str`) -> **`TiComputeGraph`**
> *Get a compute graph from an Ahead-of-Time (AOT) module by name.*
> 
> >**Parameters:**
> >
> > - `module` (Type: `TiAotModule`): The AOT module containing the compute graph.
> > - `graph_name` (Type: `str`): The name of the compute graph.
> >
> > **Returns:** `TiComputeGraph` - Compute graph from the AOT module



