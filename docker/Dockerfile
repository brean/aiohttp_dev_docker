FROM ubuntu:18.10

# install and update pip
RUN apt-get -y update && \
    apt-get install -q -y \
    python3-pip \
    python3-venv \
    gnupg2

# apt cleanup
RUN rm -rf /var/lib/apt/lists/

EXPOSE 4000
EXPOSE 4001

COPY entrypoint.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/entrypoint.sh

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
