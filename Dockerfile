FROM ubuntu:xenial

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN groupadd -r judge && useradd -r -g judge judge
RUN apt-get update && apt-get install --no-install-recommends -y openjdk-8-jdk

RUN apt-get install -y --no-install-recommends python python2.7-dev python3 python3-pip gcc g++ wget file && apt-get clean
RUN wget -q --no-check-certificate -O- https://bootstrap.pypa.io/get-pip.py | python && \
    pip install --no-cache-dir pyyaml watchdog cython ansi2html termcolor && \
    rm -rf ~/.cache

COPY . /judge
WORKDIR /judge

RUN cd ../judge
RUN pip install -r requirements.txt

RUN mkdir /problems


RUN pip install setproctitle
RUN pip install pygments
RUN env DMOJ_REDIST=1 python setup.py develop && rm -rf build/

