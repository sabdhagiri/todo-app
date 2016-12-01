##################################################
#
#  Dockerfile to build todo-app demo application
#
#################################################
# Set base image to centos
FROM python:2.7

MAINTAINER "OneCloud Consulting Inc. <sabdhagiri@onecloudinc.com>"

COPY . /todo-app
WORKDIR /todo-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 6488





