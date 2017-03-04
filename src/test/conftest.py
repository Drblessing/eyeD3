import shutil
import pytest
import eyed3
from uuid import uuid4
from pathlib import Path


DATA_D = Path(__file__).parent / "data"


@pytest.fixture(scope="function")
def audiofile(tmpdir):
    """Makes a copy of test.mp3 and loads it using eyed3.load()."""
    testmp3 = DATA_D / "test.mp3"
    testfile = Path(str(tmpdir)) / "{}.mp3".format(uuid4())
    shutil.copyfile(str(testmp3), str(testfile))
    yield eyed3.load(testfile)
    if testfile.exists():
        testfile.unlink()


@pytest.fixture(scope="function")
def id3tag():
    """Returns a default-constructed eyed3.id3.Tag."""
    from eyed3.id3 import Tag
    return Tag()
