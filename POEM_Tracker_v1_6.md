# POEM Project Tracker

**Version:** 1.6  
**Last Updated:** February 28, 2026  
**PRD Reference:** POEM_PRD_v1.3.md  
**GitHub Repo:** https://github.com/sreynolds100/poem-core

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.6 | 2026-02-28 | PRD updated to v1.3; renamed Operations Agent → DevOps Agent; added Support Ops Agent (1.10), Service Engineering Agent (1.11), Approval Gate Engine (1.12), Work Item Hierarchy (1.13), Cross-Agent Question Protocol (1.14); added design discussions D1-D5; CLA bot complete (0.1.5); updated weekly goals; updated repo structure |
| 1.5 | 2026-02-28 | Added Phase 1.9 (EventBus + ActivityStore + Reporting Dashboard + Time-Savings Model), updated PRD reference to v1.2, added decision log entries for telemetry architecture |
| 1.4 | 2026-02-28 | Phase 0.1 complete (all license/repo files committed), Phase 0.2 complete (abstractions, config, prompts), Dockerfile + docker-compose added, email set to poem.pdm@gmail.com |
| 1.3 | 2026-02-28 | GitHub repo created (sreynolds100/poem-core), added Session Handoff section, updated task statuses |
| 1.2 | 2026-02-27 | Added dual licensing structure (AGPL + Commercial), CLA, licensing tasks |
| 1.1 | 2026-02-27 | Added portability tasks (0.x), open source structure, IP protection, self-hosting |
| 1.0 | 2026-02-27 | Initial tracker based on PRD v1.0 |

---

## Session Handoff (Last Updated: 2026-02-28)

This section captures the current state for continuity across sessions.

### Current Status Summary

| Area | Status | Notes |
|------|--------|-------|
| PRD v1.3 | 🟢 Complete | All 8 sections + 3 appendices; v1.3 adds agent roles, approval gate framework, work item hierarchy, support ops agents, sequential flow |
| GitHub Repo | 🟢 Created | sreynolds100/poem-core — fully structured with all Phase 0 files |
| Phase 0.1 (Open Source Setup) | 🟢 Complete | All items including CLA bot (0.1.5) |
| Phase 0.2 (Portability) | 🟢 Complete | Config schema, provider abstractions, prompt externalization, .env.example |
| Phase 0.3 (Containers) | 🟡 In Progress | Dockerfile + docker-compose created; local/production deploy docs still needed |
| Phase 0.4 (Instance Separation) | ⬜ Not Started | poem-instance-template repo, company guides |
| Telemetry Architecture | 🟢 Designed | EventBus + ActivityStore as separate component |
| User Flow Diagrams | 🟢 Complete | 9 diagrams in Mermaid format aligned with PRD v1.3 |
| Evaluation Spreadsheet | ⬜ Not Started | Required for PRD Section 6 |

### Immediate Next Steps (Priority Order)

1. **Push updated files to repo** (PRD v1.3, Tracker v1.6, User Flow Diagrams v2)
2. **Create evaluation spreadsheet** (link to add to PRD Section 6)
3. **Resolve open design discussions** (D1-D5 in Appendix C of PRD) — needed before Phase 1 implementation
4. **Begin Phase 1 infrastructure** — dev environment setup (1.1.1), start implementing agents

### Environment Info

- **Dev Environment:** WSL Ubuntu at `/home/sam/dev`
- **Windows Path:** `\\wsl.localhost\Ubuntu\home\sam\dev`
- **Platform:** Windows 11 (64-bit)

### Files Cleaned from Project Knowledge

The following reference files were removed to reduce context size (content already incorporated into PRD):
- Cohorts_Past_Project_Ideas.xlsx
- ContractIQ.md
- Trading_Helper_agent.md
- POEM_Spreadsheet_Submission.xlsx

---

## Status Legend

| Status | Meaning |
|--------|---------|
| ⬜ Not Started | Work has not begun |
| 🟡 In Progress | Actively being worked on |
| 🟢 Complete | Done and validated |
| 🔴 Blocked | Waiting on dependency or decision |
| ⏸️ Deferred | Moved to post-MVP |

---

## Licensing Strategy: AGPL + Commercial Dual License

### Overview

POEM uses a dual licensing model:

1. **AGPL v3 (Default)** — Free for individuals, small teams, and anyone willing to open source their customizations
2. **Commercial License** — For enterprises who want proprietary customizations, SaaS deployment, or support

### Why This Works

- AGPL is OSI-approved "real" open source
- Enterprises typically require commercial license (legal teams avoid copyleft)
- You retain full rights as sole author to offer commercial terms
- Community can still use, contribute, and benefit

### License Decision Tree

```
Is the user...
│
├─► Individual/small team, personal use
│   └─► AGPL is fine, free to use
│
├─► Company using internally, willing to AGPL their config
│   └─► AGPL is fine, free to use
│
├─► Company wanting proprietary customizations
│   └─► Needs Commercial License 💰
│
├─► Anyone offering POEM as a hosted service (SaaS)
│   └─► Needs Commercial License 💰
│
└─► Enterprise wanting support/SLAs
    └─► Needs Commercial License 💰
```

### Revenue Scenarios (Post-Launch)

| Tier | Price | Target | Includes |
|------|-------|--------|----------|
| Indie | Free (AGPL) | Individuals, small startups | Full functionality, community support |
| Team | $500/year | Startups 5-20 people | Commercial license, email support |
| Business | $2,000/year | Companies 20-100 | Commercial license, priority support |
| Enterprise | Custom | 100+ or SaaS providers | Custom terms, SLA, dedicated support |

---

## Design Discussions (Open)

These require resolution before Phase 1 implementation. Tracked in PRD Appendix C.

| ID | Topic | Key Questions | Status |
|----|-------|--------------|--------|
| D1 | Approval gate configuration schema | What does config.yaml look like for roles, policies, timeouts? Free-text vs predefined roles? | ⬜ Open |
| D2 | Work item hierarchy customization | Auto-detect depth from PRD complexity? Cross-epic dependency handling? | ⬜ Open |
| D3 | Support ops integration architecture | Which support desk first? High-volume batching strategy? | ⬜ Open |
| D4 | Service Engineering Agent scope boundaries | Investigate-not-fix enforcement; handoff protocol to Engineering | ⬜ Open |
| D5 | Cross-agent question protocol | UX for questions; flywheel pause behavior; question batching | ⬜ Open |

---

## Phase 0: Foundation & Portability (Before Week 1)

