import classes as c
'''Implemente uma função que transfira os dados de uma pilha S
para uma pilha T, de tal forma que o topo da pilha S seja o
primeiro elemento da pilha T, e o último elemento de S seja
o topo da pilha T.'''

def trnsfstk(s, t):
    r = c.Stack(s.Capacity)
    r.push(s.pop())
    print(r.peek(), s.peek())
    return s, t