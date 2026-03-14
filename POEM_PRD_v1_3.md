# POEM: Product → Operations → Engineering → Marketing

**An Agentic AI System for Full Product Lifecycle Orchestration**

PRD - Cohort 8 Submission  
Author: Samantha  
Date: February 2026  
Version: 1.3

**GitHub Repository:** [sreynolds100/poem-core](https://github.com/sreynolds100/poem-core)  
**Contact:** poem.pdm@gmail.com  
**License:** AGPL-3.0 (open source) + Commercial dual license

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.3 | 2026-02-28 | Renamed Operations Agent → DevOps Agent; added Support Operations Agent and Service Engineering Agent; defined agent roles and responsibilities; redesigned approval gates (Intake, Technical Review, GTM Review, Iteration Review) with configurable approver roles and policies; added work item hierarchy (Ideas → Epics → Stories → Tasks); changed rejection flow from archive to backlog; added feedback loops from Engineering/DevOps back to Product; made Engineering → DevOps sequential (not parallel); added Support/Service feedback channel with bug/feature request/UX confusion classification; new functional requirements for all additions |
| 1.2 | 2026-02-28 | Added EventBus + ActivityStore to architecture (Section 2), expanded Core Metrics with tracking mechanism and time-savings model (Section 3), new functional requirements for telemetry and reporting |
| 1.1 | 2026-02-27 | Added GitHub repo reference, dual licensing model (AGPL + Commercial), portability architecture, updated tech stack (pgvector default), open source strategy, instance separation pattern, updated pricing to reflect licensing tiers |
| 1.0 | 2026-02-27 | Initial PRD — all 8 sections complete |

---

## 1. Problem Definition

### What problem is this solving?

Solo founders and small startup teams spend 60-70% of their time on cross-functional coordination rather than strategic work. The core pain points include:

**Context Loss During Handoffs:** Critical product decisions, user insights, and technical constraints get lost when transitioning between product discovery, engineering implementation, and go-to-market activities. Teams repeatedly re-explain the "why" behind decisions.

**Siloed Tools and Workflows:** Product managers use Notion/Figma, engineers use GitHub/Jira, marketers use HubSpot/Mailchimp. No system maintains the connective tissue between these stages.

**No Feedback Loop Closure:** Market feedback, user analytics, and support operations signals rarely flow back to inform the next product iteration in a structured way. The "flywheel" is broken.

**Manual Artifact Generation:** PRDs, engineering tickets, deployment configs, and marketing copy are created manually with substantial duplication of effort.

**Support Signals Lost in the Void:** Bug reports, feature requests, and UX confusion reports from service and support teams are handled reactively. Patterns that should inform product iteration are buried in ticket queues and never make it back to product or engineering in a structured way.

### Who are you solving this problem for?

**Primary Target Personas:**

| Persona | Profile | Key Pain Points |
|---------|---------|-----------------|
| Solo Technical Founder | Building MVP alone or with 1-2 contractors. Technical background but wears all hats. | Context switching between code, marketing, and product planning. No bandwidth for proper documentation. |
| Startup PM (Seed-Series A) | First PM hire at early-stage startup. Reports to founder. Team of 3-10 engineers. | Translating product vision into engineering tickets while also managing launch. Information scattered across tools. |
| Mid-Size Company PM | PM at company with 50-500 employees. Manages 2-3 products. Cross-functional coordination is primary role. | Spending 60%+ time in meetings syncing teams. Wants to automate repetitive coordination work. |

*Initial MVP Focus: Solo technical founders and startup PMs—those with the highest pain-to-resource ratio.*

### Why is this problem worth solving?

The market opportunity is substantial. The global project management software market is valued at $6.68 billion (2024) with 15.7% CAGR. However, existing solutions focus on single-stage optimization rather than cross-stage orchestration.

**POEM's Competitive Moats:**

1. **Full-Lifecycle Context Graph:** Unlike engineering-focused tools (Cursor, GitHub Copilot) or PM tools (Notion AI), POEM maintains context across Product → Operations → Engineering → Marketing.

2. **Flywheel Loop Architecture:** Market feedback and support operations signals automatically flow back to product discovery, creating compounding value. This closed-loop system is the core differentiator—most tools treat product development as linear rather than cyclical.

3. **Human-in-the-Loop Approval Gates:** AI suggests, humans approve—maintaining accountability while automating the grunt work. Gates are configurable by role, policy, and organizational structure.

4. **Artifact Transformation with Reasoning:** Each generated artifact (PRD → ticket → marketing brief) includes explainable provenance.

5. **Integration-First Design:** Built to connect existing tools (GitHub, Notion, Slack, analytics platforms, support systems) rather than replace them.

6. **Open Source Core with Portability:** POEM's core engine is open source under AGPL-3.0, ensuring users are never locked in to a single vendor or hosting provider. The provider abstraction layer means teams can swap LLMs, vector databases, and integrations without rewriting their workflows.

### Why Agentic AI?

Rule-based automation fails for product lifecycle orchestration because:

**Unstructured Data:** Product decisions, user feedback, support tickets, and market signals come in varied formats—meeting notes, Slack threads, analytics dashboards, customer emails, bug reports with ambiguous descriptions.

**Complex Reasoning:** Converting a product requirement into engineering tickets requires understanding technical constraints, prioritization logic, and team capacity—not simple if/then rules. Classifying support signals as bugs vs. feature requests vs. UX confusion requires contextual understanding.

**Context Preservation:** LLMs with persistent memory can maintain the "why" behind decisions across stages, something traditional automation cannot do.

**Adaptive Planning:** Agentic AI can dynamically adjust workflows based on changing requirements, failed deployments, or unexpected market feedback.

**Cross-Domain Translation:** Moving from product language to engineering language to marketing language requires semantic understanding that rule-based systems cannot achieve.

---

## 2. Solution Definition

### System Architecture Overview

POEM operates as a multi-agent system with an orchestrator coordinating specialized agents for each lifecycle stage. The architecture is designed to demonstrate the complete flywheel—from initial idea through market feedback and back to product iteration.

The "Operations" in POEM encompasses two distinct operational domains: **DevOps** (infrastructure, deployment, CI/CD) and **Support Operations** (service delivery, bug triage, UX feedback). This keeps the POEM acronym while reflecting the full operational scope of bringing a product to market and keeping it running.

The full source code is available at [sreynolds100/poem-core](https://github.com/sreynolds100/poem-core) under AGPL-3.0 with commercial licensing options.

```
[User Input] → [Orchestrator Agent] → [Stage Agents] → [Human Approval Gates] → [Artifact Output]
                      ↑                                                                │
                      ├─────────────── [Feedback Agent] ←──────────────────────────────┘
                      │                      ↑
                      │    [Support Ops Agent + Service Engineering Agent]
                      │         ↑
                      │    [Support Tickets, Bug Reports, UX Confusion Reports]
                      │
                  All components emit to:
              [EventBus] → [ActivityStore] → [Reporting Dashboard]
```

### Core Components

1. **Orchestrator Agent:** Routes tasks to appropriate stage agents, maintains lifecycle context graph, manages handoffs and approval gates, and tracks the overall flywheel state. Manages the backlog for rejected/deferred ideas.

2. **Product Agent:** Generates PRDs, user stories, acceptance criteria from product briefs and user research. Entry point for new ideas. Owns the "what" and "why" of product decisions.

3. **DevOps Agent:** (formerly "Operations Agent") Transforms approved engineering plans into deployment configs, infrastructure specs, CI/CD pipelines, and operational runbooks. Works downstream of the Engineering Agent because infrastructure decisions depend on technical approach. Named "DevOps" rather than "Platform" to avoid implying ownership of architecture decisions, which belong to Engineering.

4. **Engineering Agent:** Breaks down approved PRDs into a structured work item hierarchy (epics → stories → tasks), estimates complexity, identifies dependencies, and suggests technical approaches. Works upstream of DevOps because technical decisions inform infrastructure needs. Can raise questions back to the Product Agent when requirements are ambiguous or technically infeasible.

5. **Marketing Agent:** Creates launch briefs, positioning documents, messaging frameworks from product context. Ensures go-to-market alignment with the original product intent.

6. **Feedback Agent:** Ingests market data, user analytics, and synthesized support operations signals to inform the next iteration. Closes the flywheel loop by feeding insights back to the Product Agent. Receives classified signals from the Support Operations Agent.

7. **Support Operations Agent:** Monitors service and support channels (help desk tickets, bug reports, customer complaints). Classifies incoming signals into three categories: (a) **Bug reports** — something is broken, routes to Engineering; (b) **Feature requests** — something is missing, routes to Product via Feedback Agent; (c) **UX confusion** — working as designed but users think it's broken, routes to Product + Engineering. This third category is especially valuable because it's often lost — support closes it as "working as intended" and nobody ever fixes the underlying UX problem.

8. **Service Engineering Agent:** Handles the technical investigation side of support escalations. When the Support Ops Agent classifies an issue as a potential bug or ambiguous UX problem, the Service Engineering Agent can reproduce, investigate root cause, and provide technical context before the issue reaches the Feedback Agent or Engineering Agent. Prevents the Engineering Agent from receiving poorly-scoped bug reports.

9. **EventBus:** A lightweight, cross-cutting telemetry layer that captures events from all components — agent actions, orchestrator state transitions, approval gate decisions, and user interactions (including time-savings estimates). Decoupled from all agents so each component simply emits events without knowing about storage or reporting. Designed as a separate service so it can scale independently and later support monitoring, auditing, and compliance needs.

10. **ActivityStore:** A structured event log (postgres tables alongside the existing pgvector context graph) that stores all telemetry data. Serves as the single source of truth for metrics, reporting dashboards, and future audit trails. Append-only by design for data integrity.

### Agent Roles & Responsibilities

Each agent in POEM maps to a real-world role. This clarifies ownership boundaries and prevents confusion about which agent handles what.

| Agent | Real-World Role Equivalent | Owns | Does NOT Own |
|-------|---------------------------|------|-------------|
| Product Agent | Product Manager | What to build and why; PRDs, user stories, acceptance criteria, prioritization | How to build it; infrastructure decisions; marketing execution |
| Engineering Agent | Tech Lead / Engineering Manager | How to build it; work item breakdown, complexity estimates, technical approach, dependency mapping | What to build (that's Product); where to deploy (that's DevOps) |
| DevOps Agent | DevOps / Infrastructure Engineer | Where and how to deploy; infrastructure specs, CI/CD, deployment configs, environment setup, monitoring | Architecture decisions (that's Engineering); what to build (that's Product) |
| Marketing Agent | Product Marketing Manager | How to position and launch; messaging, positioning, audience definition, launch briefs | Product strategy; pricing decisions; technical implementation |
| Feedback Agent | Product Analyst / Insights Lead | Synthesizing signals into actionable iteration proposals; connecting feedback to original requirements | Generating the feedback itself; investigating bugs; triaging support tickets |
| Support Ops Agent | Support Operations Manager | Classifying and routing support signals; monitoring service channels; identifying patterns in support volume | Fixing bugs; making product decisions; technical investigation |
| Service Engineering Agent | Support Engineer / Escalation Engineer | Technical investigation of support issues; root cause analysis; reproducing bugs; providing engineering context to support signals | Product decisions; deployment changes; marketing |

### Approval Gate Framework

POEM uses four named approval gates, each with a specific purpose. Gates are the primary mechanism for human oversight — no artifact proceeds without explicit human approval.

#### Gate Definitions

| Gate | Name | Purpose | Triggered After |
|------|------|---------|----------------|
| Gate 1 | **Intake** | "Should we pursue this idea?" Evaluates whether the product brief warrants investment of engineering and operational resources. | Product Agent generates PRD |
| Gate 2 | **Technical Review** | "Is the engineering plan sound and the infrastructure approach viable?" Evaluates whether the technical breakdown and DevOps specs are feasible, well-scoped, and aligned with the PRD intent. | Engineering Agent + DevOps Agent complete their outputs |
| Gate 3 | **GTM Review** | "Is the go-to-market plan aligned with the product?" Evaluates whether the marketing brief accurately reflects product capabilities and is ready for launch. | Marketing Agent generates launch brief |
| Gate 4 | **Iteration Review** | "Does this feedback warrant a new cycle?" Evaluates whether synthesized feedback and support signals justify starting a new flywheel iteration. | Feedback Agent generates iteration proposal |

#### Gate Outcomes

Each gate can produce one of three outcomes:

- **Approve** — Artifact is finalized, stored in context graph, and the next stage is triggered. Time-savings calibration prompt fires.
- **Revise** — User provides specific feedback. The originating agent re-generates with revision context. The artifact returns to the same gate.
- **Reject** — Idea is moved to the **prioritized backlog** with the rejection rationale attached, so it can be resurfaced later when conditions change. A rejection explanation is sent to the original submitter. Rejection is "not now" — not "never."

#### Configurable Approver Roles

Different organizations need different approval structures. POEM supports configurable approver roles at each gate, settable at the platform level, per-project, or per-feature/function for larger teams.

**Configuration Options per Gate:**

- **Required Approvers:** A list of roles that must approve (e.g., Gate 2 requires "Engineering Lead" + "DevOps Lead")
- **Approval Policy:** How approvals are aggregated:
  - *Unanimous* — All required approvers must approve
  - *Majority* — More than half of required approvers must approve
  - *Single-Decider* — One designated role has final authority, with other roles providing advisory input
- **No-Vote Handling:** What happens when a required approver doesn't respond:
  - *Treat as abstain* — Doesn't count for or against (default)
  - *Treat as block* — No response = implicit rejection
  - *Auto-escalate after timeout* — Escalates to a designated backup approver after configurable timeout period
- **Tie-Breaking:** When using majority policy, a configurable tie-breaker role casts the deciding vote

**Default Configuration (Solo Founder):**

For the MVP target persona (solo founder), the default is simple: single-decider at all gates, with the user as the sole approver. Teams can reconfigure as they grow.

**Example Configurations:**

| Org Type | Gate 1 (Intake) | Gate 2 (Technical) | Gate 3 (GTM) | Gate 4 (Iteration) |
|----------|----------------|-------------------|-------------|-------------------|
| Solo Founder | Founder (single) | Founder (single) | Founder (single) | Founder (single) |
| Seed Startup (5 people) | PM (single) | PM + Tech Lead (unanimous) | PM + Marketing Lead (unanimous) | PM (single) |
| Series A (20 people) | PM + Founder (majority) | Engineering Lead + DevOps Lead + PM (majority) | PM + Marketing Director (unanimous) | PM + Data Analyst (majority) |
| Mid-Size (50+ people) | Product Committee (majority, 3 members) | Architecture Review Board (unanimous) | GTM Team (majority) | Product + Analytics (single-decider: VP Product) |

### Work Item Hierarchy

After Gate 2 (Technical Review) approval, the Engineering Agent produces a structured work item hierarchy rather than flat tickets. This follows industry best practices while allowing customization.

**Standard Hierarchy:**

```
Idea (from Gate 1)
└── Epic (major feature area)
    └── Story (user-facing value increment: "As a user, I want...")
        └── Task / Ticket (implementable unit of work)
```

**Level Definitions:**

| Level | What It Represents | Generated By | Example |
|-------|-------------------|-------------|---------|
| Idea | The original product concept that entered the flywheel | User input → Product Agent | "Add real-time collaboration to the editor" |
| Epic | A major feature area that groups related work. Maps to a significant deliverable. | Engineering Agent (from approved PRD) | "Real-time cursor tracking and presence" |
| Story | A user-facing value increment with clear acceptance criteria. Follows "As a [user], I want [action], so that [value]" format. | Engineering Agent (from epic breakdown) | "As an editor, I want to see other users' cursors, so I know where they're working" |
| Task / Ticket | The smallest implementable unit of work. Has clear definition of done, complexity estimate, and dependency mapping. | Engineering Agent (from story breakdown) | "Implement WebSocket connection for cursor position broadcast — 3 story points" |

**Configurable Hierarchy Levels:**

Not all teams use all levels. POEM allows teams to configure which levels they use:

- **Minimal (solo founder):** Idea → Tasks (skip epics and stories)
- **Standard (small team):** Idea → Epics → Stories → Tasks
- **Expanded (larger teams):** Idea → Themes → Epics → Stories → Sub-tasks

The Engineering Agent adapts its output granularity based on the configured hierarchy. This is set in `config.yaml` under the `engineering_agent.work_item_hierarchy` key.

### Portability Architecture

POEM is built from the ground up with portability and self-hosting as first-class concerns. The architecture uses abstraction layers so that no single vendor creates lock-in.

**Provider Abstraction Layer:**

All external dependencies are accessed through abstract interfaces that allow swappable implementations:

- **LLM Providers:** `BaseLLMProvider` interface with `generate()` and `generate_structured()` methods. Implementations exist for Anthropic (Claude), OpenAI (GPT), and Azure OpenAI. New providers can be added by extending the base class.
- **Vector Database Providers:** `BaseVectorDB` interface with `store()`, `query()`, and `delete()` methods. Default implementation is pgvector (free, self-hostable). Optional support for Pinecone and Qdrant via extras (`pip install poem-core[pinecone]`).
- **Integration Providers:** `BaseIntegration` interface with `connect()`, `push()`, `pull()`, and `health_check()` methods. Reference implementations for Jira, Linear, and Slack in the integrations directory.

**Configuration-Driven Deployment:**

All runtime configuration is managed through `config.yaml` with environment variable overrides for secrets. A fully documented `config.example.yaml` is included in the repo covering LLM selection, vector DB connection, agent behavior, orchestrator settings, integrations, UI options, server config, and logging levels.

**Externalized Prompts:**

All agent prompts live in the `/prompts/defaults/` directory as plain text files, organized by agent. This allows prompt customization without modifying source code, enables version control of prompt iterations, and supports the instance separation pattern (see Open Source Strategy below).

### Open Source Strategy & Instance Separation

POEM separates the **core engine** (open source, AGPL-3.0) from **instance configuration** (private, user-owned):

```
poem-core/                      # AGPL Licensed — open source
├── poem/                       # Core engine, agents, orchestrator
├── providers/                  # LLM and vector DB abstractions
├── integrations/               # Base interfaces + reference implementations
├── prompts/defaults/           # Generic starter prompts
└── tests/

poem-instance-template/         # Template for company/personal deployments
├── config.yaml                 # Your actual config (gitignored secrets)
├── prompts/                    # Your custom prompts (YOUR IP)
├── integrations/               # Your custom connectors (YOUR IP)
└── branding/                   # Your logos, colors, etc.
```

This separation means the core engine stays open and community-maintained, while company-specific customizations (prompts, integrations, branding) remain private and are owned by whoever creates them. A `poem-instance-template` repository will provide a reference implementation for bootstrapping new deployments.

### Self-Hosting & Containerization

POEM ships with Docker support for straightforward self-hosting:

- **Dockerfile:** Python 3.11-slim base image with health check endpoints and pgvector dependencies
- **docker-compose.yaml:** Full stack definition including POEM core + pgvector/pgvector:pg16 with persistent volumes and health checks
- **Target hosting:** Designed to run on infrastructure as modest as a $5/month VPS (DigitalOcean, Hetzner), as well as managed platforms (Railway, Render) or cloud Kubernetes

### The Flywheel in Action

The key differentiator is the closed loop. Here's how a complete cycle works:

1. **Idea → PRD:** User inputs product brief, Product Agent generates structured PRD
2. **PRD → Intake Gate:** Human reviews PRD (Gate 1: Intake). Approve, revise, or reject to backlog.
3. **PRD → Work Items:** Engineering Agent breaks approved PRD into epics, stories, and tasks
4. **Work Items → Infrastructure:** DevOps Agent creates deployment and infrastructure specs based on engineering plan (sequential — Engineering informs DevOps)
5. **Engineering + DevOps → Technical Review Gate:** Human reviews technical plan (Gate 2: Technical Review). Engineering or DevOps can raise questions back to Product Agent if requirements are unclear or infeasible.
6. **PRD → Launch Brief:** Marketing Agent creates go-to-market materials from approved PRD + product context
7. **Launch Brief → GTM Review Gate:** Human reviews marketing plan (Gate 3: GTM Review)
8. **Launch → Feedback:** Feedback Agent monitors market response, user analytics, AND support operations signals
9. **Feedback → Iteration Review Gate:** Feedback Agent synthesizes insights and proposes next iteration (Gate 4: Iteration Review)
10. **Iteration → Next Cycle:** Approved iteration feeds back to Product Agent, starting a new flywheel cycle

Each transition preserves context, so the Marketing Agent knows *why* a feature was prioritized, and the Feedback Agent can trace user complaints back to original requirements.

### User Flows

#### Primary Flow: Idea to Launch to Iteration (Full Flywheel)

**Input:** User provides product brief (natural language description of feature/product idea)

**Processing:**

- Product Agent generates PRD with user stories and acceptance criteria
- Human reviews PRD at **Gate 1 (Intake):**
  - Approve → continues to Engineering
  - Revise → Product Agent re-generates with feedback
  - Reject → Idea moves to prioritized backlog with rejection rationale; submitter notified
- Engineering Agent breaks approved PRD into work item hierarchy (epics → stories → tasks)
  - Engineering Agent can raise questions back to Product Agent if requirements are ambiguous or technically infeasible
- DevOps Agent generates deployment/infrastructure specs based on Engineering output (sequential, not parallel)
  - DevOps Agent can raise questions back to Product Agent or Engineering Agent if specs conflict with infrastructure constraints
- Human reviews engineering plan + DevOps specs at **Gate 2 (Technical Review)**
- Marketing Agent generates launch brief from PRD + product context
- Human reviews marketing materials at **Gate 3 (GTM Review)**
- Product launches, Feedback Agent monitors response from multiple channels:
  - Market analytics (adoption, engagement, retention)
  - User feedback (surveys, reviews, direct feedback)
  - Support operations signals (classified by Support Ops Agent)
- Feedback Agent synthesizes insights and proposes next iteration
- Human reviews iteration proposal at **Gate 4 (Iteration Review)** → Approved iterations return to Product Agent

**Output:** Complete cycle—approved PRD, work item hierarchy, DevOps specs, marketing brief, and feedback-driven next iteration proposal

#### Secondary Flow: Feedback-Triggered Iteration

**Input:** Feedback Agent detects significant signal (user complaints, adoption metrics, market shift)

**Processing:**

- Feedback Agent synthesizes findings with context from original PRD
- Proposes iteration to Product Agent
- Product Agent generates updated PRD or new feature brief
- Cycle continues through Engineering, DevOps, and Marketing

**Output:** Context-aware iteration that references original decisions

#### Tertiary Flow: Support Operations Signal Processing

**Input:** Support ticket, bug report, or customer complaint arrives through service channels

**Processing:**

- Support Operations Agent classifies the signal:
  - **Bug** → Service Engineering Agent investigates, confirms, provides technical context → routes to Engineering Agent with reproduction steps and root cause analysis
  - **Feature Request** → Enriched with frequency data and user context → routes to Feedback Agent for synthesis with other signals
  - **UX Confusion** (working as designed but confusing) → Tagged with user journey context → routes to both Product Agent (for UX rethink) and Engineering Agent (for implementation assessment)
- All classified signals feed into the Feedback Agent for pattern detection and iteration proposals

**Output:** Classified, enriched support signals that inform product iteration rather than dying in a ticket queue

### Addressing AI Drawbacks

| Risk | Mitigation Strategy | Implementation |
|------|---------------------|----------------|
| Hallucination | Human approval gates at each stage transition | No artifact proceeds without explicit human confirmation |
| Explainability | Reasoning traces attached to all generated content | Each artifact shows "why" with links to source context |
| Context Drift | Persistent lifecycle context graph | Vector DB stores all decisions, rationale, and connections |
| Over-automation | AI suggests, human decides | Clear delineation between automation and decision points |
| Feedback Noise | Signal detection thresholds | Feedback Agent filters noise before proposing iterations |
| Support Signal Misclassification | Service Engineering Agent validation | Technical investigation before routing prevents miscategorized bugs/UX issues |
| Vendor Lock-in | Provider abstraction layer | Swap LLMs, vector DBs, or integrations without rewriting workflows |
| Approval Bottlenecks | Configurable gate policies with timeouts | Auto-escalation prevents stalled flywheel cycles |

### Functional Requirements (User Stories)

**Core Flywheel:**

- As a solo founder, I want to input a product idea in natural language and receive a structured PRD, so I can move faster from ideation to execution.

- As a startup PM, I want to automatically generate a structured work item hierarchy (epics, stories, tasks) from an approved PRD, so I can reduce manual translation work by 50%.

- As a product team, I want to review and approve all AI-generated artifacts before they're finalized, so I maintain control over quality.

- As a marketing lead, I want to receive launch briefs that reference the original product decisions, so I can create messaging that's consistent with product intent.

- As a founder, I want market feedback to automatically inform my next product iteration, so the flywheel keeps spinning without manual synthesis.

- As a PM, I want to see the reasoning behind each generated artifact, so I can trust the AI's suggestions and catch errors early.

**DevOps & Engineering:**

- As a DevOps engineer, I want deployment specs that are generated after the engineering plan is finalized, so infrastructure decisions are based on actual technical approach rather than assumptions.

- As a tech lead, I want the Engineering Agent to raise questions back to Product when requirements are ambiguous, so we don't waste cycles building the wrong thing.

- As an engineering manager, I want to configure the work item hierarchy depth (epics only, epics + stories, full breakdown) to match my team's workflow, so POEM adapts to how we work rather than forcing a structure.

**Approval Gates:**

- As a team lead, I want to configure who approves at each gate (by role, not individual) so that approval workflows match my org structure.

- As a VP of Product, I want to set approval policies (unanimous, majority, single-decider) per gate, so critical gates like Technical Review require consensus while routine gates move faster.

- As an admin, I want rejected ideas to go to a prioritized backlog with the rejection rationale, so good ideas aren't lost — just deferred.

- As a submitter, I want to receive a clear explanation when my idea is rejected at Intake, so I understand what would need to change for it to be reconsidered.

- As a team lead, I want no-vote timeouts to auto-escalate to a backup approver, so the flywheel doesn't stall waiting on unresponsive reviewers.

**Support Operations:**

- As a support manager, I want incoming tickets automatically classified as bugs, feature requests, or UX confusion, so the right team gets the right signal without manual triage.

- As a product manager, I want UX confusion reports (working as designed but confusing to users) surfaced separately from bugs, so I can address poor user experiences that would otherwise be closed as "not a bug."

- As an engineering lead, I want bug reports to arrive with reproduction steps and root cause analysis from the Service Engineering Agent, so my team doesn't waste time on poorly-scoped tickets.

- As a PM, I want support signal patterns (e.g., "20 users reported confusion about the same flow this week") to feed into the Feedback Agent's iteration proposals, so recurring issues drive product improvement.

**Self-Hosting & Customization:**

- As a technical user, I want to self-host POEM on my own infrastructure, so I maintain full control over my data and costs.

- As a team lead, I want to customize prompts and integrations for my company without forking the core engine, so I can benefit from upstream updates while keeping my customizations private.

**Telemetry & Reporting:**

- As a solo founder, I want to see how much time POEM is saving me each week, so I can justify continued use and quantify the value.

- As a PM, I want to provide my own time estimates for manual tasks so that POEM's time-savings calculations reflect my real workflow rather than generic benchmarks.

- As a team lead, I want an activity dashboard showing flywheel cycle times, approval rates, and agent usage across my team, so I can identify bottlenecks and measure ROI.

- As an admin, I want an append-only audit trail of all system events, so I can review what actions were taken, when, and by whom.

---

## 3. Setting Core Metrics

### How will you know the problem is solved?

**North Star Metric:** Full flywheel cycle time — the elapsed time from product idea input to market feedback synthesis and next iteration proposal. This measures the velocity of the complete loop, which is POEM's core differentiator.

| Metric Type | Metric | Target | How It's Tracked |
|-------------|--------|--------|------------------|
| North Star | Full flywheel cycle time (idea → feedback → next iteration) | Complete cycle in <1 week (vs. 4-6 weeks manual) | EventBus captures timestamps at each orchestrator state transition; cycle time = delta between "idea_submitted" and "iteration_proposed" events |
| Primary | Artifact generation accuracy (human approval rate) | >80% first-pass approval | Every approval gate decision emits an event with outcome (approved/revised/rejected); approval rate = approved / total per agent per time period |
| Primary | Context preservation score (cross-stage consistency) | >90% key decisions traceable end-to-end | Periodic automated consistency checks compare downstream artifacts against source PRD decisions; scored as percentage of key decisions that appear in downstream outputs |
| Primary | Flywheel completion rate | >70% of projects complete at least one full loop | Orchestrator emits lifecycle state; completion rate = projects reaching "feedback_synthesized" state / total projects started |
| Secondary | User time saved per week | 10+ hours for active users | Time-savings estimation model (see below) calculates per-action savings from user-calibrated estimates; aggregated weekly per user |
| Secondary | Feedback-to-iteration latency | <48 hours from signal detection to proposal | EventBus captures "feedback_signal_detected" and "iteration_proposed" timestamps; latency = delta between these events |
| Secondary | Support signal classification accuracy | >85% correct classification | Tracked via human overrides on Support Ops Agent classifications; accuracy = 1 - override rate |
| Secondary | Cross-stage context queries (users checking "why") | Decreasing over time (indicates trust building) | UI interaction events track when users inspect reasoning traces; declining frequency signals growing trust in system outputs |

### How Metrics Are Tracked: The Telemetry Architecture

POEM's metrics are not aspirational — they are built into the system architecture. The EventBus and ActivityStore components (described in Section 2) provide the foundation for all measurement, reporting, and future auditing needs.

**Event Model**

Every trackable action in POEM emits a structured event to the EventBus:

```
{
  event_id:    "uuid",
  timestamp:   "ISO-8601",
  event_type:  "agent_action | gate_decision | state_transition | user_interaction | system_health | support_signal",
  agent:       "product | devops | engineering | marketing | feedback | support_ops | service_engineering | orchestrator",
  project_id:  "uuid",
  user_id:     "uuid",
  metadata:    { ... event-specific data }
}
```

This is a lightweight, append-only event stream. Every component emits events without knowing about storage or reporting — the EventBus handles routing to the ActivityStore, which is a set of postgres tables alongside the existing pgvector context graph.

**Key Event Types and What They Measure**

| Event Type | Emitted By | Example Events | Metrics Derived |
|------------|------------|----------------|-----------------|
| state_transition | Orchestrator | idea_submitted, prd_generated, prd_approved, tickets_generated, feedback_synthesized, iteration_proposed, idea_backlogged | Flywheel cycle time, stage durations, completion rate, backlog size |
| agent_action | All agents | artifact_generated, context_retrieved, reasoning_trace_created, question_raised_to_product | Agent usage frequency, generation time per artifact, token costs, cross-agent communication frequency |
| gate_decision | Approval Gate UI | artifact_approved, artifact_revised, artifact_rejected | Approval rate per agent, revision frequency, time-to-decide, rejection-to-backlog rate |
| user_interaction | UI / Dashboard | time_estimate_submitted, reasoning_trace_viewed, dashboard_viewed | Time-savings data, trust indicators, engagement |
| support_signal | Support Ops Agent | signal_classified_bug, signal_classified_feature_request, signal_classified_ux_confusion, classification_overridden | Classification accuracy, signal volume by type, override rate |
| system_health | All components | agent_latency, error_occurred, api_call_made | System reliability, cost tracking, performance |

### Time-Savings Estimation Model

Time saved is the hardest metric to measure credibly. POEM uses a calibrated estimation model rather than fabricated benchmarks.

**How It Works**

1. **Industry Defaults as Starting Point:** POEM ships with reasonable default estimates for each action type based on published productivity research and typical workflows. For example, "PRD generation" defaults to 4 hours manual equivalent, "engineering ticket breakdown" defaults to 2 hours, "marketing brief creation" defaults to 3 hours.

2. **User Calibration:** After a user's first few interactions with each action type, POEM prompts: *"How long would this have taken you manually?"* The user's answer replaces the default for that action type going forward. This happens naturally at approval gates — the user is already reviewing the output, so the prompt fits the workflow without adding friction.

3. **Persistent Memory:** Each user's (or team's) calibrated estimates are stored in the ActivityStore and applied automatically to future calculations. Users can revise estimates at any time via the dashboard settings.

4. **Aggregation:** Weekly and monthly time-savings reports are calculated by multiplying the number of completed actions per type by the calibrated estimate for that type. Reports are available at the individual, project, team, and organization level.

**Time-Savings Calculation**

```
Weekly time saved =
  Σ (actions_completed_by_type × calibrated_estimate_per_type)

Example:
  3 PRDs generated × 4 hrs each    = 12 hrs
  8 ticket sets created × 2 hrs    =  16 hrs
  2 marketing briefs × 3 hrs       =   6 hrs
  1 feedback synthesis × 1.5 hrs   =  1.5 hrs
  5 support signals classified × 0.5 hrs = 2.5 hrs
                                     ─────────
  Total weekly savings:              38 hrs
```

This gives POEM users defensible, personalized ROI numbers rather than marketing claims.

### Reporting Dashboard (MVP)

The MVP dashboard provides three views, all powered by queries against the ActivityStore:

**Personal View:** "You saved ~X hours this week." Shows time savings by action type, recent activity timeline, and flywheel cycles completed.

**Project View:** Displays per-project flywheel state (which stage each project is in), cycle time for completed loops vs. the user's manual baseline, and approval rates by stage.

**Team/Org View (post-MVP):** Rolls up individual metrics across team members. Identifies bottlenecks (e.g., "marketing brief approval is your slowest stage"), trends over time, and aggregate ROI.

### Metric Tracking Over Time

All metrics are designed to be compared across time periods. Because the ActivityStore is append-only with timestamps on every event, any metric can be windowed by day, week, month, or quarter. This enables:

- **Trend analysis:** "Your approval rate improved from 65% to 85% over 3 months"
- **Baseline comparison:** "Your first flywheel cycle took 9 days; your latest took 3 days"
- **ROI reporting:** "POEM has saved your team an estimated 142 hours this quarter"
- **Anomaly detection:** Sudden drops in approval rate or spikes in cycle time surface automatically

---

## 4. Prioritization

### Breaking the Agentic Workflow into Components

The POEM system consists of the following major components, designed to work together as a complete flywheel:

```
[Input Ingestion] → [Orchestrator] → [Product Agent] → [Engineering Agent] → [DevOps Agent] → [Marketing Agent] → [Feedback Agent] ─┐
                         ↑                    ↑                                                                        ↑              │
                         │                    └── questions ──────────────────┘                   [Support Ops Agent] ──┘              │
                         │                                                                       [Service Eng Agent] ──┘              │
                         └────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

All components emit to: [EventBus] → [ActivityStore] → [Reporting Dashboard]
```

### Component Risk Assessment

#### Component: Input Ingestion (Product Brief Parsing)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Product briefs are unstructured natural language with variable formats | PASS - Rule-based parsing would fail on varied inputs |
| Do you have data? | Can use public PRD examples + synthetic generation | PASS - Sufficient training data available |
| Can it scale? | LLM inference scales horizontally | PASS - No architectural blockers |
| Explainability? | Need to show what info was extracted from brief | PASS - Can output structured extraction with citations |

#### Component: PRD Generation (Product Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Requires understanding product context and generating coherent documentation | PASS - LLMs excel at structured document generation |
| Customer accuracy expectations? | PRDs require high quality - directly impacts downstream work | MEDIUM RISK - Human review required |
| How easy to judge quality? | PRD quality is subjective but can use rubrics | PASS - Structured eval criteria exist |

#### Component: Work Item Hierarchy Generation (Engineering Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Breaking PRD into structured hierarchy requires technical understanding | PASS - Requires reasoning about dependencies and scope |
| Customer accuracy expectations? | Incorrect breakdown wastes engineering cycles | MEDIUM RISK - Human review at Gate 2 required |
| What laws apply? | No specific regulations for internal ticketing | PASS - Low regulatory risk |
| Bias concerns? | Could over/under-estimate complexity for certain tech stacks | LOW RISK - Human review mitigates |
| Cross-agent communication? | Must be able to raise questions back to Product Agent | MEDIUM RISK - Requires question-routing logic |

#### Component: DevOps Spec Generation (DevOps Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Translating engineering plans to infrastructure needs requires reasoning | PASS - Not a simple template-fill task |
| Technical accuracy? | Incorrect DevOps specs could cause deployment failures | MEDIUM RISK - Requires ops-savvy human review |
| Dependency on Engineering output? | Must work downstream of Engineering Agent, not in parallel | PASS - Sequential flow ensures correct inputs |
| Integration complexity? | May need to query existing infrastructure state | MEDIUM RISK - API integrations required |

#### Component: Marketing Brief Generation (Marketing Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Requires translating technical features to customer benefits | PASS - LLMs strong at audience adaptation |
| Accuracy concerns? | Marketing claims must match product capabilities | MEDIUM RISK - Human review prevents overclaiming |
| Brand consistency? | Must match company voice/style | LOW RISK - Can be configured with brand guidelines |

#### Component: Feedback Synthesis (Feedback Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Synthesizing diverse feedback signals (market + support) requires reasoning | PASS - Not rule-based aggregation |
| Data availability? | Requires access to analytics, CRM, support signals | MEDIUM RISK - Integration complexity |
| Signal vs. noise? | Must distinguish meaningful feedback from noise | MEDIUM RISK - Threshold tuning required |
| Closing the loop? | Must connect feedback to original requirements | CRITICAL - Core differentiator |

#### Component: Support Signal Classification (Support Ops Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Distinguishing bugs vs feature requests vs UX confusion requires contextual understanding | PASS - Rule-based triage fails on ambiguous reports |
| Accuracy requirements? | Misclassification wastes team time (bug sent to Product, feature request sent to Engineering) | MEDIUM RISK - Must track classification accuracy and allow human overrides |
| Data availability? | Requires integration with support/help desk systems | MEDIUM RISK - Integration with Zendesk, Intercom, etc. |
| Volume handling? | High-volume support channels could overwhelm the agent | LOW RISK - LLM inference scales; batching possible |

#### Component: Technical Investigation (Service Engineering Agent)

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Root cause analysis and bug reproduction require technical reasoning | PASS - Cannot be rule-based |
| Accuracy requirements? | Incorrect root cause wastes Engineering time | MEDIUM RISK - Human verification before escalation |
| Scope creep risk? | Could attempt to fix bugs rather than just investigate | LOW RISK - Clear role boundary: investigate and report, don't fix |

#### Component: Orchestrator

| Check | Why | Result |
|-------|-----|--------|
| Is ML necessary? | Routing logic could be deterministic, but context management requires reasoning | PASS - Context graph management needs ML |
| Complexity? | Coordinating 8 agents + human gates + backlog + state management | MEDIUM RISK - Careful architecture required |
| Failure modes? | Must handle partial failures gracefully | MEDIUM RISK - Need robust error handling |

### Overall Component Risk Summary

| Component | Risk Level | Comment |
|-----------|------------|---------|
| Input Ingestion | Low | Standard NLP task, well-understood |
| Product Agent (PRD Gen) | Medium | Quality variance - requires human review gate |
| Engineering Agent (Work Items) | Medium | Complexity estimation is imperfect; question-routing adds complexity |
| DevOps Agent (Infra Specs) | Medium | Technical accuracy critical; sequential dependency on Engineering |
| Marketing Agent (Brief) | Low | LLMs strong at marketing copy; context from PRD helps |
| Feedback Agent (Synthesis) | Medium-High | Integration complexity + multi-channel signal detection; core differentiator |
| Support Ops Agent | Medium | Classification accuracy critical; needs human override mechanism |
| Service Engineering Agent | Medium | Technical investigation depth is hard to scope; clear boundaries needed |
| Orchestrator | Medium | Routing is mostly deterministic; backlog management and gate configuration add complexity |
| EventBus + ActivityStore | Low | Standard telemetry pattern; postgres tables; no ML required |
| Reporting Dashboard | Low | Read-only queries against ActivityStore; standard UI work |
| Approval Gate Engine | Medium | Configurable role-based policies add design complexity beyond simple approve/reject |

### MVP Scope: Full Loop, Shallow Depth

The MVP will demonstrate the **complete flywheel** with intentionally shallow depth at each stage. This approach:

- **Validates the core hypothesis:** That cross-stage context preservation creates compounding value
- **Demonstrates the differentiator:** The closed feedback loop is what makes POEM unique
- **Allows rapid iteration:** Shallow implementations can be deepened based on user feedback

**MVP Implementation:**

- All core agents operational with basic capabilities (Product, Engineering, DevOps, Marketing, Feedback)
- Support Ops Agent with basic classification (bug/feature request/UX confusion)
- Service Engineering Agent with basic investigation prompts
- Sequential Engineering → DevOps flow with question-routing back to Product
- Approval gates with named stages (Intake, Technical Review, GTM Review, Iteration Review)
- Default single-decider approval policy (solo founder configuration)
- Rejection → backlog with rationale
- Work item hierarchy with configurable depth (default: Ideas → Stories → Tasks for MVP)
- Single integration per external tool category (e.g., one project management tool, one analytics source)
- Context graph storing key decisions and reasoning (pgvector as default vector DB)
- One complete flywheel cycle demonstrable end-to-end
- Self-hostable via Docker (Dockerfile + docker-compose.yaml)
- Provider abstractions in place (LLM, vector DB, integrations) for future extensibility
- EventBus capturing events from all components
- ActivityStore with postgres schema for event log and time-savings estimates
- Basic reporting dashboard (personal view with time saved, project view with cycle times and approval rates)
- Time-savings estimation with industry defaults and user calibration prompts at approval gates

**Post-MVP Deepening:**

- Multi-approver gate configurations (majority, unanimous policies)
- No-vote timeout and auto-escalation
- Per-project and per-feature gate configuration
- Full work item hierarchy with epic support
- Richer artifact generation (more detailed PRDs, more granular work items)
- Additional integrations per category (including support desk systems)
- Advanced feedback signal detection
- Support Ops Agent integration with Zendesk, Intercom, etc.
- Automated threshold tuning
- Additional LLM and vector DB providers (GPT-4o, Qdrant, Pinecone)

---

## 5. Roadmap

| Release | Features | Duration |
|---------|----------|----------|
| Phase 0 (Foundation) | Open source repo setup (AGPL + commercial license files), portability architecture (provider abstractions, config schema, prompt externalization), Dockerfile + docker-compose, instance separation pattern | Pre-Week 1 (personal time) |
| MVP | All 8 agents with basic capabilities, Orchestrator routing with backlog management, Named approval gates (Intake/Technical/GTM/Iteration) with single-decider default, Sequential Engineering → DevOps flow with question-routing, Work item hierarchy (configurable depth), Support Ops classification (bug/feature/UX confusion), Basic context graph (pgvector), Single integration per tool category, Self-hosting support, EventBus + ActivityStore, Time-savings estimation, Basic reporting dashboard | Week 1-3 |
| MVP+1 | Multi-approver gate configurations, No-vote timeout and auto-escalation, Per-project gate configuration, Full work item hierarchy (themes → epics → stories → tasks), Deeper PRD generation, Reasoning traces visible in UI, Feedback Agent signal detection tuning, Support desk integrations (Zendesk/Intercom), Additional provider implementations (GPT-4o, Qdrant), Team/org reporting rollup, Anomaly detection on metrics | Week 4-5 |
| Launch | Full flywheel demo (idea → feedback → iteration), Context graph visualization, Multi-project support, Documentation and onboarding, Licensing guide for companies, Per-feature gate configuration for larger teams | Week 6 |
| Iteration | Additional integrations (GitHub, Jira, HubSpot, etc.), Advanced analytics in Feedback Agent, Team collaboration features, API access, Commercial infrastructure (Stripe, license keys), Monitoring service, Audit trail export | Post-cohort |

---

## 6. Evaluations

### Evaluation Strategy

Ground truth will be established using expert-created PRDs, work items, DevOps specs, and marketing briefs as reference standards. Evaluation will measure both component-level quality and end-to-end flywheel coherence.

**Key Evaluation Dimensions:**

- Individual artifact quality (per agent)
- Cross-stage consistency (does the marketing brief reflect the PRD decisions?)
- Flywheel integrity (does feedback correctly trace to original requirements?)
- Context preservation (can we answer "why was this decision made?" at any point?)
- Support signal classification accuracy (are bugs, feature requests, and UX confusion correctly identified?)
- Approval gate effectiveness (do configurable policies produce appropriate outcomes?)

### HHH Framework Evaluation

| Component | Helpful | Honest | Harmless |
|-----------|---------|--------|----------|
| PRD Generation | Completeness score (all sections present), Actionability rating | No hallucinated features, Accurate reflection of input brief | No discriminatory assumptions, Safe technical recommendations |
| Work Item Generation | Coverage (all requirements mapped), Appropriate hierarchy depth, Clear acceptance criteria | Realistic complexity estimates, Dependencies correctly identified | No security anti-patterns, No harmful code suggestions |
| DevOps Spec Generation | Deployment-ready specs, Infrastructure appropriateness | Realistic resource estimates, Dependencies correctly identified | No security anti-patterns, Safe default configurations |
| Marketing Brief | Messaging clarity, Target audience fit | Claims match product capabilities, No exaggeration | No manipulative language, Compliant with ad standards |
| Feedback Synthesis | Actionable insights, Relevant signal detection across all channels | Accurate representation of feedback, No cherry-picking | No bias amplification, Fair representation of user segments |
| Support Classification | Correct categorization rate, Appropriate routing | Transparent classification reasoning, No suppression of negative signals | No bias in bug vs UX confusion classification, Fair treatment of all user segments |
| Service Engineering | Accurate root cause identification, Useful reproduction steps | Honest assessment of bug severity, No minimization of issues | No security information exposure in investigation reports |

### Prompt Strategy

POEM will employ the following prompting techniques:

**Chain-of-Thought (CoT):** For complex reasoning tasks like work item breakdown, complexity estimation, feedback synthesis, and support signal classification.

**Few-Shot Examples:** Include 2-3 examples of high-quality outputs in prompts for each agent. All prompts are stored as external text files in `/prompts/defaults/` organized by agent, making them easy to iterate, version control, and customize per deployment.

**Structured Output Constraints:** JSON schema enforcement for consistent artifact structure.

**Context Injection:** Retrieved context from lifecycle graph injected into each agent prompt.

**Cross-Agent Handoff Prompts:** Specialized prompts for stage transitions that emphasize context preservation.

**Classification Prompts:** Specialized prompts for the Support Ops Agent that distinguish bug reports from feature requests from UX confusion, with examples of each category and edge cases.

### Launch Criteria

| Launch Phase | Helpful | Honest | Harmless | Gate |
|--------------|---------|--------|----------|------|
| Measurement (1-2%) | >60% approval | >80% accuracy | 0 critical issues | Internal only |
| Beta (2-10%) | >75% approval | >85% accuracy | 0 critical issues | Invited users |
| Launch | >80% approval | >90% accuracy | 0 critical issues | Public access |

**Additional Launch Gates:**

- At least 3 complete flywheel cycles demonstrated with real users before public launch
- Support signal classification accuracy >85% (measured against human-classified test set)
- Approval gate configuration tested across at least 2 org-size configurations

---

## 7. Responsible AI Risks & Mitigation

### Accountability

| Question | Response |
|----------|----------|
| Efficacy and limitations? | POEM generates draft artifacts that require human approval. Not designed for autonomous decision-making. Quality depends on input brief quality. Full flywheel requires user engagement at each gate. Support signal classification may misroute issues — human override always available. |
| Sensitive data policies? | Product briefs may contain confidential business info. Support tickets may contain customer PII. Data stored encrypted, not used for training. SOC2 compliance planned for post-launch. Self-hosting option gives users full data control. The instance separation pattern ensures company-specific data never touches the open source core. |
| Human oversight? | Mandatory approval gates at each stage transition. No artifact proceeds without explicit human confirmation. Flywheel pauses at each gate until human approves. Support signal classifications can be overridden by humans at any time. |

### Transparency

| Question | Response |
|----------|----------|
| Direct and indirect use cases? | Direct: Draft document generation across product lifecycle; support signal triage. Indirect: Could be used to inflate PM headcount metrics if presented as human work (mitigated by watermarking). |
| How results are generated? | Each artifact includes reasoning traces showing what context influenced generation. Support classifications include explanation of why the signal was categorized a specific way. Users can inspect provenance at any point in the flywheel. Core engine is open source (AGPL-3.0) so the system's behavior is fully auditable. |
| Required disclosures? | AI-generated content will be marked. Users informed that outputs are drafts requiring review. Flywheel state visible at all times. Open source license and commercial terms clearly documented in the repository. |

### Fairness

| Question | Response |
|----------|----------|
| Underrepresented groups? | Non-English product briefs may receive lower quality outputs initially. Roadmap includes multilingual support. Hardware/IoT products may get less relevant work items. B2C vs B2B bias possible in marketing briefs. Support signal classification may be biased toward common issue patterns, potentially underweighting edge-case user segments. |
| Feedback loops for fairness? | User feedback on artifact quality tracked by product category, company size, and industry. Quarterly bias audits planned. Feedback Agent specifically monitored for segment bias. Support Ops classification accuracy tracked per user segment. |

### Reliability and Safety

| Question | Response |
|----------|----------|
| Acceptable error rates? | <20% major revision rate on first-pass artifacts. <15% misclassification rate on support signals. Human approval gate catches errors before downstream impact. Flywheel designed to be resilient to single-stage failures. |
| What can go wrong with input data? | Malicious prompts, proprietary competitor info, feedback manipulation, support ticket spam. Input validation and content filtering will be implemented. Support channel integration includes rate limiting. |
| Recovery plan? | All artifacts are drafts until approved. System can be disabled without data loss. Rollback to previous versions supported. Flywheel state is persistent and resumable. Self-hosted deployments can be backed up and restored independently. Misclassified support signals can be reclassified and rerouted. |
| System health monitoring? | Latency, error rates, approval rates monitored per agent. Alerts for quality degradation. Flywheel completion rate tracked. Support classification accuracy monitored. User communication via in-app notifications. Docker health check endpoints enable container orchestration monitoring. |

---

## 8. Pricing & Licensing

### Licensing Model: AGPL-3.0 + Commercial Dual License

POEM uses a dual licensing model that balances open source community access with commercial sustainability:

**AGPL-3.0 (Default — Free):** The core engine is licensed under the GNU Affero General Public License v3.0. This means individuals, small teams, and anyone willing to open source their customizations can use POEM at no cost. The AGPL's copyleft provision ensures that modifications to the core engine shared as a service must also be open sourced.

**Commercial License (Paid):** For organizations that need proprietary customizations, want to deploy POEM as a SaaS product, or require enterprise support and SLAs, a commercial license is available. This removes the AGPL's copyleft obligations.

**Why dual licensing works for POEM:**

- AGPL is OSI-approved "real" open source — the community can freely use, modify, and contribute
- Enterprise legal teams typically require non-copyleft licensing, creating natural demand for commercial licenses
- As sole author, full rights are retained to offer both licensing paths
- The Contributor License Agreement (CLA) ensures contributions can be included in both versions

**License Decision Tree:**

- Individual or small team, personal/internal use → AGPL is fine, free to use
- Company using internally, willing to AGPL their modifications → AGPL is fine, free to use
- Company wanting proprietary customizations → Needs Commercial License
- Anyone offering POEM as a hosted service (SaaS) → Needs Commercial License
- Enterprise wanting support/SLAs → Needs Commercial License

For licensing inquiries: poem.pdm@gmail.com

### Costs & Accuracy Tradeoffs

| # | Item | What We Used | Why We Chose This | Trade-Offs |
|---|------|--------------|-------------------|------------|
| 1 | Framework | LangChain + LangGraph | Required for multi-agent orchestration and flywheel state management | More complex than single-agent but necessary for architecture |
| 2 | LLM for Inference | Claude 3.5 Sonnet (primary), GPT-4o (fallback) | Better reasoning for complex cross-stage tasks | Higher cost per token but better output quality |
| 3 | Vector Database | pgvector (PostgreSQL) | Free, self-hostable, portable, eliminates managed service dependency | Less feature-rich than Pinecone but sufficient for MVP; Pinecone/Qdrant available as optional extras |
| 4 | User Interface | React + Tailwind | Standard choice, no significant trade-offs | N/A |
| 5 | Integrations | REST APIs for external tools | Maintenance overhead but necessary for flywheel completeness | Each integration adds maintenance burden |
| 6 | Containerization | Docker + docker-compose | Enables self-hosting on minimal infrastructure | Adds operational complexity for non-Docker users |

### Development Costs (MVP — Solo Developer)

| Item | Estimated Cost |
|------|----------------|
| Anthropic API (Claude 3.5 Sonnet) — Development | $200/month |
| OpenAI API (GPT-4o) — Fallback/Comparison | $100/month |
| pgvector (self-hosted via Docker) | $0 (included in hosting) |
| Vercel Hosting (Pro) — UI | $20/month |
| VPS for POEM core + pgvector (DigitalOcean/Hetzner) | $5-20/month |
| GitHub (personal) | $0 |
| Analytics Tool API (for Feedback Agent) | $50/month |
| Domain + DNS | $12/year |
| **Total (Solo Developer)** | **~$380-400/month** |

### Resource (Manpower Cost — Post-MVP)

| Role | Estimated Cost |
|------|----------------|
| DevOps Engineer (part-time/contract) | $5,000/month |
| Frontend Engineer | $8,000/month |
| Backend Engineer (x2) | $16,000/month |
| **Total** | **~$29,000/month** |

### Operational Costs (Post-Launch)

Ongoing costs scale with user count and flywheel cycle volume. Primary cost drivers are LLM API calls (per-token pricing), vector DB storage (scales with context graph size), and hosting infrastructure. Self-hosting users absorb their own infrastructure costs, reducing POEM's operational burden for the AGPL tier.

### Market Size

**TAM (Total Addressable Market):** $6.68B — Global project management software market (2024)

**SAM (Serviceable Addressable Market):** $1.2B — AI-augmented product management tools segment

**SOM (Serviceable Obtainable Market):** $50M — Solo founders and early-stage startup PMs (initial target)

### Revenue Potential & Pricing

**Pricing Model:** Dual license tiers (annual subscription for commercial licenses)

**Rationale:** The AGPL open source tier drives adoption and community contributions. Commercial licenses provide revenue from organizations that need proprietary rights, SaaS deployment permissions, or enterprise support. Annual pricing aligns with enterprise procurement cycles and provides predictable revenue.

| Tier | Price | Target | Includes |
|------|-------|--------|----------|
| Indie (AGPL) | Free | Individuals, small startups | Full functionality, community support, must comply with AGPL |
| Team | $500/year | Startups (5-20 employees) | Commercial license, email support, proprietary customization rights |
| Business | $2,000/year | Companies (20-100 employees) | Commercial license, priority support, dedicated onboarding |
| Enterprise | Custom pricing | 100+ employees or SaaS providers | Custom terms, SLA, dedicated support, custom integrations |

**Revenue Scenarios (Year 1 Post-Launch):**

| Scenario | Team Licenses | Business Licenses | Enterprise | Annual Revenue |
|----------|---------------|-------------------|------------|----------------|
| Conservative | 20 | 5 | 0 | $20,000 |
| Moderate | 50 | 15 | 2 | $85,000+ |
| Optimistic | 100 | 30 | 5 | $160,000+ |

---

## Appendix A: Why Full Flywheel for MVP

The decision to implement the complete flywheel (shallow) rather than a partial loop (deep) is intentional:

1. **The loop IS the product.** POEM's differentiation is the closed feedback loop. A partial implementation doesn't demonstrate the core value proposition.

2. **User validation requires completeness.** Users can only evaluate whether the flywheel creates value if they experience a complete cycle.

3. **Context preservation needs full path.** The context graph's value compounds across stages. Testing only a subset of agents doesn't validate the architecture.

4. **Shallow is iterable.** Starting shallow across all stages allows user feedback to guide where to deepen first.

5. **Personal utility.** This tool is being built to be genuinely useful for the creator's own product development workflow, which requires the full loop.

## Appendix B: Key Project Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-28 | Renamed Operations Agent → DevOps Agent | "Operations" was ambiguous; "DevOps" clarifies the agent owns infrastructure/deployment, not architecture decisions; "Platform Agent" rejected because it implies architecture ownership |
| 2026-02-28 | Added Support Operations Agent + Service Engineering Agent | Support signals (bugs, feature requests, UX confusion) are a critical feedback channel that was missing; keeping under "Operations" in POEM acronym preserves naming while expanding operational scope |
| 2026-02-28 | Named approval gates: Intake, Technical Review, GTM Review, Iteration Review | Named gates are clearer than numbered gates; each has a distinct purpose and question it answers |
| 2026-02-28 | Configurable approver roles per gate with policy options | Different org structures need different approval patterns; solo founders need simplicity, larger teams need consensus mechanisms; policies (unanimous/majority/single-decider) cover the spectrum |
| 2026-02-28 | Rejection → prioritized backlog (not archive) | Rejected ideas aren't dead — they're "not now"; preserving rejection rationale enables resurfacing when conditions change |
| 2026-02-28 | Engineering → DevOps sequential (not parallel) | DevOps specs depend on engineering approach; parallel execution leads to misaligned infrastructure decisions |
| 2026-02-28 | Engineering/DevOps can raise questions back to Product | Without feedback loops, ambiguous requirements waste cycles; agents need a way to flag infeasibility or request clarification |
| 2026-02-28 | Work item hierarchy: Ideas → Epics → Stories → Tasks (configurable) | Flat tickets miss important structure; hierarchy follows industry best practices while configurability accommodates different team workflows |
| 2026-02-28 | Support signal classification: bug / feature request / UX confusion | Three distinct categories ensure signals reach the right team; UX confusion is the most valuable category because it's typically lost in traditional support workflows |
| 2026-02-28 | EventBus + ActivityStore as separate component (not Orchestrator sub-module) | UI and agents all emit events; Orchestrator shouldn't own UI-originated telemetry; separate component scales independently and supports future monitoring/auditing services |
| 2026-02-28 | Time-savings model: industry defaults + user calibration | Pure user-provided estimates add friction; pure defaults lack credibility; hybrid approach provides useful numbers from day one that become personalized over time |
| 2026-02-28 | GitHub repo created: sreynolds100/poem-core | Establishing IP ownership with timestamp |
| 2026-02-28 | Dedicated project email: poem.pdm@gmail.com | Separates personal from project communications across all license files and docs |
| 2026-02-28 | Full AGPL-3.0 text in LICENSE file | Custom header alone is insufficient for legal enforceability |
| 2026-02-28 | pyproject.toml with optional dependency groups | `pip install poem-core[pinecone]` pattern keeps base install lean |
| 2026-02-28 | CLA bot configured via CLA Assistant | Automated CLA signing for PRs; linked to CLA gist |
| 2026-02-27 | Full flywheel for MVP (shallow depth) | Core differentiator is the closed loop; partial implementation doesn't validate hypothesis |
| 2026-02-27 | Open source core + instance separation | Protect IP, enable portability across jobs/companies |
| 2026-02-27 | AGPL + Commercial dual licensing | Enables revenue while staying open source; AGPL triggers enterprise license purchases |
| 2026-02-27 | pgvector as default vector DB | Free, self-hostable, portable, sufficient for MVP |
| 2026-02-27 | Prompts externalized to files | Portability, version control, easy customization per deployment |
| 2026-02-27 | Markdown format for all docs | Easier iteration and version control |

---

## Appendix C: Open Design Discussions

These items require further design work before implementation. They are tracked in the project tracker with dedicated discussion tasks.

| ID | Topic | Key Questions | Status |
|----|-------|--------------|--------|
| D1 | Approval Gate Configuration Schema | What does the config.yaml schema look like for gate policies? How do we handle role definitions that vary across orgs? Should roles be free-text or predefined? | Open |
| D2 | Work Item Hierarchy Customization | How do teams configure which hierarchy levels to use? Should the Engineering Agent detect appropriate depth automatically based on PRD complexity? How do we handle cross-epic dependencies? | Open |
| D3 | Support Ops Integration Architecture | Which support desk systems to integrate first? How do we handle high-volume ticket streams without overwhelming the classification agent? What's the right batching strategy? | Open |
| D4 | Service Engineering Agent Scope Boundaries | How do we prevent the Service Engineering Agent from attempting to fix bugs rather than just investigate? What's the handoff protocol to Engineering Agent? | Open |
| D5 | Cross-Agent Question Protocol | When Engineering or DevOps raises a question to Product, what's the UX? Does the flywheel pause? Can multiple questions be batched? How does this interact with approval gates? | Open |

---

*End of PRD Document — Version 1.3*
*GitHub: [sreynolds100/poem-core](https://github.com/sreynolds100/poem-core) | Contact: poem.pdm@gmail.com*
