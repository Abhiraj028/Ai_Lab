import random

def f(x):
    return x**2

def hillClimb(f,choice_range,step,max_iter = 1000):
    chosen = random.choice(choice_range)
    print(chosen)
    for i in range(max_iter):
        neighbors = [chosen+s for s in[-step,0,step]]
        neighbors = [n for n in neighbors if n >= min(choice_range) and n <= max(choice_range)]
        if not neighbors:
            break
        max_neighbor = max(neighbors, key = lambda x:f(x))
        if(max_neighbor <= chosen):
            break
        chosen = max_neighbor
    return chosen,f(chosen)

if __name__ == "__main__":
    start = int(input("Enter the start value:"))
    end = int(input("Enter the end value:"))
    step = float(input("Enter the step value:"))
    choice_range = [n for n in range(start,end+1)]
    max_val, max_output = hillClimb(f,choice_range,step)
    print("Max Value = ",round(max_val,3),"Max Output: ",round(max_output,3))
