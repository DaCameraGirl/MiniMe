# Ford-Fulkerson Documentation Rubric

### Implementation Correctness (40 points)
1. Creates virtual super-source (S) connecting A,B and super-sink (T) from E,F (+8)
2. Implements residual edges with capacity formula: residual[u][v] = graph[u][v] - flow[u][v] (+7)
3. Shows augmenting path discovery steps for sample graph (A->B->E->F path first) (+6)
4. Calculates max flow as 30 (15 from A->B->E->F + 15 from A->C->E->F) (+10)
5. Handles zero-capacity edges by excluding them from residual paths (+5)
6. Includes time complexity analysis: O(E * max_flow) for DFS, O(VE²) for BFS (+4)

### Code Quality (30 points)
1. Uses adjacency matrix with capacity values matching sample graph edges (+6)
2. Implements path backtracking with parent pointer array (+5)
3. Includes validation test for flow conservation: Σin = Σout except S/T (+5)
4. Provides 3 test cases: 
   - Single source/sink (score 25)
   - Multiple sources (score 30)
   - Cyclic graph (score 15) (+8)
5. Benchmarking setup with time/space metrics for 1000-node graphs (+6)

### Documentation Standards (30 points)
1. Includes SVG/ASCII diagram of residual graph at each augmentation step (+8)
2. Compares DFS stack vs BFS queue implementations in performance table (+6)
3. Lists 3 real-world applications: network routing, airline scheduling, bipartite matching (+5)
4. Provides 2 practice problems:
   - Modify for vertex capacities
   - Handle dynamic edge updates (+7)
5. Cites 3 academic sources including Cormen et al. (+4)

### Critical Errors (-40 points)
1. Missing super-node handling (directly uses original sources/sinks) (-12)
2. Fails to update backward edges in residual graph (-10)
3. Allows negative flow values in calculations (-8)
4. Omits bottleneck calculation in augmenting paths (-6)
5. Uses incorrect O-notation (e.g. claims O(E)) (-4)
