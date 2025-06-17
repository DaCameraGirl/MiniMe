Strict Prompt Rubric:
[+10] The response must compare operational complexity for logging/monitoring between Kubernetes and Nomad
[+10] The response must analyze multi-cloud networking approaches including latency/security tradeoffs
[+8] The response must detail compliance enforcement mechanisms in both systems
[+8] The response must provide 2+ real outage examples with root causes
[+5] The response must discuss team skill requirements for each platform
[-10] The response claims either system is "perfect" for all use cases
[-5] The response omits discussion of stateful service challenges
[-3] The response recommends an approach without considering compliance needs

Example [+10]:
"Kubernetes requires service meshes for advanced networking which adds complexity, while Nomad's simpler architecture needs less instrumentation but offers fewer built-in controls"

Example [-10]:
"Kubernetes works perfectly for all workloads with no operational overhead"

Rating Criteria Rubric:
Technical Accuracy: 40% (Must correctly describe orchestration systems)
Practical Insights: 30% (Must focus on real operational tradeoffs)
Example Quality: 20% (Must use meaningful production examples)
Clarity: 10% (Must present comparison clearly)
