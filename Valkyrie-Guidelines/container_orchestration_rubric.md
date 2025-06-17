Strict Prompt Rubric:
[+10] Response compares operational complexity for logging/monitoring between K8s and Nomad
[+10] Analyzes networking approaches across clouds including latency/security tradeoffs
[+8] Details compliance enforcement mechanisms in both systems
[+8] Provides 2+ real outage examples with root causes
[+5] Discusses team skill requirements for each platform
[-10] Claims either system is "perfect" for all use cases
[-5] Omits discussion of stateful service challenges  
[-3] Recommends without considering compliance needs

Example [+10]:
"Kubernetes requires service meshes for advanced networking which adds complexity, while Nomad's simpler architecture needs less instrumentation but offers fewer built-in controls"

Example [-10]:
"Kubernetes works perfectly for all workloads with no operational overhead"

Rating Criteria Rubric:
Technical Accuracy: 40% (Must correctly describe orchestration systems)
Practical Insights: 30% (Must focus on real operational tradeoffs)
Example Quality: 20% (Must use meaningful production examples)
Clarity: 10% (Must present comparison clearly)
