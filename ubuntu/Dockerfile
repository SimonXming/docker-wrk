# Docker image for wrk
#
FROM       ubuntu:16.04
MAINTAINER SimonShyu <simonshy2@gmail.com>

COPY sources.list /etc/apt/sources.list

RUN set -ex && \
    echo "===> Installing  tools..."  && \
    apt-get -y update && \
    apt-get -y install build-essential curl && \
    apt-get -y install lua5.1 lua-cjson && \
    \
    echo "===> Installing wrk" && \
    WRK_VERSION=4.0.2 && \
    echo $WRK_VERSION && \
    mkdir /opt/wrk && \
    cd /opt/wrk && \
    curl -L https://github.com/wg/wrk/archive/$WRK_VERSION.tar.gz | \
       tar zx --strip 1 && \
    make && \
    cp wrk /usr/local/bin/ && \
    \
    echo "===> Cleaning the system" && \
    apt-get -f -y --auto-remove remove build-essential curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/wrk/

ENV LUA_CPATH /usr/lib/x86_64-linux-gnu/lua/5.1/?.so;;

WORKDIR /opt
ENTRYPOINT ["wrk"]
