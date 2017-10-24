FROM ubuntu:15.04
RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils
RUN apt-get install -y vim
RUN apt-get clean

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
