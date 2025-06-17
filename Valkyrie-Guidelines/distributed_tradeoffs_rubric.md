Strict Prompt Rubric:
[+10] Response compares coordination mechanisms (e.g. quorum writes, consensus protocols) in strong consistency vs conflict resolution approaches (e.g. vector clocks, CRDTs) in eventual 
[+10] Response provides specific latency percentiles (P50/P99) comparisons for both models under normal and partition conditions
[+8] Response details monitoring/diagnostics tools needed for each model (e.g. consistency metrics for eventual, quorum health for strong)
[+8] Response cites 2+ production examples with concrete metrics (e.g. "DynamoDB achieves 15ms P99 reads with eventual consistency")
[+5] Response analyzes throughput impact comparing both models
[+5] Response addresses the 1s staleness tolerance requirement
[-10] Response claims perfect consistency during partitions (violates CAP theorem) 
[-5] Response lacks concrete numbers for latency/throughput impacts
[-3] Response recommends an approach without considering read-heavy workload

Example [+10]: 
"Spanner uses synchronized clocks for strong consistency requiring complex infrastructure, while DynamoDB's eventual consistency allows simpler scaling but needs application-level conflict resolution"

Example [-10]:
"Strong consistency guarantees perfect data consistency even during regional outages"

Rating Criteria Rubric:
Technical Accuracy: 40% (Must correctly apply distributed systems theory)
Comparative Analysis: 30% (Must thoroughly contrast both models' tradeoffs)
Practical Examples: 20% (Must include relevant production case studies)
Clarity: 10% (Must present information in logical, digestible manner)
