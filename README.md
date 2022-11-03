## Parallel Cost Distance and Inverse Distance Weighting


Fast_cd_idw is a parallel tool to calculate parallel the Cost Distance (CD) and Inverse Distance Weighting (IDW) metrics. This tool was developed entirely in C++ and can efficiently scale on large input rasters.

The parallel implementation was coded using two parallel approaches. 1) CPU architectures on a single server using OpenMP, which also supports the Message Passing Interface (MPI) to run it into a distributed computing cluster, and 2) Multi-Graphics Processing Units (GPUs) architectures using the CUDA platform. This module is currently under development (testing process). 


## 1. Installation
### 1.1. Software Requierements
This tool was tested using the following libraries:
> + GDAL V2.4.2 [See installation](https://gdal.org/index.html)
> + TCLAP V1.2.5 [See installation](https://tclap.sourceforge.net/)
> + OpenMP V4.5 [See installation](https://www.openmp.org/)

## 2. Usage
This tool was initially designed to run as a command-line application. It can be used in a computing cluster or via a web-based platform. It required only three parameters 
+ A friction raster map  (.tif) *-f* 
+ A localities raster file (.tif) *-l* 
+ A demmand file (.csv) *-d*

**Example of usage**
``` 
bash fast_idw_cd -f <path_to_friction/fricction.tif> -l <path_to_locs/locs.tif> -d <path_to_demmand/demmand.csv>

``` 



