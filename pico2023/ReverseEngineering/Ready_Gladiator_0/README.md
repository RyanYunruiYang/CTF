# Setup 
In this challenge, we are tasked with creating a CoreWars warrior that always loses. CoreWars was first introduced to the world in May 1984, and involves two sides writing low-level code attempting to cause the other side to "die." Dying occurs if the program (warrior) executes or an illegal instruction or if it executes an instruction that results in an error.

One primitive that is often used as part of larger CodeWars strategies is the "Imp." This following block of code has three liens of comments (the semicolons), and the imp consists of the single line `mov 0, 1`. This moves the program from address 0 (current) to address (1), while keeping the original, marching forwards and continuously multiplying itself until it fills the entire core. 

```
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

# Solution
```
;redcode
;name MyBadImp
;assert 1
mov 0, 100
end
``` 

This solution works. In theory, if the buffersize has size $n$, then strategies with size $k$ where $\gcd(k,n) = 1$ feel like they *should* all probably be isomorphic. After all, you can reindex each memory location $nk \mapsto n$.

However, when  you invert, then the 1-Imp strategy seems to always map just perfectly. We refer to the imp that steps $k$ at a time as a k-Imp.

The reason why the 100-Imp loses is because it is too spread out. The 100-Imp will claim the addresses $100, 200,\ldots$ which will all defend each other. Similarly, the 1-Imp will travael to $1,2,\ldots$. Let the tails of the imp be any address that the $k$-Imp owns but where it doesn't own the position $k$ before. The question then becomes, who can eat the other person's tail, because everything else is reinforced. The 1-Imp does this first because it takes 100 rounds for it to hit the 100-Imp's tail, whereas the 100-imp needs $x$ rounds where $100x \equiv 1 \pmod{n}$ (which in fact never happens since $n=8080$!). Thus, the 100-Imp runs around the core rarely ever managing to make a dent in the 1-Imp's single, contiguous block, which only has one weak point that it recovers anyways in the next round, while the 100-Imp is slowly eaten.

```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}
```