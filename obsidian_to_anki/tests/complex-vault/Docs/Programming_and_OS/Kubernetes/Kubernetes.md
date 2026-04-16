---
summary: An open source way to manage containerized workloads and services for declarative configuration and automation. Kubernetes (k8s) is running production workloads at scale.
type: note/system
headings:
  - "[[#Concepts of Note]]"
aliases:
  - k8s
date created: Friday, January 9th 2026, 9:44:33 am
date modified: Friday, January 9th 2026, 9:54:31 am
items:
  - "[[k8s API server]]"
  - "[[k8s Controller Manager]]"
  - "[[k8s kubelet]]"
  - "[[k8s kube-proxy]]"
  - "[[k8s Scheduler]]"
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[Docker]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
Service discovery and load balancing
- K8s can expose a container using a DNS name or their own IP adderss. If traffic to a container is high, K8s can load balance and distribute network traffic so deployment is stable.
Storage orchestration
- Lets you automatically mount a storage system of your choice, such as local storage, cloud providers, and more
Automated rollouts and rollbacks
- You can describe the desired state for your deployed contaienrs with K8s
Automatic bin packing
Self-healing
- Restarting containers that fail , replacing containers, killl containers that don't respond to your user-defined health check.
Secret and config management
- Lets you store and manage sensitive info like passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and app config without rebuilding your container images, and without exposing secrets in your stack config.
Batch execution
Horizontal scaling
- Scale your app up and down with a simple command, a UI, or automatically based on CPU usage.
IPv4/IPv6 dual stack

### Weaknesses
- Doesn't deploy source code or build an app. 
- Doesn't provide app services like middleware (message buses) data processing frameworks (Spark) databases, caches, or cluster systems as built-in services. These components *can* run on K8s or can be accessed by apps running on k8s through portable mechanisms.
- Does not dictate logging, monitoring, or alerting solutions.
- Does not provide nor mandate a config language/system
- Does not provide nor mandate a config language/system
- Does not provide nor adopt any comprehensive machine config maintenance management, or self-healing systems
- K8s eliminates the need for orchestration. K8s sets a state of independent, composable control processes that continuously drive the current state towards the provided desired state. Shouldn't matter how you get from A to C. Centralized control is also not required.