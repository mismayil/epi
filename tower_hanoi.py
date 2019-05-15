NUM_PEGS = 3

def computeTowerHanoi(n):
    pegs = [list(reversed(range(1, n+1)))] + [[] for _ in range(1, NUM_PEGS)]
    computeTowerHanoiSteps(n, pegs, 0, 1, 2)

    for i in range(NUM_PEGS):
        peg = pegs[i]
        print('peg {}'.format(i))

        while len(peg) != 0:
            print(peg.pop())

def computeTowerHanoiSteps(n, pegs, from_peg, to_peg, use_peg):
    if n > 0:
        computeTowerHanoiSteps(n-1, pegs, from_peg, use_peg, to_peg)
        ring = pegs[from_peg].pop()
        pegs[to_peg].append(ring)
        print('Move {} from peg {} to peg {}'.format(ring, from_peg, to_peg))
        computeTowerHanoiSteps(n-1, pegs, use_peg, to_peg, from_peg)

n = int(input('Enter tower size: '))
computeTowerHanoi(n)
