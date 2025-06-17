I'm designing a globally distributed key-value store that needs to serve high-throughput requests from multiple regions. The read-heavy workload needs low latency but can tolerate slightly stale data. Compare strong consistency vs eventual consistency approaches - specifically examining the tradeoffs in implementation complexity, performance impact during network partitions, and developer experience.

Focus your analysis on:
1. The architectural changes needed to implement each model
2. How write conflicts get resolved in each case  
3. Expected 99th percentile read latencies in a 3-region deployment
4. Operational considerations for debugging data inconsistencies
