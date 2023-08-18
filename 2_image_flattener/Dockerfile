FROM reidm512/opencv:1.0

# Add our own code.
ADD image_flattener.py /image_flattener.py
ADD requirements.txt /requirements.txt

#ENV OPENCV_LOG_LEVEL=debug
#ENV OPENCV_VIDEOIO_DEBUG=1
RUN sudo pip3 install -r requirements.txt