*Critical: Complete these on personal time, personal equipment, before using at any company.*

### 0.1 Open Source Core Setup

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 0.1.1 | Create poem-core repo on personal GitHub | 🟢 | None | ✅ Created: sreynolds100/poem-core |
| 0.1.2 | Add AGPL-3.0 LICENSE file | 🟢 | 0.1.1 | ✅ Full AGPL-3.0 text + custom header with commercial notice |
| 0.1.3 | Create COMMERCIAL_LICENSE.md | 🟢 | 0.1.1 | ✅ Pricing tiers, FAQ, contact: poem.pdm@gmail.com |
| 0.1.4 | Create CLA.md (Contributor License Agreement) | 🟢 | 0.1.1 | ✅ Covers dual licensing grant |
| 0.1.5 | Set up CLA bot (CLA Assistant) | 🟢 | 0.1.4 | ✅ CLA Assistant installed, linked to CLA gist, configured for poem-core |
| 0.1.6 | Add copyright headers template | 🟢 | 0.1.1 | ✅ All .py files have AGPL headers |
| 0.1.7 | Write initial README with project vision | 🟢 | 0.1.1 | ✅ Badges, architecture, quick start, licensing section |
| 0.1.8 | Set up repo structure (see Architecture below) | 🟢 | 0.1.1 | ✅ Full directory tree with placeholder files |
| 0.1.9 | Add CONTRIBUTING.md (references CLA) | 🟢 | 0.1.4 | ✅ Coding standards, commit conventions, CLA requirement |
| 0.1.10 | Add CODE_OF_CONDUCT.md | 🟢 | 0.1.1 | ✅ Contributor Covenant v2.1 |
| 0.1.11 | Initial commit with structure + licenses | 🟢 | 0.1.8 | ✅ 47 files committed to repo |

### 0.2 Portability Architecture

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 0.2.1 | Design config.yaml schema | 🟢 | None | ✅ config.example.yaml with all sections: LLM, vector DB, agents, orchestrator, integrations, UI, server, logging |
| 0.2.2 | Create LLM provider abstraction interface | 🟢 | None | ✅ BaseLLMProvider in providers/llm/base.py (generate, generate_structured) |
| 0.2.3 | Create vector DB abstraction interface | 🟢 | None | ✅ BaseVectorDB in providers/vectordb/base.py (store, query, delete) |
| 0.2.4 | Create integration abstraction interface | 🟢 | None | ✅ BaseIntegration in integrations/base_integration.py (connect, push, pull, health_check) |
| 0.2.5 | Externalize all prompts to /prompts directory | 🟢 | None | ✅ 6 prompt templates across 5 agent directories |
| 0.2.6 | Environment variable mapping for secrets | 🟢 | 0.2.1 | ✅ .env.example with all API keys, config.yaml uses ${VAR} syntax |
| 0.2.7 | Create config.example.yaml (no secrets) | 🟢 | 0.2.1 | ✅ Fully documented, safe to commit |

### 0.3 Self-Hosting & Containerization

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 0.3.1 | Create Dockerfile for core engine | 🟢 | 0.1.8 | ✅ Python 3.11-slim, health check, pgvector deps |
| 0.3.2 | Create docker-compose.yaml (full stack) | 🟢 | 0.3.1 | ✅ poem + pgvector/pgvector:pg16, volumes, health checks |
| 0.3.3 | Document local development setup | 🟡 | 0.3.2 | README has Quick Start; detailed dev docs still needed |
| 0.3.4 | Document production deployment options | ⬜ | 0.3.2 | VPS, Railway, Render, cloud k8s |
| 0.3.5 | Test deployment on $5 VPS (DigitalOcean/Hetzner) | ⬜ | 0.3.2 | Prove self-hosting works |
| 0.3.6 | Add health check endpoints | ⬜ | 0.3.1 | For container orchestration |

### 0.4 Instance Separation Pattern

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 0.4.1 | Create poem-instance-template repo | ⬜ | 0.1.8 | Reference implementation for customization |
| 0.4.2 | Document core vs instance separation | ⬜ | 0.4.1 | What goes where |
| 0.4.3 | Create instance bootstrap script | ⬜ | 0.4.1 | Quick start for new deployments |
| 0.4.4 | Document "using at your company" guide | ⬜ | 0.4.2 | How to pitch IT/legal, deploy, customize |
| 0.4.5 | Document licensing options for companies | ⬜ | 0.1.3 | When AGPL is fine vs need commercial |

---

## Licensing Templates

### LICENSE (AGPL-3.0 with Commercial Notice)

```
POEM - Product Operations Engineering Marketing Lifecycle Agent
Copyright (C) 2026 Samantha Reynolds

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

---

COMMERCIAL LICENSING

For commercial licensing options (proprietary use, SaaS deployment, 
enterprise support), see COMMERCIAL_LICENSE.md or contact:
poem.pdm@gmail.com
```

### COMMERCIAL_LICENSE.md (Template)

```markdown
# Commercial License for POEM

## When Do You Need a Commercial License?

POEM is available under AGPL-3.0 for free. However, you need a 
commercial license if:

1. **Proprietary Customizations** — You want to modify POEM without 
   releasing your changes under AGPL
2. **SaaS Deployment** — You want to offer POEM as a hosted service
3. **Enterprise Requirements** — You need SLAs, dedicated support, 
   or your legal team requires non-copyleft licensing

## When Is AGPL Sufficient?

You can use POEM under AGPL for free if:

- You're an individual or small team using it internally
- You're willing to release any modifications under AGPL
- You're not offering POEM as a service to others

## Pricing

| Tier | Annual Price | For |
|------|--------------|-----|
| Team | $500/year | Startups (5-20 employees) |
| Business | $2,000/year | Companies (20-100 employees) |
| Enterprise | Contact us | 100+ employees or SaaS providers |

## Contact

For commercial licensing inquiries: poem.pdm@gmail.com

## FAQ

**Q: Can I try POEM before buying a commercial license?**
A: Yes! Use it under AGPL as long as you need. Only purchase when 
   you need proprietary rights or support.

**Q: What if I contribute code back?**
A: Contributors sign a CLA granting us rights to include contributions 
   in both AGPL and commercial versions. You retain rights to your 
   contributions.

**Q: Can my company use POEM internally under AGPL?**
A: Yes, if you're not distributing it or offering it as a service, 
   and you're comfortable with AGPL terms for any modifications.
```

### CLA.md (Contributor License Agreement - Template)

