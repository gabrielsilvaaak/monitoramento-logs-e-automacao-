import time
import datetime

while True:
    with open("logs.txt", "a") as log:
        log.write(f"Monitoramento ativo: {datetime.datetime.now()}\n")
    print("Log registrado...")
    time.sleep(5)
