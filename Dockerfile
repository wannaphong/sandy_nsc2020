FROM balenalib/raspberrypi3-python:3.6-latest

ENTRYPOINT []

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get -y install git sox swig3.0 python3-pyaudio libatlas-base-dev libportaudio-dev python3-dev python3-pip ffmpeg libavcodec-extra libopenblas-dev python3-scipy libhdf5-dev python3-h5py python3-numpy

RUN pip install cython

WORKDIR /root/  

COPY src/* /root/service/

RUN pip install -r /root/service/requirements.txt

WORKDIR /root/service/thaitts
RUN pip install -e .

WORKDIR /root/service/pyvadrun
RUN pip install -e .

WORKDIR /root/service

RUN [ "cross-build-end" ]

CMD [ "python", "run.py"]