```markdown
# Contributor License Agreement

Thank you for your interest in contributing to POEM!

## Why a CLA?

POEM uses dual licensing (AGPL + Commercial). For us to include your 
contributions in both versions, we need your permission via this CLA.

## What You're Agreeing To

By submitting a pull request, you agree that:

1. **You own the contribution** — You have the right to submit it
2. **License grant** — You grant us (Samantha Reynolds) a perpetual, 
   worldwide, non-exclusive, royalty-free license to use, modify, and 
   distribute your contribution under any license we choose
3. **You keep your rights** — You retain all rights to your contribution 
   and can use it however you want
4. **It's your original work** — Or you have permission to submit it

## How to Sign

We use CLA Assistant. When you open your first PR, you'll be prompted 
to sign electronically.

## Questions?

Contact: poem.pdm@gmail.com
```

### Source File Header Template

```python
# POEM - Product Operations Engineering Marketing Lifecycle Agent
# Copyright (C) 2026 Samantha Reynolds
#
# This file is part of POEM.
#
# POEM is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# POEM is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for
# more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with POEM. If not, see <https://www.gnu.org/licenses/>.
#
# Commercial licensing available. See COMMERCIAL_LICENSE.md
```

---

## Repository Structure

```
poem-core/                      # AGPL Licensed - YOU OWN
├── LICENSE                     # AGPL-3.0 with commercial notice
├── COMMERCIAL_LICENSE.md       # How to get commercial license
├── CLA.md                      # Contributor License Agreement
├── README.md
├── CONTRIBUTING.md             # References CLA requirement
├── CODE_OF_CONDUCT.md
├── pyproject.toml              # or package.json
├── Dockerfile
├── docker-compose.yaml
├── config.example.yaml         # Template, no secrets
│
├── poem/
│   ├── __init__.py
│   ├── orchestrator/
│   │   ├── __init__.py
│   │   ├── state_machine.py
│   │   └── context_graph.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py       # Abstract base class
│   │   ├── product_agent.py
│   │   ├── devops_agent.py     # renamed from operations_agent.py
│   │   ├── engineering_agent.py
│   │   ├── marketing_agent.py
│   │   ├── feedback_agent.py
│   │   ├── support_ops_agent.py      # NEW in v1.6
│   │   └── service_engineering_agent.py  # NEW in v1.6
│   │
│   ├── gates/                  # NEW in v1.6 — Approval Gate Engine
│   │   ├── __init__.py
│   │   ├── gate_engine.py      # Core gate logic, policy evaluation
│   │   ├── gate_config.py      # Configuration loading from config.yaml
│   │   └── backlog.py          # Rejected idea storage and retrieval
│   │
│   ├── work_items/             # NEW in v1.6 — Work Item Hierarchy
│   │   ├── __init__.py
│   │   ├── hierarchy.py        # Idea/Epic/Story/Task models
│   │   └── dependency_graph.py # Cross-item dependency tracking
│   │
│   ├── providers/              # Abstraction layer
│   │   ├── __init__.py
│   │   ├── llm/
│   │   │   ├── base.py         # Abstract LLM interface
│   │   │   ├── anthropic.py    # Claude implementation
│   │   │   ├── openai.py       # GPT implementation
│   │   │   └── azure.py        # Azure OpenAI
│   │   │
│   │   └── vectordb/
│   │       ├── base.py         # Abstract vector DB interface
│   │       ├── pinecone.py
│   │       ├── qdrant.py
│   │       └── pgvector.py
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── base_integration.py # Abstract integration interface
│   │   └── examples/
│   │       ├── jira.py         # Reference implementation
│   │       ├── linear.py
│   │       └── slack.py
│   │
│   ├── telemetry/              # EventBus + ActivityStore
│   │   ├── __init__.py
│   │   ├── event_bus.py        # Lightweight event emitter
│   │   ├── event_schema.py     # Event model definitions
│   │   ├── activity_store.py   # Postgres event log
│   │   ├── time_savings.py     # Defaults + calibration logic
│   │   └── reporting.py        # Aggregation queries for dashboard
│   │
│   └── ui/
│       └── (React app)
│
├── prompts/
│   └── defaults/               # Generic starter prompts
│       ├── product_agent/
│       │   ├── prd_generation.txt
│       │   └── user_story.txt
│       ├── engineering_agent/
│       ├── devops_agent/       # renamed from operations_agent/
│       ├── marketing_agent/
│       ├── feedback_agent/
│       ├── support_ops_agent/        # NEW in v1.6
│       │   └── classification.txt
│       └── service_engineering_agent/ # NEW in v1.6
│           └── investigation.txt
│
└── tests/

poem-instance-template/         # Template for company/personal instances
├── README.md                   # How to customize
├── config.yaml                 # Actual config (gitignored secrets)
├── config.example.yaml         # Safe to commit
├── .env.example
├── docker-compose.override.yaml
│
├── prompts/                    # Override/extend default prompts
│   └── (company-specific)      # These are THEIR IP if proprietary
│
├── integrations/               # Company-specific integrations
│   └── (their custom connectors)
│
└── branding/
    └── (logos, colors, etc)
```

---

## Phase 1: MVP (Week 1-3)

### 1.1 Core Infrastructure

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.1.1 | Set up development environment | ⬜ | Phase 0 | Poetry/npm, linting, formatting |
| 1.1.2 | Implement LLM provider abstraction | ⬜ | 0.2.2 | Start with Claude, interface ready for others |
| 1.1.3 | Implement vector DB abstraction | ⬜ | 0.2.3 | Start with pgvector (free, portable) |
| 1.1.4 | Configure LangChain + LangGraph | ⬜ | 1.1.2 | Multi-agent orchestration |
| 1.1.5 | Implement config loading from yaml + env | ⬜ | 0.2.1, 0.2.6 | Pydantic settings or similar |
| 1.1.6 | Basic React + Tailwind UI scaffold | ⬜ | 0.1.8 | |
| 1.1.7 | Set up prompt loading from files | ⬜ | 0.2.5 | Hot-reload in dev mode |
| 1.1.8 | Add license headers to all source files | ⬜ | 0.1.6 | Automate with pre-commit hook |

