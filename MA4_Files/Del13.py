'''
Student: David Hovstadius
Presented too: Nandini M S
Presentation date: 14/10-2022

'''
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
from unittest import result
from Del12 import Dspherevol




# def runner():
#     print("Performing a costly function")
#     result = Dspherevol(10000000, 11)
#     print("Function complete")
#     return result

# if __name__ == "__main__":
#     start = pc()
#     r = runner()
#     print(r)
#     end = pc()
#     print(f"Process took {round(end-start, 2)} seconds")

def runner(n):
    print(f"Performing a costly function {n}")
    result = Dspherevol(1000000, 11)
    print(f"Function {n} complete")
    return result


if __name__ == "__main__":
    start = pc()
    
    with future.ProcessPoolExecutor() as ex:
        p = [1,2,3,4,5,6,7,8,9,10]
        results = ex.map(runner,p)
        for r in results:
            ans = sum(results)/len(p)
            print(ans)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

'''
Dspherevol(10000000, 11)
answer = 1.8812928
Process took 97.58 seconds


Dspherevol(1000000,11) with 10 processes
ans = 1.7328128
Processes took 69.92s

'''

