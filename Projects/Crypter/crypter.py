"""Scrie un program care cripteaza fisiere text folosind diferiti algortmi.
Fisierele criptate vor contine pe prima linie numele clasei (cifrului) pentru a facilita decriptarea"""

# Logging:
# mesaje de DEBUG
# mesaje de INFO
# Warning
# ERRORS
# CRITICAL


import sys
import pathlib
from exceptions import ArgvException, NotATextFile, CrypterBaseException
import logging
from ciphers import Caesar

ROOT = pathlib.Path(__file__).parent
LOGS_DIR = ROOT / "logs"

try:
    LOGS_DIR.mkdir(exist_ok=True)
except OSError:
    logs_file_name = None
else:
    logs_file_name = LOGS_DIR / "log.log"

# logging.root.setLevel(logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s [line: %(lineno)d] %(message)s",
    filename=logs_file_name
)


def get_file_text(path):
    with open(path) as fin:
        content = fin.read()
    return content


def get_path_from_argv():
    if len(sys.argv) == 1:
        raise ArgvException("Error: argument PATH not found")

    path = pathlib.Path(sys.argv[1])
    if not path.is_file():
        raise NotATextFile(f"Error: there is no such file {sys.argv[1]}")

    return path


try:
    logging.info(get_path_from_argv())
except CrypterBaseException as err:
    logging.error(err)


def write_message_to_file(message, file_name):
    with open(f"_{file_name}", "w") as fin:
        fin.write(message)


# def crypt(msg, cypher):
#     pass

msg = get_file_text(get_path_from_argv())
cipher = Caesar(18)
write_message_to_file(cipher.crypt(msg), get_path_from_argv())

# write encrypted message in a txt file (acelasi nume dar cu _in fata: _practice.txt)
# logging