### 1.2 Orchestrator Agent

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.2.1 | Design orchestrator state machine | ⬜ | 1.1.4 | Define flywheel states and transitions; include named gates and backlog state |
| 1.2.2 | Implement agent routing logic | ⬜ | 1.2.1 | Route tasks to appropriate stage agents |
| 1.2.3 | Build context graph schema | ⬜ | 1.1.3 | Define how decisions/context are stored |
| 1.2.4 | Implement context retrieval for agents | ⬜ | 1.2.3 | Agents can query relevant context |
| 1.2.5 | Build human approval gate system | ⬜ | 1.2.1 | Pause flywheel for human review; integrates with Gate Engine (1.12) |
| 1.2.6 | Implement flywheel state persistence | ⬜ | 1.2.1, 1.1.3 | Resume interrupted cycles |
| 1.2.7 | Implement backlog management (rejected ideas storage + retrieval) | ⬜ | 1.2.1, 1.12.3 | Prioritized backlog with rejection rationale |
| 1.2.8 | Implement sequential Engineering → DevOps routing | ⬜ | 1.2.2 | Engineering completes before DevOps starts; replaces parallel routing |

### 1.3 Product Agent (PRD Generation)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.3.1 | Design PRD output schema | ⬜ | None | JSON structure for generated PRDs |
| 1.3.2 | Create product brief ingestion parser | ⬜ | 1.1.2 | Extract structure from natural language |
| 1.3.3 | Build PRD generation prompt templates | ⬜ | 1.3.1, 1.1.7 | Few-shot + CoT, stored in /prompts |
| 1.3.4 | Implement user story generation | ⬜ | 1.3.3 | Part of PRD output |
| 1.3.5 | Implement acceptance criteria generation | ⬜ | 1.3.3 | Part of PRD output |
| 1.3.6 | Add reasoning trace output | ⬜ | 1.3.3 | Explainability for decisions |
| 1.3.7 | Build PRD review UI | ⬜ | 1.1.6, 1.3.3 | Human approval interface |
| 1.3.8 | Connect to context graph (write) | ⬜ | 1.2.3, 1.3.3 | Store PRD decisions in context |

### 1.4 DevOps Agent (formerly Operations Agent)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.4.1 | Design DevOps spec output schema | ⬜ | None | Infrastructure/deployment spec structure |
| 1.4.2 | Build DevOps spec generation prompt templates | ⬜ | 1.4.1, 1.1.7 | Stored in /prompts/devops_agent/ |
| 1.4.3 | Implement deployment config generation | ⬜ | 1.4.2 | Basic deployment specs |
| 1.4.4 | Implement infrastructure requirements | ⬜ | 1.4.2 | Resource estimates, dependencies |
| 1.4.5 | Add reasoning trace output | ⬜ | 1.4.2 | Why these infrastructure choices |
| 1.4.6 | Build DevOps spec review UI | ⬜ | 1.1.6, 1.4.2 | Human approval interface |
| 1.4.7 | Connect to context graph (read PRD + engineering plan, write DevOps specs) | ⬜ | 1.2.4, 1.4.2 | Context preservation; reads Engineering output |

### 1.5 Engineering Agent (Work Item Generation)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.5.1 | Design work item output schema | ⬜ | 1.13.1 | References hierarchy from Work Item Hierarchy component |
| 1.5.2 | Build work item generation prompt templates | ⬜ | 1.5.1, 1.1.7 | Stored in /prompts |
| 1.5.3 | Implement complexity estimation | ⬜ | 1.5.2 | Story points / t-shirt sizing |
| 1.5.4 | Implement dependency identification | ⬜ | 1.5.2 | Which items block others |
| 1.5.5 | Add reasoning trace output | ⬜ | 1.5.2 | Why this breakdown |
| 1.5.6 | Build work item review UI | ⬜ | 1.1.6, 1.5.2 | Human approval interface with hierarchy view |
| 1.5.7 | Connect to context graph (read PRD, write work items) | ⬜ | 1.2.4, 1.5.2 | Context preservation |

### 1.6 Marketing Agent (Launch Brief Generation)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.6.1 | Design marketing brief output schema | ⬜ | None | Positioning, messaging, audience |
| 1.6.2 | Build marketing brief prompt templates | ⬜ | 1.6.1, 1.1.7 | Stored in /prompts |
| 1.6.3 | Implement positioning statement generation | ⬜ | 1.6.2 | Core value prop articulation |
| 1.6.4 | Implement messaging framework | ⬜ | 1.6.2 | Key messages, proof points |
| 1.6.5 | Implement target audience definition | ⬜ | 1.6.2 | From PRD personas |
| 1.6.6 | Add reasoning trace output | ⬜ | 1.6.2 | Why this positioning |
| 1.6.7 | Build marketing brief review UI | ⬜ | 1.1.6, 1.6.2 | Human approval interface |
| 1.6.8 | Connect to context graph (read all, write marketing) | ⬜ | 1.2.4, 1.6.2 | Full context access |

### 1.7 Feedback Agent

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.7.1 | Design feedback input schema | ⬜ | None | How feedback data is structured; includes support signal inputs |
| 1.7.2 | Design iteration proposal output schema | ⬜ | None | What Feedback Agent produces |
| 1.7.3 | Build feedback synthesis prompt templates | ⬜ | 1.7.1, 1.7.2, 1.1.7 | Stored in /prompts |
| 1.7.4 | Implement signal detection logic | ⬜ | 1.7.3 | Distinguish signal from noise across all channels |
| 1.7.5 | Implement context linking | ⬜ | 1.2.4, 1.7.3 | Connect feedback to original PRD |
| 1.7.6 | Build iteration proposal generation | ⬜ | 1.7.3 | Suggest next product iteration |
| 1.7.7 | Add reasoning trace output | ⬜ | 1.7.3 | Why this interpretation |
| 1.7.8 | Build feedback review UI | ⬜ | 1.1.6, 1.7.3 | Human approval for iteration |
| 1.7.9 | Connect to Product Agent (close loop) | ⬜ | 1.7.6, 1.3.2 | Feed iteration back to Product Agent |

### 1.8 Single Integration (Reference Implementation)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.8.1 | Implement base integration interface | ⬜ | 0.2.4 | Abstract class for all integrations |
| 1.8.2 | Build one project management integration | ⬜ | 1.8.1, 1.5.6 | Linear recommended (simpler API than Jira) |
| 1.8.3 | Build one feedback source integration | ⬜ | 1.8.1, 1.7.1 | Manual input first, then simple analytics |
| 1.8.4 | Build notification integration | ⬜ | 1.8.1, 1.2.5 | Slack or email for approval gates |

