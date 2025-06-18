# Ford-Fulkerson Algorithm Rubric

## Core Criteria (Weight 6-10)
1. [Accuracy] Implements super-source/super-sink correctly with ∞ capacity (Explicit, Objective) (+8)
2. [Completeness] Includes all residual graph transformations for sample input (Explicit, Objective) (+7)
3. [Instruction Following] Calculates correct max flow of 30k units/day (Explicit, Objective) (+10)
4. [Context Awareness] Handles multiple sources via virtual super-node pattern (Implicit, Objective) (+6)

## Quality Enhancements (Weight 1-5)
1. [Communication Quality] Diagrams show residual capacity changes at each step (Implicit, Objective) (+5)
2. [Completeness] Benchmarks include 1000-node stress test (Explicit, Objective) (+4)
3. [Context Awareness] Compares DFS/BFS tradeoffs in real-world scenarios (Implicit, Subjective) (+3)

## Negative Weights
1. [Accuracy] Missing backward edge updates in residual graph (-10)
2. [Instruction Following] Uses original sources instead of super-node (-12)
3. [Accuracy] Allows negative flow values in calculations (-8)
4. [Completeness] Omits bottleneck detection in augmenting paths (-6)

## Evaluation Scale
**Excellent:** 85+ points - Exceeds all core requirements  
**Proficient:** 70-84 points - Meets requirements with minor gaps  
**Developing:** 50-69 points - Partial fulfillment with notable issues  
**Missing:** <50 points - Fundamental flaws present
