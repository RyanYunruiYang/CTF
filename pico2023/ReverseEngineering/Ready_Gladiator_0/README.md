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

This solution works. I'm not entirely sure *why* to be honest. My intuition, mostly gleaned from the internet, is that the Imp wins by having a dense set of itself, and each round all of them copy over to each other, thus allowing for self-healing. Increasing the step size weakens this effect.

However, I think if the buffersize has size $n$, then strategies with size $k$ where $\gcd(k,n) = 1$ should all probably be isomorphic? Idk.

```
picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}
```