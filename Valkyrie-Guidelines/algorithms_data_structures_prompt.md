Debugging my Ford-Fulkerson implementation for a supply network optimization problem. The system has multiple factories (A,B) and distribution centers (E,F) with these pipeline capacities:
A->B:15k units/day
A->C:10k 
B->D:5k
B->E:15k
C->E:10k  
D->F:10k
E->F:15k

My code works for single sources but fails with multiple. Current output shows 25k max flow instead of expected 30k. Should I stick with standard residual graphs or need special handling for multi-source setups?
