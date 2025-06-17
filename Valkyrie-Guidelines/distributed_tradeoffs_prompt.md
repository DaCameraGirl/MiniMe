We're implementing a globally distributed key-value store with:
- Read-heavy workload (90% reads)
- Multi-region deployment (3 regions) 
- P99 latency target <100ms
- Tolerance for stale reads (up to 1 second)

Compare strong vs eventual consistency regarding:
1. Implementation complexity (e.g. coordination overhead vs conflict resolution)
2. Latency distribution during normal ops and network partitions
3. Debugging tools/techniques for each model
4. 2+ real production examples showing success/failure

Include specific metrics where possible (e.g. latency percentiles, throughput impact).
