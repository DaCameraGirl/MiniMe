# Algorithm Documentation Rubric

### Core Criteria
1. Correctly identifies the need for a super-source/super-sink approach (+8)
2. Implements residual graph updates properly with path backtracking (+7)
3. Handles edge cases with zero-capacity edges and cyclic paths (+6)
4. Includes time complexity analysis distinguishing O(E|f*|) vs O(VE²) cases (+5)

### Quality Differentiators
1. Compares BFS (Edmonds-Karp) vs DFS approaches (-3 if missing)
2. Provides test cases with asymmetric source/sink configurations (+4)
3. Diagrams showing residual graph transformations (+3)

### Critical Errors
1. Fails to handle backward edges in residual graph (-6)
2. Allows flow conservation violations at regular nodes (-8)
3. Incorrectly reports max flow for given example graph (-10)
