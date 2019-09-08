from startup_check import startup_check
from drive import get_worksheet, get_last_n_rows

startup_check()

ws = get_worksheet()

rows = get_last_n_rows(ws, 10)

print(rows)