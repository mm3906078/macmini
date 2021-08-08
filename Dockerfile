FROM python:3.9.1-alpine
RUN pip3 install fake-useragent
RUN pip3 install smtplib
RUN pip3 install requests
RUN pip3 install bs4
WORKDIR /app
COPY . .
CMD [ "python3","/app/macmini.py" ]