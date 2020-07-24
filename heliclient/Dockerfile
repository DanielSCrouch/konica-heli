FROM python
WORKDIR /usr/app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "helicopter.py"]
# docker build -t duartcs/heliclient:latest . 
# docker run -it duartcs/heliclient sh
