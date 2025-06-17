Strict Prompt Rubric:
[+10] The response must compare write coordination overhead (e.g. quorum writes) in strong consistency versus conflict resolution complexity (e.g. vector clocks) in eventual consistency
[+10] The response must explain latency differences between models including partition scenarios (e.g. strong consistency's higher latency during partitions)
[+10] The response must describe debugging approaches for each model (e.g. read-repair for eventual, quorum health checks for strong)
[+8] The response must provide at least two real-world examples where each model succeeded/failed (e.g. DynamoDB's eventual consistency vs Spanner's strong)
[+5] The response must discuss developer experience tradeoffs (e.g. simpler application logic vs fault tolerance)
[-10] The response claims strong consistency never loses writes during network partitions (violates CAP theorem)
[-5] The response omits discussion of stale read windows in eventual consistency
[-3] The response suggests a one-size-fits-all solution without qualifying workload needs

Example [+10]: 
"Spanner uses synchronized clocks for strong consistency requiring complex infrastructure, while DynamoDB's eventual consistency allows simpler scaling but needs application-level conflict resolution"

Example [-10]:
"Strong consistency guarantees perfect data consistency even during regional outages"

Rating Criteria Rubric:
Technical Accuracy: 40% (Must correctly apply distributed systems theory)
Comparative Analysis: 30% (Must thoroughly contrast both models' tradeoffs)
Practical Examples: 20% (Must include relevant production case studies)
Clarity: 10% (Must present information in logical, digestible manner)
