import logging

logging.basicConfig(level=logging.INFO, filename="day-48/exercises_app.log")

logging.info("First message")
logging.info("Second message")

with open("day-48/exercises_app.log") as file:
    print(file.read())
