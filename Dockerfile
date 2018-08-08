FROM ubuntu
RUN apt-get update && apt-get -y upgrade \
&& apt install -y --no-install-recommends \
    dpkg-dev \
    python-dev \
    python-pip \
    python-setuptools \
    usbutils \
    libnfc-dev \
    udev \
&& apt autoremove -y && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \
&& pip install wheel \
&& pip install nfcpy \
&& pip install luigi \
&& pip install requests \
&& pip install google-cloud-datastore \
&& groupadd -r librarian \
&& useradd -r -g librarian librarian \
&& gpasswd -a librarian plugdev \
&& sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
USER librarian
WORKDIR /home/librarian
COPY --chown=librarian:librarian . .
