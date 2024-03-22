import classes as c
import func as f

#Implemente uma função que transfira os dados de uma pilha S para uma pilha T,
#de tal forma que o topo da pilha S seja o primeiro elemento da pilha T, e o
#último elemento de S seja o topo da pilha T.


def f(s, t):
    aux = c.Stack()
    aux2 = c.Stack(s.Capacity-1)
    aux3 = c.Stack(t.Capacity)

    aux.push(s.pop())
    while s.isEmpty != False:
        aux2.push(s.pop())
    while t.isEmpty != False:
        aux3.push(t.pop())
    t.push(aux2.pop())
    
    for i in range (t.Capacity-2):
        t.push(aux3.pop())
    t.push(aux.pop())
    while aux2.isEmpty != False:
        s.push(aux2.pop())

s = c.Stack(5)
t = c.Stack(5)

for i in range(3):
    s.push(5)