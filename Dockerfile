FROM alpine:3.7
RUN apk add --update \
    python2 \
    python2-dev \
    py2-pip \
    build-base \
    libusb \
&& pip install nfcpy \
&& pip install luigi \
&& pip install requests \
&& pip install google-cloud-datastore \
&& adduser -S librarian
USER librarian
WORKDIR /home/librarian
COPY . .
