# Stellons Development Roadmap

## Vision

Stellons is a Human-in-the-Loop Multi-Cloud Container Deployment Platform powered by AI agents.

Users describe infrastructure requirements in natural language.

Example:

> Deploy a 3-node AKS cluster in East US with autoscaling enabled.

Stellons converts this request into:

* Implementation Plan
* Infrastructure as Code
* Validation
* Approval Workflow
* Deployment Pipeline

---

# Phase 1 - Foundation ✅

Status: Completed

## Objectives

Build the initial AI orchestration framework.

## Completed

* GitHub Repository Setup
* Project Structure
* Python Virtual Environment
* NVIDIA API Integration
* DeepSeek Integration
* Planner Agent
* Task Model
* Agent Model
* Workflow Engine
* Agent Prompt Structure

## Deliverables

```text
backend/
├── llm/
├── models/
├── orchestrator/
├── agents/
```

Result:

Planner Agent can generate implementation plans using NVIDIA DeepSeek.

---

# Phase 2 - Agent Framework

Status: In Progress

## Objectives

Connect all agent personalities and responsibilities to the backend engine.

## Tasks

### Planner Agent

* Load system_prompt.md
* Generate implementation roadmap

### Developer Agent

Responsibilities:

* Python
* FastAPI
* APIs
* Unit Tests

### DevOps Agent

Responsibilities:

* OpenTofu
* Terraform
* Kubernetes
* ArgoCD

### Documentation Agent

Responsibilities:

* README
* API Docs
* Release Notes

### Debugging Agent

Responsibilities:

* Log Analysis
* Error Investigation
* Root Cause Analysis

### Architect Agent

Responsibilities:

* Azure
* AWS
* GCP
* Platform Design

## Deliverables

```text
backend/agents/

planner_agent.py
developer_agent.py
devops_agent.py
documentation_agent.py
debugging_agent.py
architect_agent.py
```

---

# Phase 3 - Agent Router

Status: Planned

## Objectives

Automatically select the correct agent.

## Example

User Request:

"Create AKS Terraform"

↓

DevOps Agent

User Request:

"Write FastAPI API"

↓

Developer Agent

User Request:

"Debug deployment failure"

↓

Debugging Agent

## Deliverables

```text
backend/llm/model_router.py
backend/orchestrator/agent_runner.py
```

---

# Phase 4 - Multi-Agent Workflow

Status: Planned

## Objectives

Allow multiple agents to collaborate.

## Workflow

Planner
↓
Architect
↓
Developer
↓
DevOps
↓
Documentation

## Deliverables

```text
backend/orchestrator/workflow.py
```

Enhanced to support agent chaining.

---

# Phase 5 - FastAPI Backend

Status: Planned

## Objectives

Expose Stellons through APIs.

## Endpoints

POST /plan

POST /workflow

POST /generate

POST /deploy

## Deliverables

```text
backend/api/main.py
```

---

# Phase 6 - Human Approval Layer

Status: Planned

## Objectives

Prevent autonomous deployments.

## Workflow

AI Generates Infrastructure

↓

User Reviews

↓

Approve / Reject

↓

Deployment

## Deliverables

Approval Engine

Audit Trail

Request Tracking

---

# Phase 7 - OpenTofu Generator

Status: Planned

## Objectives

Generate Infrastructure as Code.

## Examples

AKS

EKS

GKE

Virtual Networks

Storage

Databases

## Deliverables

```text
infrastructure/opentofu/
```

---

# Phase 8 - GitHub Integration

Status: Planned

## Objectives

Allow agents to create commits and pull requests.

## Features

* Create Branch
* Commit Files
* Create Pull Request
* Request Approval

---

# Phase 9 - Deployment Engine

Status: Planned

## Objectives

Deploy approved infrastructure.

## Workflow

Prompt
↓
IaC
↓
Git
↓
ArgoCD
↓
AKS / EKS / GKE

---

# Phase 10 - Stellons MVP

Status: Future

## Final Workflow

User Prompt
↓
Planner Agent
↓
Architect Agent
↓
Policy Agent
↓
Developer Agent
↓
DevOps Agent
↓
Documentation Agent
↓
Validation Agent
↓
Git Repository
↓
ArgoCD
↓
AKS / EKS / GKE

---

# Current Sprint

## Active Goal

Complete Agent Framework

### Sprint Tasks

* Connect system_prompt.md files
* Complete Developer Agent
* Complete DevOps Agent
* Complete Documentation Agent
* Complete Debugging Agent
* Complete Architect Agent
* Build Agent Router
* Build Multi-Agent Workflow

Success Criteria:

All agents can receive a goal, load instructions, invoke NVIDIA models, and return a response.
