FROM python:3.6
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ENV LASER /LASER
ENV PATH /root/miniconda/bin:/root/miniconda/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
WORKDIR /
RUN git clone https://github.com/facebookresearch/LASER.git
ADD setup_LASER.sh /
RUN ["chmod", "+x", "/setup_LASER.sh"]
RUN /setup_LASER.sh
ADD sentance_encoder_test.py /LASER/source/
ENTRYPOINT [ "bash" ]