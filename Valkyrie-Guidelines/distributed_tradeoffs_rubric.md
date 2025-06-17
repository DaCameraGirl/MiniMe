Strict Prompt Rubric:
[+10] The response must compare coordination mechanisms (e.g. quorum writes, consensus protocols) in strong consistency vs conflict resolution (e.g. vector clocks, CRDTs) in eventual consistency
[+10] The response must provide specific latency percentiles (P50/P99) comparisons for both models under normal and partition conditions
[+8] The response must detail monitoring/diagnostics tools needed for each model (e.g. consistency metrics for eventual, quorum health for strong)
[+8] The response must cite 2+ production examples with concrete metrics (e.g. "DynamoDB achieves 15ms P99 reads with eventual consistency")
[+5] The response must analyze throughput impact comparing both models
[+5] The response must address the 1s staleness tolerance requirement specified in the prompt
[-10] The response claims perfect consistency during partitions (violates CAP theorem)
[-5] The response lacks concrete numbers for latency/throughput impacts
[-3] The response recommends an approach without considering the read-heavy workload

Example [+10]: 
"Spanner uses synchronized clocks for strong consistency requiring complex infrastructure, while DynamoDB's eventual consistency allows simpler scaling but needs application-level conflict resolution"

Example [-10]:
"Strong consistency guarantees perfect data consistency even during regional outages"

Rating Criteria Rubric:
Technical Accuracy: 40% (Must correctly apply distributed systems theory)
Comparative Analysis: 30% (Must thoroughly contrast both models' tradeoffs)
Practical Examples: 20% (Must include relevant production case studies)
Clarity: 10% (Must present information in logical, digestible manner)
