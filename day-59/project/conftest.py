import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

# Other days (e.g. day-57's examples) also have a module literally named
# "main" -- if pytest already cached one of those under sys.modules["main"]
# before this directory's tests run, "from main import app" below would
# silently import the WRONG app. Force a fresh import scoped to this folder.
for _name in ("main", "models", "repository", "routers", "routers.books"):
    sys.modules.pop(_name, None)

TEST_DB = "day-59/project/test_library.db"
if os.path.exists(TEST_DB):
    os.remove(TEST_DB)

os.environ["DB_PATH_OVERRIDE"] = TEST_DB
