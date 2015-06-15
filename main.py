__author__ = 'Slawek'

import random as rand
import time
import numpy as np


def bubble_sort(tab):
    n = len(tab)
    while n > 1:
        for t in range(n-1):
            if tab[t] > tab[t+1]:
                (tab[t], tab[t+1]) = (tab[t+1], tab[t])
                n = len(tab)
        n -= 1
    return tab


def selection_sort(tab):
    for n in range(len(tab)-1):
        minimum = n
        for i in range(n+1, len(tab)):
            if tab[i] < tab[minimum]:
                minimum = i
        if minimum != n:
            (tab[n], tab[minimum]) = (tab[minimum], tab[n])
    return tab


def quick_sort(tab):
    if len(tab) < 2:
        return tab
    head, *tail = tab
    less = quick_sort([i for i in tail if i < head])
    more = quick_sort([i for i in tail if i >= head])
    return less + [head] + more


def main():
    tab = [rand.randint(-500, 500) for _ in range(1000)]
    print("Bubble sort")
    start = time.time()
    print(bubble_sort(np.copy(tab)))
    end = time.time()
    print("Czas: {}".format(end - start))
    print()

    print("Selection sort")
    start = time.time()
    print(selection_sort(np.copy(tab)))
    end = time.time()
    print("Czas: {}".format(end - start))
    print()

    print("Quick sort")
    start = time.time()
    print(quick_sort(np.copy(tab)))
    end = time.time()
    print("Czas: {}".format(end - start))


if __name__ == "__main__":
    import sys
    sys.exit(main())