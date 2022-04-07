FROM ubuntu:latest
LABEL "Author"="Deepak"
LABEL "Project"="Calculator"
RUN apt update && apt install git -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install django
RUN pip install django_jenkins
WORKDIR /home
EXPOSE 8000
RUN git init
RUN git pull https://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@github.com/deeplearn-optimizer/calculator.git
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
