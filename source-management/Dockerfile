# from https://github.com/blang/latex-docker/blob/42d2c532a09a00938331512fd2b539f9944c400c/Dockerfile.ubuntu
FROM ubuntu:jammy
MAINTAINER Benedikt Lang <mail@blang.io>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && apt-get install -qy \
    texlive-full \
    python3-pygments gnuplot \
    make git \
    && rm -rf /var/lib/apt/lists/*

# Prebuild font cache for lualatex
RUN luaotfload-tool -v -u

WORKDIR /data
VOLUME ["/data"]
