import time

def send_emails():
    for i in range(100000):
        pass

start = time.time()
send_emails()
end = time.time()
duration = start - end
print(duration)