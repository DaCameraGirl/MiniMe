Strict Prompt Rubric:
[+10] Response compares implementation complexity between strong and eventual consistency (e.g. coordination overhead vs conflict resolution)
[+8] Analyzes latency impact including normal ops vs partition scenarios
[+7] Details specific debugging approaches for each consistency model
[+5] Provides real-world examples of success/failure cases
[-5] Makes false guarantees about availability during partitions
[-3] Fails to mention operational overhead differences
[-3] Recommends an approach without workload context

Example [+10]: "Strong consistency adds coordination overhead like quorum writes, while eventual consistency requires vector clocks and conflict resolution"

Example [-5]: "Strong consistency guarantees no data loss even during network partitions"

Rating Criteria Rubric:
Accuracy: 40%
- Technical correctness of distributed systems concepts
- Real-world example accuracy

Completeness: 30%
- Covers all requested comparison points
- Includes both pros and cons for each approach

Practicality: 20%
- Actionable recommendations
- Considers operational realities

Clarity: 10%
- Logical organization
- Clear technical explanations
