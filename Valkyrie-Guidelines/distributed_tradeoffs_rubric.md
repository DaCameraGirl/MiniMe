Rubric Criteria (+/- weights indicate importance):
[+10] Response clearly differentiates how writes propagate in strong vs eventual consistency models
[+8] Explains at least two concrete resolution strategies for write conflicts in eventual consistency systems (e.g. last-write-wins, CRDTs)
[+7] Quantifies the latency impact of strong consistency with round-trips between regions
[+6] Details the debugging tools/techniques needed for diagnosing inconsistencies in eventual consistent systems
[+5] Mentions the operational overhead of maintaining cross-region coordination in strong consistency
[-5] Fails to mention the CAP theorem implications for partition tolerance
[-3] Suggests eventual consistency is always better without qualifying tradeoffs
[-3] Omits discussion of stale reads in eventual consistency models

Example of meeting [+10] criterion: 
"Strong consistency requires synchronous replication before acknowledging writes, while eventual consistency allows asynchronous propagation with potential temporary divergence."

Example of [-5] violation:
"The system will maintain perfect consistency during network partitions" (false for partition-tolerant systems)
