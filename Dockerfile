FROM balenalib/raspberrypi3-python:3.7-latest

ENTRYPOINT []

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get -y install build-essential

RUN apt-get -y install libatlas3-base libgfortran5 vlc cython3 pkg-config git sox swig3.0 python3-matplotlib python3-pyaudio libatlas-base-dev libportaudio-dev python3-dev ffmpeg libavcodec-extra libopenblas-dev python3-scipy libhdf5-dev python3-h5py

WORKDIR /root/  

COPY src/* /root/service/

RUN python -m pip install -U pip

RUN pip install --extra-index-url https://www.piwheels.org/simple -r /root/service/requirements-pi.txt

WORKDIR /root/service/thaitts
RUN pip install -e .

WORKDIR /root/service/pyvadrun
RUN pip install -e .

WORKDIR /root/service

RUN [ "cross-build-end" ]

CMD [ "python", "run.py"]
