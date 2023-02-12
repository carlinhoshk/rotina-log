import psutil
import time

while True:
    processes = []
    for process in psutil.process_iter():
        processes.append(process.as_dict(attrs=['pid', 'name', 'cpu_percent']))
        
    with open("process_log.txt", "a") as file:
        for process in processes:
            file.write(str(process) + "\n")
        
    print("Pausa por 180 segundos (3 minutos)")
    time.sleep(180)
    
