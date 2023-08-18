# OpenCV Image for Pachyderm Pipelines
This directory is for building the OpenCV source image for the upper directory.

## Building

You will need to adjust the `cmake` `-j` switch to allow compilation to
succeed. When using all CPUs, the build usually fails from lack of RAM, even with
over 50GB of RAM allocated and nothing else running in Docker.

Use a value of 1/2 the number of CPUs allocated to Docker, and a substantial
portion of available RAM allocated to Docker for this build to succeed. I needed
to reduce the 16 available CPUs to only 8 in order for OpenCV to compile
successfully. YMMV, so you may have to further de-tune the parallelism to get
a good build.

Example build command on my M1 based macOS system:

    docker buildx build --platform linux/amd64 -t lbliii/opencv:2.0.1 --push .
