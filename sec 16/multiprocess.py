import multiprocessing as mp
import time 

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)

if __name__ == "__main__":
    process1 = mp.Process(target=print_numbers)
    process2 = mp.Process(target=print_letters)
    t=time.time()
    process1.start()
    process2.start()

    process1.join() # Wait for process1 to finish before proceeding
    process2.join() # Wait for process2 to finish before proceeding 

    print("Done!")
    print(f"Execution time: {time.time() - t} seconds")
    