### 1.9 Telemetry, Reporting & Time-Savings (EventBus + ActivityStore)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.9.1 | Design event schema (event_type, agent, project_id, user_id, metadata) | ⬜ | None | Structured event model — see PRD Section 3; includes support_signal event type |
| 1.9.2 | Create ActivityStore postgres schema (events table, time_estimates table) | ⬜ | 1.1.3 | Append-only log alongside pgvector; same postgres instance |
| 1.9.3 | Implement EventBus class (emit method, write to ActivityStore) | ⬜ | 1.9.2 | Lightweight — ~100 lines; all components get a reference |
| 1.9.4 | Wire EventBus into Orchestrator (state_transition events) | ⬜ | 1.9.3, 1.2.1 | Timestamps at each flywheel stage change; includes idea_backlogged event |
| 1.9.5 | Wire EventBus into all agents (agent_action events) | ⬜ | 1.9.3, 1.3-1.7, 1.10-1.11 | Artifact generated, context retrieved, reasoning trace created, question_raised_to_product |
| 1.9.6 | Wire EventBus into approval gates (gate_decision events) | ⬜ | 1.9.3, 1.2.5, 1.12.2 | Approved/revised/rejected with timestamps; rejection-to-backlog events |
| 1.9.7 | Implement time-savings defaults table | ⬜ | 1.9.2 | Industry-standard estimates per action type |
| 1.9.8 | Implement time-estimate calibration prompt at approval gates | ⬜ | 1.9.7, 1.2.5 | "How long would this have taken manually?" — stores user answer |
| 1.9.9 | Implement time-savings aggregation queries | ⬜ | 1.9.7, 1.9.8 | Weekly/monthly rollup per user, per project |
| 1.9.10 | Build personal reporting dashboard (time saved, activity timeline) | ⬜ | 1.9.9, 1.1.6 | Read-only queries against ActivityStore |
| 1.9.11 | Build project reporting view (cycle times, approval rates, stage durations) | ⬜ | 1.9.9, 1.1.6 | Per-project metrics derived from events |
| 1.9.12 | Emit system_health events (latency, errors, API costs) | ⬜ | 1.9.3 | Foundation for future monitoring service |

### 1.10 Support Operations Agent

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.10.1 | Design support signal input schema | ⬜ | None | How support tickets/bug reports are structured for ingestion |
| 1.10.2 | Design classification output schema (bug/feature request/UX confusion) | ⬜ | None | Three-category output with confidence scores and reasoning |
| 1.10.3 | Build classification prompt templates | ⬜ | 1.10.2, 1.1.7 | Few-shot examples of each category + edge cases; stored in /prompts |
| 1.10.4 | Implement classification logic | ⬜ | 1.10.3 | Core classification with routing rules per category |
| 1.10.5 | Implement human override mechanism | ⬜ | 1.10.4 | Allow reclassification; track override rate for accuracy metric |
| 1.10.6 | Implement pattern detection (recurring signals) | ⬜ | 1.10.4 | "20 users reported same UX confusion this week" aggregation |
| 1.10.7 | Build support signal review UI | ⬜ | 1.1.6, 1.10.4 | Classification results with override capability |
| 1.10.8 | Connect to Feedback Agent (feature requests + UX confusion) | ⬜ | 1.10.4, 1.7.1 | Route classified signals to Feedback Agent for synthesis |
| 1.10.9 | Connect to Engineering Agent (bugs) | ⬜ | 1.10.4, 1.5.1 | Route confirmed bugs with Service Engineering context |
| 1.10.10 | Wire EventBus (support_signal events) | ⬜ | 1.9.3, 1.10.4 | Classification events, override events for accuracy tracking |

### 1.11 Service Engineering Agent

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.11.1 | Design investigation output schema | ⬜ | None | Root cause analysis, reproduction steps, severity assessment |
| 1.11.2 | Build investigation prompt templates | ⬜ | 1.11.1, 1.1.7 | Stored in /prompts; emphasis on investigate-not-fix boundary |
| 1.11.3 | Implement technical investigation logic | ⬜ | 1.11.2 | Analyze bug reports, provide engineering context |
| 1.11.4 | Implement handoff protocol to Engineering Agent | ⬜ | 1.11.3, 1.5.1 | Enriched bug reports with reproduction steps and root cause |
| 1.11.5 | Add reasoning trace output | ⬜ | 1.11.2 | Why this root cause assessment |
| 1.11.6 | Wire EventBus (agent_action events) | ⬜ | 1.9.3, 1.11.3 | Investigation events |

### 1.12 Approval Gate Engine

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.12.1 | Design gate configuration schema for config.yaml | ⬜ | None | Roles, policies, timeouts per gate — see Discussion D1 |
| 1.12.2 | Implement single-decider approval policy (MVP default) | ⬜ | 1.2.5 | Solo founder configuration; simplest case |
| 1.12.3 | Implement rejection-to-backlog flow | ⬜ | 1.12.2 | Backlog storage, rejection rationale, submitter notification |
| 1.12.4 | Build backlog management UI | ⬜ | 1.12.3, 1.1.6 | View, reprioritize, resubmit backlogged ideas |
| 1.12.5 | Implement named gate stages (Intake/Technical/GTM/Iteration) | ⬜ | 1.12.2 | Gate naming in UI and event emissions |
| 1.12.6 | Implement multi-approver policies (majority, unanimous) | ⬜ | 1.12.2 | Post-MVP but design now — see Discussion D1 |
| 1.12.7 | Implement no-vote timeout and auto-escalation | ⬜ | 1.12.6 | Post-MVP |
| 1.12.8 | Implement per-project gate configuration | ⬜ | 1.12.6 | Post-MVP |
| 1.12.9 | Implement per-feature/function gate configuration | ⬜ | 1.12.8 | Post-MVP; for larger teams |

### 1.13 Work Item Hierarchy

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.13.1 | Design work item hierarchy schema (idea/epic/story/task) | ⬜ | None | Configurable levels — see Discussion D2 |
| 1.13.2 | Add hierarchy depth configuration to config.yaml | ⬜ | 1.13.1 | engineering_agent.work_item_hierarchy key |
| 1.13.3 | Update Engineering Agent to generate hierarchical output | ⬜ | 1.13.1, 1.5.2 | Replaces flat ticket generation |
| 1.13.4 | Implement cross-hierarchy dependency mapping | ⬜ | 1.13.3 | Dependencies between stories, between epics |
| 1.13.5 | Build hierarchy view in UI | ⬜ | 1.13.3, 1.1.6 | Tree view with expand/collapse |
| 1.13.6 | Implement minimal hierarchy mode (idea → tasks) | ⬜ | 1.13.2 | Default for solo founders |

