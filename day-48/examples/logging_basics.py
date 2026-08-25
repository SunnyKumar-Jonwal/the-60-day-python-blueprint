import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logging.debug("Debug detail for developers")
logging.info("Starting the process")
logging.warning("Config file not found, using defaults")
logging.error("Failed to connect to the database")
logging.critical("Out of memory, shutting down")

logging.getLogger().setLevel(logging.WARNING)
logging.info("This is now suppressed, level was raised to WARNING")
logging.warning("This still shows")

file_logger = logging.getLogger("file_demo")
file_logger.setLevel(logging.INFO)
file_logger.propagate = False  # don't also send these up to root's console handler
handler = logging.FileHandler("day-48/examples_app.log")
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
file_logger.addHandler(handler)

file_logger.info("This goes to the file, not the console")

with open("day-48/examples_app.log") as file:
    print(file.read())

named_logger = logging.getLogger(__name__)
named_logger.setLevel(logging.INFO)
named_logger.info("Using a named logger")
