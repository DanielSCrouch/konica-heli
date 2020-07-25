FROM python
WORKDIR /usr/app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "app.py"]

# docker build -t duartcs/heliserver:latest .
# docker run -it duartcs/heliserver sh