### 1.14 Cross-Agent Question Protocol

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 1.14.1 | Design question-routing protocol | ⬜ | None | See Discussion D5; how agents flag ambiguity back to Product |
| 1.14.2 | Implement Engineering → Product question flow | ⬜ | 1.14.1, 1.2.2 | Pause flywheel at that stage, present question to user |
| 1.14.3 | Implement DevOps → Product/Engineering question flow | ⬜ | 1.14.1, 1.2.2 | DevOps can question either upstream agent |
| 1.14.4 | Build question/answer UI | ⬜ | 1.14.1, 1.1.6 | In-context Q&A within the flywheel stage |
| 1.14.5 | Wire EventBus (question_raised events) | ⬜ | 1.9.3, 1.14.1 | Track cross-agent communication frequency |

---

## Phase 2: MVP+1 (Week 4-5)

### 2.1 Deeper Artifact Generation

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.1.1 | Enhanced PRD templates (multiple formats) | ⬜ | Phase 1 | |
| 2.1.2 | More granular work item breakdown options | ⬜ | Phase 1 | Full hierarchy with themes and sub-tasks |
| 2.1.3 | Detailed DevOps runbook generation | ⬜ | Phase 1 | |
| 2.1.4 | Expanded marketing deliverables | ⬜ | Phase 1 | Social copy, email templates |

### 2.2 Enhanced Reasoning & Explainability

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.2.1 | Reasoning trace visualization in UI | ⬜ | Phase 1 | Show "why" interactively |
| 2.2.2 | Context graph explorer UI | ⬜ | Phase 1 | Navigate decisions visually |
| 2.2.3 | Cross-stage consistency checker | ⬜ | Phase 1 | Flag inconsistencies |

### 2.3 Feedback Agent Tuning

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.3.1 | Signal detection threshold tuning | ⬜ | 1.7.4 | Reduce noise |
| 2.3.2 | Feedback categorization improvements | ⬜ | 1.7.3 | Better synthesis |
| 2.3.3 | Historical pattern detection | ⬜ | 1.7.3 | Learn from past cycles |

### 2.4 Additional Provider Support

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.4.1 | Add GPT-4o provider implementation | ⬜ | 1.1.2 | Test provider abstraction |
| 2.4.2 | Add Qdrant vector DB implementation | ⬜ | 1.1.3 | Test vector DB abstraction |
| 2.4.3 | Add Pinecone vector DB implementation | ⬜ | 1.1.3 | Managed option |

### 2.5 Advanced Reporting & Metrics

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.5.1 | Team/org rollup dashboard | ⬜ | 1.9.10 | Aggregate metrics across team members |
| 2.5.2 | Metric anomaly detection (approval rate drops, cycle time spikes) | ⬜ | 1.9.11 | Automated alerts based on trend deviation |
| 2.5.3 | Baseline comparison view ("first cycle vs. latest") | ⬜ | 1.9.11 | Show improvement over time |
| 2.5.4 | Export reporting data (CSV, API) | ⬜ | 1.9.2 | For external BI tools |

### 2.6 Advanced Gate Configuration

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.6.1 | Multi-approver gate UI | ⬜ | 1.12.6 | Show approval status per role |
| 2.6.2 | No-vote timeout alerts and auto-escalation UI | ⬜ | 1.12.7 | Notify backup approvers |
| 2.6.3 | Per-project gate configuration UI | ⬜ | 1.12.8 | Project settings page |

### 2.7 Support Ops Enhancements

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 2.7.1 | Support desk integration (Zendesk or Intercom) | ⬜ | 1.10.1 | First external support channel |
| 2.7.2 | Advanced pattern detection (cross-project trends) | ⬜ | 1.10.6 | Patterns across multiple products |
| 2.7.3 | Classification accuracy dashboard | ⬜ | 1.10.5, 1.9.10 | Override rate trends, per-category accuracy |

---

## Phase 3: Launch (Week 6)

### 3.1 Full Flywheel Demo

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 3.1.1 | End-to-end flywheel test suite | ⬜ | Phase 2 | Automated cycle testing |
| 3.1.2 | Demo scenario preparation | ⬜ | Phase 2 | Compelling walkthrough |
| 3.1.3 | Record demo video | ⬜ | 3.1.2 | For presentation |

### 3.2 Multi-Project Support

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 3.2.1 | Project creation/management UI | ⬜ | Phase 2 | |
| 3.2.2 | Project-scoped context graphs | ⬜ | Phase 2 | Isolation between projects |
| 3.2.3 | Project switching in UI | ⬜ | 3.2.1 | |

### 3.3 Documentation & Onboarding

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 3.3.1 | User documentation | ⬜ | Phase 2 | How to use POEM |
| 3.3.2 | Onboarding flow in product | ⬜ | Phase 2 | First-run experience |
| 3.3.3 | Example projects/templates | ⬜ | Phase 2 | Get started quickly |
| 3.3.4 | "Deploy at your company" guide | ⬜ | 0.4.4 | For sharing with coworkers |
| 3.3.5 | Licensing FAQ for companies | ⬜ | 0.4.5 | When AGPL vs commercial |

### 3.4 Evaluation & Launch Criteria

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 3.4.1 | Implement HHH evaluation framework | ⬜ | Phase 2 | Helpful, Honest, Harmless scoring |
| 3.4.2 | Set up metrics tracking | ⬜ | Phase 2 | Per PRD Section 3 |
| 3.4.3 | Complete 3+ internal flywheel cycles | ⬜ | Phase 2 | Launch gate requirement |
| 3.4.4 | Beta user recruitment | ⬜ | 3.3.1 | |
| 3.4.5 | Beta feedback collection system | ⬜ | 3.4.4 | |
| 3.4.6 | Support signal classification accuracy >85% | ⬜ | 1.10.5 | Launch gate: measured against human-classified test set |
| 3.4.7 | Gate configuration tested across 2+ org sizes | ⬜ | 1.12.6 | Launch gate requirement |

---

## Phase 4: Post-MVP Iteration

### 4.1 Additional Integrations

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 4.1.1 | GitHub integration | ⏸️ | Launch | Issue/PR creation |
| 4.1.2 | Jira integration | ⏸️ | Launch | |
| 4.1.3 | HubSpot integration | ⏸️ | Launch | Marketing automation |
| 4.1.4 | Notion integration | ⏸️ | Launch | Documentation export |
| 4.1.5 | Multiple analytics sources | ⏸️ | Launch | Richer feedback data |
| 4.1.6 | Azure OpenAI provider | ⏸️ | Launch | Enterprise compatibility |
| 4.1.7 | AWS Bedrock provider | ⏸️ | Launch | Enterprise compatibility |
| 4.1.8 | Zendesk integration (if not done in 2.7.1) | ⏸️ | Launch | Support ops channel |
| 4.1.9 | Intercom integration | ⏸️ | Launch | Support ops channel |

