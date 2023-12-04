# TaichiAOT-Python-API
## Taichi C-API Functions

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

... (continue for other functions)

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

... (continue for other functions)


