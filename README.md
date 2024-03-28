# Decrypt NVML Debug Log Files
The [NVIDIA Management Library (NVML)
](https://developer.nvidia.com/nvidia-management-library-nvml) library `libnvidia-ml.so` can generate a debug/trace log file.

In the log file each byte/character is encrypted by the next pseudorandom number generated with a xorwow random number generator.

This tool can decrypt those log files.

## generate example log file
```sh
__NVML_DBG_FILE=nvml-trace.log __NVML_DBG_LVL=DEBUG nvidia-smi -L
```

## decrypt example log file
```sh
./nvml-log-decrypt.py ./nvml_trace.log 

NVML LOG

Build branch : r551_40
Build date   : Thu-Feb-22-01:23:10-UTC-2024
Build CL     : 33933991
Build Type   : Local build
NVML Log 3/28/2024 09:23:08.012
DEBUG:	[tid 2522389]	[0.000048s - nvml.c:148]	Entering nvmlInitWithFlags(void) ()
INFO:	[tid 2522389]	[0.005029s - nvml.c:230]	-1
INFO:	[tid 2522389]	[0.005055s - nvml.c:239]	
DEBUG:	[tid 2522389]	[0.005325s - dmal/common/common_ops.c:43]	c1d08eb5 00000214
DEBUG:	[tid 2522389]	[0.005356s - dmal/common/common_ops.c:45]	c1d08eb5 00000214 ## 0x0
DEBUG:	[tid 2522389]	[0.005362s - dmal/common/common_ops.c:43]	c1d08eb5 0000021b
DEBUG:	[tid 2522389]	[0.005371s - dmal/common/common_ops.c:45]	c1d08eb5 0000021b ## 0x0
DEBUG:	[tid 2522389]	[0.005376s - dmal/common/common_ops.c:43]	c1d08eb5 00000279
DEBUG:	[tid 2522389]	[0.005385s - dmal/common/common_ops.c:45]	c1d08eb5 00000279 ## 0x0
DEBUG:	[tid 2522389]	[0.005391s - dmal/common/common_ops.c:43]	c1d08eb5 00000289
DEBUG:	[tid 2522389]	[0.005453s - dmal/common/common_ops.c:45]	c1d08eb5 00000289 ## 0x0
DEBUG:	[tid 2522389]	[0.005463s - dmal/common/common_ops.c:43]	c1d08eb5 00000290
DEBUG:	[tid 2522389]	[0.005468s - dmal/common/common_ops.c:45]	c1d08eb5 00000290 ## 0x0
DEBUG:	[tid 2522389]	[0.005478s - dmal/common/common_ops.c:43]	c1d08eb5 00000214
DEBUG:	[tid 2522389]	[0.005491s - dmal/common/common_ops.c:45]	c1d08eb5 00000214 ## 0x0
DEBUG:	[tid 2522389]	[0.005496s - dmal/rm/rm_nvml.c:80]	0 0x6100 0 97 0
DEBUG:	[tid 2522389]	[0.007225s - dmal/common/common_mig.c:2276]	1b
DEBUG:	[tid 2522389]	[0.008874s - nvml.c:330]	Returning 0 (Success)
DEBUG:	[tid 2522389]	[0.009070s - entry_points.h:2412]	Entering nvmlDeviceGetCount_v2(unsigned int *deviceCount) (0x7ffecb617078)
DEBUG:	[tid 2522389]	[0.009079s - entry_points.h:2412]	Returning 0 (Success)
DEBUG:	[tid 2522389]	[0.009083s - entry_points.h:1866]	(0, 0x7ffecb617090, 34)
DEBUG:	[tid 2522389]	[0.009086s - entry_points.h:1866]	0 Success
DEBUG:	[tid 2522389]	[0.009089s - entry_points.h:2416]	Entering nvmlDeviceGetHandleByIndex_v2(unsigned int index, nvmlDevice_t *device) (0, 0x7ffecb617080)
DEBUG:	[tid 2522389]	[0.009093s - dmal/common/common_ops.c:43]	c1d08eb5 00000215
DEBUG:	[tid 2522389]	[0.009100s - dmal/common/common_ops.c:45]	c1d08eb5 00000215 ## 0x0
INFO:	[tid 2522389]	[0.009103s - dmal/common/common_nvml.c:821]	
INFO:	[tid 2522389]	[0.009107s - dmal/common/common_objects.c:247]	
DEBUG:	[tid 2522389]	[0.009109s - dmal/common/common_ops.c:43]	c1d08eb5 00000202
DEBUG:	[tid 2522389]	[0.009120s - dmal/common/common_ops.c:45]	c1d08eb5 00000202 ## 0x0
INFO:	[tid 2522389]	[0.009123s - dmal/common/common_flags.c:40]	0
INFO:	[tid 2522389]	[0.009125s - dmal/common/common_flags.c:45]	1
INFO:	[tid 2522389]	[0.009127s - dmal/common/common_flags.c:48]	0
INFO:	[tid 2522389]	[0.009128s - dmal/common/common_flags.c:51]	1
INFO:	[tid 2522389]	[0.009130s - dmal/common/common_flags.c:54]	0
INFO:	[tid 2522389]	[0.009132s - dmal/common/common_flags.c:57]	0
INFO:	[tid 2522389]	[0.009134s - dmal/common/common_flags.c:60]	24832
DEBUG:	[tid 2522389]	[0.009192s - dmal/common/common_ops.c:43]	a55a0000 00800289
DEBUG:	[tid 2522389]	[0.009202s - dmal/common/common_ops.c:45]	a55a0000 00800289 ## 0x0
DEBUG:	[tid 2522389]	[0.009249s - dmal/common/common_ops.c:43]	a55a0010 20800406
DEBUG:	[tid 2522389]	[0.009283s - dmal/common/common_ops.c:45]	a55a0010 20800406 ## 0x0
DEBUG:	[tid 2522389]	[0.014343s - dmal/common/common_ops.c:43]	a55a0010 20800406
DEBUG:	[tid 2522389]	[0.014380s - dmal/common/common_ops.c:45]	a55a0010 20800406 ## 0x0
DEBUG:	[tid 2522389]	[0.014385s - dmal/common/common_ops.c:43]	a55a0010 20801701
DEBUG:	[tid 2522389]	[0.014391s - dmal/common/common_ops.c:45]	a55a0010 20801701 ## 0x0
DEBUG:	[tid 2522389]	[0.014394s - dmal/common/common_nvml.c:1109]	170 2
DEBUG:	[tid 2522389]	[0.014397s - entry_points.h:2416]	Returning 0 (Success)
DEBUG:	[tid 2522389]	[0.014401s - entry_points.h:2424]	Entering nvmlDeviceGetName(nvmlDevice_t device, char* name, unsigned int length) (0x7f578f73bf38, 0x7ffecb6170c0, 64)
DEBUG:	[tid 2522389]	[0.014405s - dmal/common/common_ops.c:43]	a55a0010 20800110
DEBUG:	[tid 2522389]	[0.014410s - dmal/common/common_ops.c:45]	a55a0010 20800110 ## 0x0
DEBUG:	[tid 2522389]	[0.014422s - dmal/common/common_ids.c:42]	NVIDIA GeForce RTX 3080
DEBUG:	[tid 2522389]	[0.014425s - entry_points.h:2424]	Returning 0 (Success)
DEBUG:	[tid 2522389]	[0.014434s - entry_points.h:158]	Entering nvmlDeviceGetUUID(nvmlDevice_t device, char *uuid, unsigned int length) (0x7f578f73bf38, 0x7ffecb617100, 96)
DEBUG:	[tid 2522389]	[0.014438s - dmal/common/common_ops.c:43]	a55a0010 2080014a
DEBUG:	[tid 2522389]	[0.014450s - dmal/common/common_ops.c:45]	a55a0010 2080014a ## 0x0
DEBUG:	[tid 2522389]	[0.014453s - dmal/common/common_ids.c:352]	GPU-4032aa05-3eef-4d99-60e6-06c046db9a54
DEBUG:	[tid 2522389]	[0.014456s - entry_points.h:158]	Returning 0 (Success)
nvidia-smi stdout: GPU 0: NVIDIA GeForce RTX 3080 (UUID: GPU-4032aa05-3eef-4d99-60e6-06c046db9a54)
DEBUG:	[tid 2522389]	[0.014475s - entry_points.h:1284]	Entering nvmlDeviceGetMaxMigDeviceCount(nvmlDevice_t device, unsigned int *migDeviceCount) (0x7f578f73bf38, 0x7ffecb61707c)
DEBUG:	[tid 2522389]	[0.014480s - dmal/common/common_ops.c:43]	a55a0010 20800102
DEBUG:	[tid 2522389]	[0.014495s - dmal/common/common_ops.c:45]	a55a0010 20800102 ## 0x0
DEBUG:	[tid 2522389]	[0.014498s - entry_points.h:1284]	Returning 0 (Success)
DEBUG:	[tid 2522389]	[0.014503s - nvml.c:432]	Entering nvmlShutdown(void) ()
INFO:	[tid 2522389]	[0.014506s - nvml.c:457]	
DEBUG:	[tid 2522389]	[0.014663s - entry_points.h:2412]	Entering nvmlDeviceGetCount_v2(unsigned int *deviceCount) (0x7ffecb617154)
DEBUG:	[tid 2522389]	[0.014688s - entry_points.h:2412]	1 Uninitialized
DEBUG:	[tid 2522389]	[0.014743s - dmal/common/common_nvml.c:1209]	
DEBUG:	[tid 2522389]	[0.014751s - dmal/common/common_ops.c:43]	c1d08eb5 00000216
DEBUG:	[tid 2522389]	[0.014768s - dmal/common/common_ops.c:45]	c1d08eb5 00000216 ## 0x0
DEBUG:	[tid 2522389]	[0.014844s - nvml.c:497]	Returning 0 (Success)
```