### 4.2 Advanced Features

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 4.2.1 | Team collaboration features | ⏸️ | Launch | Multi-user approval flows |
| 4.2.2 | API access for external tools | ⏸️ | Launch | |
| 4.2.3 | Custom agent configuration | ⏸️ | Launch | Adjust prompts via UI |
| 4.2.4 | Multilingual support | ⏸️ | Launch | Non-English briefs |
| 4.2.5 | Prompt versioning and A/B testing | ⏸️ | Launch | Optimize over time |
| 4.2.6 | Per-feature/function gate configuration | ⏸️ | 1.12.9 | For larger teams |

### 4.3 Responsible AI & Compliance

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 4.3.1 | AI content watermarking | ⏸️ | Launch | |
| 4.3.2 | SOC2 compliance preparation | ⏸️ | Launch | |
| 4.3.3 | Bias audit implementation | ⏸️ | Launch | Quarterly reviews |
| 4.3.4 | Enhanced content filtering | ⏸️ | Launch | Input validation |

### 4.4 Commercial Infrastructure (When Revenue Justifies)

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 4.4.1 | Set up Stripe for license payments | ⏸️ | Launch | |
| 4.4.2 | License key generation/validation | ⏸️ | 4.4.1 | |
| 4.4.3 | Customer portal for license management | ⏸️ | 4.4.1 | |
| 4.4.4 | Commercial support ticketing system | ⏸️ | 4.4.1 | |

### 4.5 Monitoring, Auditing & Advanced Telemetry

| ID | Task | Status | Dependencies | Notes |
|----|------|--------|--------------|-------|
| 4.5.1 | Dedicated monitoring service (health checks, alerts, uptime) | ⏸️ | Launch | Builds on system_health events from 1.9.12 |
| 4.5.2 | Audit trail export (compliance-ready event logs) | ⏸️ | Launch | Append-only ActivityStore enables this |
| 4.5.3 | Cost tracking dashboard (LLM API spend per project/user) | ⏸️ | Launch | Derived from api_call_made events |
| 4.5.4 | Advanced anomaly detection (ML-based trend analysis) | ⏸️ | 2.5.2 | Upgrade from rule-based to learned thresholds |

---

## PRD Deliverables Tracker

| Section | PRD Status | Eval Ready | Notes |
|---------|------------|------------|-------|
| 1. Problem Definition | 🟢 Complete | N/A | v1.3 — added support signals pain point |
| 2. Solution Definition | 🟢 Complete | N/A | v1.3 — agent roles, gate framework, work item hierarchy, support ops, sequential flow, question routing |
| 3. Core Metrics | 🟢 Complete | N/A | v1.2 — expanded with tracking mechanism, time-savings model; v1.3 added support classification accuracy metric |
| 4. Prioritization | 🟢 Complete | N/A | v1.3 — new risk assessments for Support Ops, Service Engineering, Gate Engine |
| 5. Roadmap | 🟢 Complete | N/A | v1.3 — updated all phases with new components |
| 6. Evaluations | 🟢 Complete | ⬜ | v1.3 — added HHH evals for support classification and service engineering; need to create eval spreadsheet |
| 7. Responsible AI | 🟢 Complete | N/A | v1.3 — added support data sensitivity, classification bias |
| 8. Pricing | 🟢 Complete | N/A | v1.1 |
| User Flow Diagrams | 🟢 Complete | N/A | v2.0 — 9 Mermaid diagrams aligned with PRD v1.3 |
| Evaluation Spreadsheet | ⬜ Not Started | N/A | Link to add to PRD |

---

## Weekly Goals

### Pre-Week 1 (ASAP - Personal Time)
- [x] Create poem-core repo on personal GitHub ✅ sreynolds100/poem-core
- [x] Complete Phase 0 open source setup (0.1.2-0.1.11) ✅ All license files, README, structure committed
- [x] Complete portability architecture design (0.2.x) ✅ Abstractions, config schema, prompt externalization
- [x] Initial Dockerfile and docker-compose (0.3.1, 0.3.2) ✅ Python 3.11 + pgvector stack
- [x] Set up CLA bot (0.1.5) ✅ CLA Assistant configured on cla-assistant.io
- [x] User flow diagrams (v2.0) ✅ 9 Mermaid diagrams

### Week 1
- [ ] Complete remaining infrastructure setup (1.1.x)
- [ ] Orchestrator state machine design with named gates and backlog (1.2.1, 1.2.7)
- [ ] Product Agent basic implementation (1.3.1-1.3.5)
- [ ] EventBus schema + ActivityStore postgres tables (1.9.1-1.9.3)
- [ ] Resolve design discussions D1 (gate config) and D2 (work item hierarchy) — needed for Engineering Agent and Gate Engine implementation
- [ ] Approval Gate Engine: single-decider + rejection-to-backlog (1.12.1-1.12.5)

### Week 2
- [ ] Complete Orchestrator with sequential routing (1.2.x including 1.2.8)
- [ ] Complete Product Agent with UI (1.3.x)
- [ ] Engineering Agent with work item hierarchy (1.5.x + 1.13.x)
- [ ] Cross-agent question protocol design (1.14.1)
- [ ] Wire EventBus into Orchestrator + approval gates (1.9.4, 1.9.6)

### Week 3
- [ ] DevOps Agent — sequential after Engineering (1.4.x)
- [ ] Marketing Agent (1.6.x)
- [ ] Begin Feedback Agent (1.7.1-1.7.5)
- [ ] Support Ops Agent basic classification (1.10.1-1.10.5)
- [ ] Service Engineering Agent basic investigation (1.11.1-1.11.3)
- [ ] Time-savings model + calibration prompts (1.9.7-1.9.8)
- [ ] Personal + project reporting dashboard (1.9.10-1.9.11)

### Week 4
- [ ] Complete Feedback Agent (1.7.x)
- [ ] Close the flywheel loop (1.7.9)
- [ ] Reference integrations (1.8.x)
- [ ] Wire EventBus into all agents (1.9.5)
- [ ] Support Ops → Feedback Agent connection (1.10.8)
- [ ] Begin MVP+1 enhancements (2.1.x)

