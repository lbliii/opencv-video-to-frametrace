FROM ubuntu:22.04

ENV OPENCV_VERSION=4.8.0
# Fix timezone issue
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install opencv and matplotlib.
RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections; \
    apt-get update -qqy \
    && apt-get install -qqy make git pkg-config libswscale-dev python3-dev \
    	python3-numpy python3-tk libtbb2 libtbb-dev libjpeg-dev libpng-dev \
    	libtiff-dev bpython python3-pip libfreetype6-dev wget unzip cmake \
      ffmpeg sudo \
      libgstreamer1.0-dev \
      libgstreamer-plugins-base1.0-dev \
      libgstreamer-plugins-bad1.0-dev \
      gstreamer1.0-plugins-base \
      gstreamer1.0-plugins-good \
      gstreamer1.0-plugins-bad \
      gstreamer1.0-plugins-ugly \
      gstreamer1.0-libav \
      gstreamer1.0-tools \
      gstreamer1.0-x \
      gstreamer1.0-alsa \
      gstreamer1.0-gl \
      gstreamer1.0-gtk3 \
      gstreamer1.0-qt5 \
      gstreamer1.0-pulseaudio \
    && apt-get clean \
    && rm -rf /var/lib/apt

RUN cd \
	&& wget https://github.com/opencv/opencv/archive/refs/tags/$OPENCV_VERSION.zip \
	&& unzip $OPENCV_VERSION.zip \
	&& cd opencv-$OPENCV_VERSION \
	&& mkdir build \
	&& cd build \
	&& cmake -D WITH_FFMPEG=ON -D WITH_GSTREAMER=ON .. \
	&& make -j6 \
	&& make install \
	&& cd \
	&& rm $OPENCV_VERSION.zip \
    && rm -rf opencv-$OPENCV_VERSION
RUN python3 --version && pip3 --version && sudo pip3 install matplotlib \
      && sudo pip3 install opencv-python

# Debug switches for OpenCV
#ENV OPENCV_LOG_LEVEL=debug
#ENV OPENCV_VIDEOIO_DEBUG=1