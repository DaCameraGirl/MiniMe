Rubric Criteria:
[+10] Explains write propagation differences (sync vs async) with concrete examples
[+8] Details two real debugging incidents/tools for each approach (e.g. DynamoDB vs Cassandra issues)
[+7] Compares latency distributions showing impact of coordination rounds
[+5] Mentions tradeoffs in team velocity and error rates from real production systems
[-5] Claims DC failures won't impact availability in strong consistency systems
[-3] Omits discussion of memory/disk overhead differences
[-3] Suggests one size fits all without workload context

Example [+10]: "Shopify moved from strong to eventual consistency for carts, reducing checkout latency by 300ms but requiring new reconciliation workers"

Violation [-5]: "Our strong consistent system will never lose writes during outages"
