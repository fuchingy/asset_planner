FROM python:3.6.5
MAINTAINER Fu-Ching Yang "fcyangesl@gmail.com"

# system packages for general use
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    sudo \
    tcsh \
    bash

# copy pre-generated config files
COPY cfg/start.sh      /home/
COPY cfg/launch_app.sh /tmp/

# Software for Dash deployment
RUN apt-get -y install \
    vim \
    nginx
RUN mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
COPY cfg/default /etc/nginx/sites-available/

# Software for Flask cache
RUN apt-get -y install redis-server

# install python package dependencies of the app
RUN pip install --upgrade pip
RUN pip install pandas && \
    pip install feather-format && \
    pip install flask-caching && \
    pip install Flask-Session && \
    pip install redis && \
    pip install plotly && \
    pip install sklearn && \
    pip install flask-cors && \
    pip install palettable && \
    pip install matplotlib

# For remove numpy warning message
# https://stackoverflow.com/questions/40845304/runtimewarning-numpy-dtype-size-changed-may-indicate-binary-incompatibility
RUN pip install numpy==1.15.1

# For Dash deployment
RUN pip install gunicorn

EXPOSE 8050

CMD ["bash", "/home/start.sh"]
