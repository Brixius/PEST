# PEST
Python implementation of PEST (Taylor &amp; Creelman, 1967).

PEST rules from the paper:

"
1. On every reversal of step direction, halve the step size. 

2. The second step in a given direction, if called for, is the same size as the first. 

3. The fourth and subsequent steps in a given direction are each double their predecessor (except that, as noted above, large steps may be disturbing to a human observer and an upper limit on permissible step size may be needed). 

4. Whether a third successive step in a given direction is the same as or double the second depends on the sequence of steps leading to the most recent reversal.  If the step immediately preceding that reversal resulted from a doubling, then the third step is not doubled, while if the step leading to the most recent reversal was not the result of a doubling, then this third step is double the second.
"