### Week 5
- [ ] Complete MVP+1 features (2.x)
- [ ] Reasoning trace visualization
- [ ] Feedback Agent tuning
- [ ] Test additional providers (2.4.x)
- [ ] Team/org rollup + anomaly detection (2.5.x)
- [ ] Advanced gate configuration (2.6.x)
- [ ] Support ops enhancements (2.7.x)

### Week 6
- [ ] Full flywheel demo (3.1.x)
- [ ] Documentation including licensing guide (3.3.x)
- [ ] Launch criteria validation (3.4.x) — including classification accuracy and gate config tests
- [ ] Cohort presentation preparation

---

## Decision Log

| Date | Decision | Rationale | Impact |
|------|----------|-----------|--------|
| 2026-02-28 | Renamed Operations Agent → DevOps Agent | "Operations" was ambiguous; "DevOps" clarifies infrastructure/deployment ownership; "Platform Agent" rejected (implies architecture ownership) | Rename throughout codebase; update prompts directory |
| 2026-02-28 | Added Support Ops Agent + Service Engineering Agent | Support signals are a critical missing feedback channel; three-category classification (bug/feature/UX confusion) ensures right team gets right signal | 2 new agents, 16 new build tasks |
| 2026-02-28 | Named approval gates: Intake, Technical Review, GTM Review, Iteration Review | Named gates clearer than numbered; each has distinct purpose | Update all gate references in code and UI |
| 2026-02-28 | Configurable approver roles per gate | Different org structures need different approval patterns; solo founder default = single-decider | New Approval Gate Engine component (1.12.x), 9 tasks |
| 2026-02-28 | Rejection → backlog (not archive) | Rejected ideas aren't dead; preserving rationale enables resurfacing | Backlog management in Orchestrator + UI |
| 2026-02-28 | Engineering → DevOps sequential (not parallel) | DevOps specs depend on engineering approach | Orchestrator routing change (1.2.8) |
| 2026-02-28 | Engineering/DevOps → Product question routing | Without feedback loops, ambiguous requirements waste cycles | Cross-agent question protocol (1.14.x), 5 tasks |
| 2026-02-28 | Work item hierarchy: Ideas → Epics → Stories → Tasks | Flat tickets miss important structure; configurable depth accommodates teams | New hierarchy component (1.13.x), 6 tasks |
| 2026-02-28 | Support signal classification: bug / feature request / UX confusion | Three distinct categories ensure signals reach the right team; UX confusion is the most valuable category because it's typically lost | Support Ops Agent (1.10.x), 10 tasks |
| 2026-02-28 | CLA bot configured via CLA Assistant | Automated CLA signing for PRs; linked to public CLA gist on gist.github.com | Task 0.1.5 complete, blocker R2 resolved |
| 2026-02-28 | EventBus + ActivityStore as separate component | UI and agents all emit events; Orchestrator shouldn't own UI telemetry; separate component scales for future monitoring/auditing | Phase 1.9 tasks, 12 build items |
| 2026-02-28 | Time-savings model: industry defaults + user calibration | Pure defaults lack credibility; pure user input adds friction; hybrid gives useful numbers from day one that personalize over time | Time estimate prompt added to approval gates |
| 2026-02-28 | Phase 0 files committed with poem.pdm@gmail.com contact | Dedicated project email separates personal from project communications | All license files, templates, and docs use this email |
| 2026-02-28 | Full AGPL-3.0 text included in LICENSE file | Custom header alone is insufficient; full text required for legal enforceability | LICENSE file now ~650 lines |
| 2026-02-28 | pyproject.toml with optional dependency groups | pinecone and qdrant as optional extras keeps base install lean | `pip install poem-core[pinecone]` pattern |
| 2026-02-28 | GitHub repo created: sreynolds100/poem-core | Establishing IP ownership with timestamp | Phase 0.1.1 complete |
| 2026-02-27 | Full flywheel for MVP (shallow depth) | Core differentiator is the closed loop; partial implementation doesn't validate hypothesis | All 8 agents in scope |
| 2026-02-27 | Markdown format for all docs | Easier iteration and version control | Versioning: decimal (1.1, 1.2) for minor, full for major |
| 2026-02-27 | Open source core + instance separation | Protect IP, enable portability across jobs/companies | Must complete Phase 0 on personal time before any company use |
| 2026-02-27 | AGPL + Commercial dual licensing | Enables revenue while staying "open source"; AGPL triggers enterprise license purchases | Need CLA for contributors |
| 2026-02-27 | pgvector as default vector DB | Free, self-hostable, portable, good enough for MVP | Can add Pinecone/Qdrant later |
| 2026-02-27 | Prompts externalized to files | Portability, version control, easy customization | /prompts directory structure |

---

## Blockers & Risks

| ID | Issue | Severity | Owner | Status | Resolution |
|----|-------|----------|-------|--------|------------|
| R1 | Must add license files to repo before any code | High | Samantha | ✅ Resolved | All license files committed 2026-02-28 |
| R2 | CLA bot setup required before accepting contributions | Medium | Samantha | ✅ Resolved | CLA Assistant configured on cla-assistant.io, linked to public CLA gist |
| R3 | Design discussions D1-D5 must be resolved before Phase 1 implementation | Medium | Samantha | Open | Gate config schema, work item hierarchy, support ops integration, service eng scope, question protocol |

---

## IP Protection Checklist

Before using POEM at any company, verify:

- [x] poem-core repo exists on personal GitHub ✅ sreynolds100/poem-core
- [x] AGPL LICENSE file committed ✅ Full AGPL-3.0 text + custom header
- [x] COMMERCIAL_LICENSE.md is in place ✅ Pricing tiers, FAQ, contact email
- [x] CLA.md is in place ✅ Dual licensing grant, signing instructions
- [x] CLA bot configured ✅ CLA Assistant on cla-assistant.io
- [ ] Initial commits made from personal machine, personal email
- [x] README and LICENSE committed with clear timestamps ✅
- [ ] No company resources used for core development
- [x] Clear documentation of what is open source vs instance-specific ✅ README + CONTRIBUTING
- [x] All source files have AGPL copyright headers ✅ All 47 files

---

## Notes

- **Phase 0 is critical** — must be done on personal time before any company involvement
- **AGPL + CLA = future revenue option** — set up correctly from day 1
- This tracker should be updated as work progresses
- Version this file alongside the PRD (POEM_Tracker_v1.6.md)
- Add new tasks as they're discovered during implementation
- **Always produce full tracker versions, never deltas**

---

*End of Tracker - Version 1.6*
