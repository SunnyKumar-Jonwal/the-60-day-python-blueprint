import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

# Other days (e.g. day-59's capstone) also have a module literally named
# "main" -- if pytest already cached one of those under sys.modules["main"]
# before this directory's tests run, "from main import app" below would
# silently import the WRONG app. Force a fresh import scoped to this folder.
sys.modules.pop("main", None)

TEST_DB = "day-57/examples/test.db"
if os.path.exists(TEST_DB):
    os.remove(TEST_DB)

os.environ["DB_PATH_OVERRIDE"] = TEST_DB
