import random

def ListOverlay():
    a=random.sample(range(1,50),10)
    print(a);
    b=random.sample(range(1,50),7)
    print(b);

    for x in a:
        if x in b:
            print(x); 
ListOverlay()