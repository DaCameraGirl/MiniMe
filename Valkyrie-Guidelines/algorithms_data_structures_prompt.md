I'm documenting the Ford-Fulkerson algorithm for our engineering team's knowledge base. Need to explain how it handles multiple source/sink scenarios and validate my Python implementation. The example graph I'm using has these edges:
A->B:15, A->C:10, B->D:5, B->E:15, C->E:10, D->F:10, E->F:15

Should I use the standard implementation or modify residual graph handling? My current version fails to find the max flow when sources/sinks are unbalanced.
