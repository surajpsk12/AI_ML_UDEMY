import time 
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    t=time.time()
    thread1.start()
    thread2.start()

    thread1.join() # Wait for thread1 to finish before proceeding
    thread2.join() # Wait for thread2 to finish before proceeding 

    print("Done!")
    print(f"Execution time: {time.time() - t} seconds")
