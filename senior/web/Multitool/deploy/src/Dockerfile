FROM disconnect3d/nsjail:3.0

ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf


RUN apt-get update
RUN apt-get install -y python3 python3-pip
# cal
RUN apt-get install -y bsdmainutils 

ENV PYTHONUNBUFFERED 1

WORKDIR /chroot/
COPY ./app/ ./app/
WORKDIR ./app/

RUN pip3 install -r requirements.txt

WORKDIR /chroot/

RUN mkdir -p ./usr/lib/ && \
    cp -R /lib* . && \
    cp -R /usr/lib* ./usr/
#    cp -R /usr/lib* ./usr/ && \
#    mkdir -p ./usr/local/lib && \
#    cp -R /usr/local/lib/python* ./usr/local/lib

RUN mkdir ./dev && \
    mknod ./dev/null c 1 3 && \
    mknod ./dev/zero c 1 5 && \
    mknod ./dev/random c 1 8 && \
    mknod ./dev/urandom c 1 9 && \
    chmod 666 ./dev/*

RUN mkdir -p ./bin/ && \
    cp /bin/sh \
       /bin/ls \
       /bin/cat \
       /bin/pwd \
       /bin/date \
       /bin/echo \
       ./bin/ && \
    ln -s /bin/sh ./bin/bash && \
    chmod 111 ./bin/*

#RUN mkdir -p ./usr/bin/ && \
#    cp /usr/bin/id \
RUN cp /usr/bin/id \
       /usr/bin/whoami \
#       /usr/bin/python3 \
       /usr/bin/uptime \
       /usr/bin/cal \
       /usr/bin/env \
       ./bin/
#       ./bin/ && \
#    chmod 111 ./usr/bin/*

RUN mkdir ./etc/ && \
    cp /etc/passwd ./etc/ && \
    chmod 444 ./etc/*

RUN mkdir ./tmp/ && \
    chmod 777 ./tmp/ && \
    chmod +t ./tmp/

WORKDIR /
ADD nsjail/nsjail.sh /nsjail.sh
RUN chmod 555 /nsjail.sh

WORKDIR /chroot/app/

RUN chmod 444 ./flag.txt

RUN touch ./rm_me.txt

#ENTRYPOINT ["/nsjail.sh" ]
#CMD [ "which", "cat"]
#WORKDIR /app/
#CMD [ "/usr/bin/python3", "server.py" ]

#ENV FLASK_APP=server.py
#ENV FLASK_ENV=development
#CMD [ "gunicorn", "-b", "0.0.0.0:5656", "-w", "4", "wsgi:app" ]
CMD [ "python3", "server.py"]
