FROM STARK/STARK_USERBOT:latest

# نسخ رابط السورس 
RUN git clone https://github.com/STARK-LUCIFER/STARK_USERBOT.git /root/userbot
# اخـراج العـمل 
WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r resources/setup/requirements.txt

ENV PATH="/home/userbot/resources/setup/bin:$PATH"

CMD ["python3","-m","userbot"]
