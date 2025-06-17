We're scaling our distributed key-value store globally and need to pick between strong and eventual consistency. Our workload is read-heavy across regions, latency-sensitive but can handle slightly stale reads temporarily. Help me weigh the tradeoffs focusing on:

1. Implementation complexity differences
2. Expected latency impact during normal ops and partitions
3. What debugging looks like when inconsistencies appear
4. Real-world examples where each model succeeded/failed 
