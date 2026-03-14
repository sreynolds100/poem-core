# POEM User Flow Diagrams

**For PRD Section 2: Solution Definition**  
**Version:** 2.1 (aligned with PRD v1.3)  
**Date:** February 2026

---

## 1. Primary Flow: Full Flywheel (Idea → Launch → Iteration)

```mermaid
flowchart TD
    A([👤 User Inputs Product Brief]) --> B[Product Agent]
    B --> B1[Generate PRD + User Stories\n+ Acceptance Criteria]
    B1 --> B2[Attach Reasoning Trace]
    B2 --> G1{🔒 Gate 1: Intake\n'Should we pursue this idea?'}

    G1 -->|✅ Approve| C[Engineering Agent]
    G1 -->|✏️ Revise| B1
    G1 -->|❌ Reject| BL([📋 Prioritized Backlog\nRejection rationale attached\nSubmitter notified])

    C --> C1[Break PRD into Work Item Hierarchy\nEpics → Stories → Tasks]
    C1 --> C2[Estimate Complexity\n+ Map Dependencies]
    C2 --> CQ{Requirements\nclear?}
    CQ -->|Yes| C3[Attach Reasoning Trace]
    CQ -->|❓ Ambiguous| CQ1[Raise Question\nto Product Agent]
    CQ1 --> CQ2([👤 User Answers])
    CQ2 --> C1

    C3 --> D[DevOps Agent\n— sequential after Engineering]
    D --> D1[Generate Deployment Specs\n+ Infrastructure Requirements\n+ CI/CD Config]
    D1 --> DQ{Specs align with\nengineering plan?}
    DQ -->|Yes| D2[Attach Reasoning Trace]
    DQ -->|❓ Conflict| DQ1[Raise Question to\nProduct or Engineering]
    DQ1 --> DQ2([👤 User Answers])
    DQ2 --> D1

    D2 --> G2{🔒 Gate 2: Technical Review\n'Is the plan sound and viable?'}

    G2 -->|✅ Approve| F[Marketing Agent]
    G2 -->|✏️ Revise Engineering| C1
    G2 -->|✏️ Revise DevOps| D1
    G2 -->|❌ Reject| BL

    F --> F1[Generate Launch Brief\n+ Positioning + Messaging\n+ Target Audience]
    F1 --> F2[Attach Reasoning Trace]
    F2 --> G3{🔒 Gate 3: GTM Review\n'Is the launch plan aligned\nwith the product?'}

    G3 -->|✅ Approve| H([🚀 Product Launches])
    G3 -->|✏️ Revise| F1
    G3 -->|❌ Reject| BL

    H --> I[Feedback Agent]
    I --> I1[Monitor Market Analytics\n+ User Feedback\n+ Support Ops Signals]
    I1 --> I2[Synthesize Insights\n+ Link to Original PRD]
    I2 --> I3[Generate Iteration Proposal]
    I3 --> G4{🔒 Gate 4: Iteration Review\n'Does this warrant\na new cycle?'}

    G4 -->|✅ Approve| A
    G4 -->|✏️ Revise| I2
    G4 -->|⏸️ No Action| W([⏸️ Continue Monitoring])

    style A fill:#4A90D9,color:#fff
    style H fill:#4AD97A,color:#fff
    style BL fill:#E8943A,color:#fff
    style W fill:#888,color:#fff
    style G1 fill:#F5A623,color:#fff
    style G2 fill:#F5A623,color:#fff
    style G3 fill:#F5A623,color:#fff
    style G4 fill:#F5A623,color:#fff
```

---

## 2. Context Flow: What Gets Stored and Retrieved

```mermaid
flowchart LR
    subgraph Context Graph — pgvector
        CG[(Lifecycle\nContext Graph)]
    end

    PA[Product Agent] -->|WRITE: PRD decisions,\nuser stories, rationale| CG
    EA[Engineering Agent] -->|WRITE: work items,\ncomplexity estimates,\ndependencies| CG
    DA[DevOps Agent] -->|WRITE: infra specs,\ndeployment decisions| CG
    MA[Marketing Agent] -->|WRITE: positioning,\nmessaging decisions| CG
    FA[Feedback Agent] -->|WRITE: insights,\nsignal interpretations| CG
    SO[Support Ops Agent] -->|WRITE: classified signals,\npattern data| CG
    SE[Service Eng Agent] -->|WRITE: root cause\nanalysis, repro steps| CG

    CG -->|READ: PRD context| EA
    CG -->|READ: PRD + engineering plan| DA
    CG -->|READ: all upstream context| MA
    CG -->|READ: full lifecycle context\n+ support signals| FA
    CG -->|READ: feedback + original PRD| PA
    CG -->|READ: product context\nfor classification| SO
    CG -->|READ: engineering context\nfor investigation| SE

    style CG fill:#7B68EE,color:#fff
```

---

## 3. Telemetry Flow: EventBus + ActivityStore

```mermaid
flowchart TD
    subgraph Emitters
        OR[Orchestrator\nstate_transition events]
        AG[All 8 Agents\nagent_action events]
        GT[Approval Gates\ngate_decision events]
        UI[UI / Dashboard\nuser_interaction events]
        SO[Support Ops Agent\nsupport_signal events]
        SY[All Components\nsystem_health events]
    end

    OR --> EB[EventBus]
    AG --> EB
    GT --> EB
    UI --> EB
    SO --> EB
    SY --> EB

    EB --> AS[(ActivityStore\nPostgres — append-only)]

    AS --> D1[Personal Dashboard\ntime saved, activity]
    AS --> D2[Project Dashboard\ncycle times, approval rates]
    AS --> D3[Team Dashboard\nrollups, bottlenecks]

    subgraph Time-Savings Model
        TS1[Industry Defaults] --> TSC[Calibrated Estimates]
        TS2[User Input at\nApproval Gates] --> TSC
        TSC --> D1
    end

    style EB fill:#F5A623,color:#fff
    style AS fill:#7B68EE,color:#fff
```

---

## 4. Secondary Flow: Feedback-Triggered Iteration

```mermaid
flowchart TD
    A([📊 Feedback Signal Detected\nMarket data, analytics,\nor support patterns]) --> B[Feedback Agent]
    B --> B1[Retrieve Original PRD Context\nfrom Lifecycle Graph]
    B1 --> B2[Synthesize Findings\nacross all channels]
    B2 --> B3[Generate Iteration Proposal]
    B3 --> B4[Attach Reasoning Trace\nlinks to source feedback\n+ original PRD decisions]
    B4 --> C{🔒 Gate 4: Iteration Review}

    C -->|✅ Approve| D[Product Agent]
    C -->|✏️ Revise| B2
    C -->|⏸️ No Action| E([⏸️ Archive Insight\nContinue Monitoring])

    D --> D1[Generate Updated PRD\nor New Feature Brief]
    D1 --> D2{🔒 Gate 1: Intake}

    D2 -->|✅ Approve| F[Engineering Agent → DevOps Agent\n→ Marketing Agent]
    D2 -->|✏️ Revise| D1
    D2 -->|❌ Reject| BL([📋 Prioritized Backlog])

    F --> G[Full Flywheel Continues\nsee Primary Flow]

    style A fill:#4AD97A,color:#fff
    style E fill:#888,color:#fff
    style BL fill:#E8943A,color:#fff
    style C fill:#F5A623,color:#fff
    style D2 fill:#F5A623,color:#fff
```

---

## 5. Tertiary Flow: Support Operations Signal Processing

```mermaid
flowchart TD
    A([📨 Support Ticket / Bug Report\n/ Customer Complaint]) --> B[Support Ops Agent]
    B --> B1[Classify Signal]

    B1 --> C{Classification}

    C -->|🐛 Bug| D[Service Engineering Agent]
    D --> D1[Investigate + Reproduce]
    D1 --> D2[Root Cause Analysis\n+ Severity Assessment]
    D2 --> D3{Confirmed Bug?}
    D3 -->|Yes| D4[Route to Engineering Agent\nwith repro steps + root cause]
    D3 -->|No — actually UX confusion| E1

    C -->|💡 Feature Request| E[Enrich with Frequency\n+ User Context]
    E --> E2[Route to Feedback Agent\nfor synthesis with\nother signals]

    C -->|😕 UX Confusion| E1[Tag with User Journey Context]
    E1 --> E1a[Route to Product Agent\nfor UX rethink]
    E1 --> E1b[Route to Engineering Agent\nfor implementation assessment]

    D4 --> FA[Feedback Agent\nPattern Detection]
    E2 --> FA
    E1a --> FA
    E1b --> FA

    FA --> FA1[Aggregate patterns:\n'20 users hit same\nUX confusion this week']
    FA1 --> FA2[Feed into Iteration Proposal\nat Gate 4]

    subgraph Human Override — Available at Any Point
        HO([👤 Reclassify Signal])
    end
    B1 -.->|Override| HO
    HO -.->|Corrected classification| C

    style A fill:#4A90D9,color:#fff
    style D4 fill:#D94A4A,color:#fff
    style E2 fill:#4AD97A,color:#fff
    style E1a fill:#F5A623,color:#fff
    style E1b fill:#F5A623,color:#fff
```

---

## 6. Orchestrator State Machine

```mermaid
stateDiagram-v2
    [*] --> idea_submitted

    idea_submitted --> prd_generating : Product Agent starts
    prd_generating --> intake_pending : PRD ready for Gate 1

    state gate1 <<choice>>
    intake_pending --> gate1 : Gate 1 — Intake
    gate1 --> prd_generating : Revise
    gate1 --> backlogged : Reject
    gate1 --> engineering_generating : Approve

    engineering_generating --> question_pending_product : Engineering raises question
    question_pending_product --> engineering_generating : User answers
    engineering_generating --> devops_generating : Work items complete → DevOps starts

    devops_generating --> question_pending_upstream : DevOps raises question
    question_pending_upstream --> devops_generating : User answers
    devops_generating --> technical_review_pending : DevOps specs ready for Gate 2

    state gate2 <<choice>>
    technical_review_pending --> gate2 : Gate 2 — Technical Review
    gate2 --> engineering_generating : Revise engineering
    gate2 --> devops_generating : Revise DevOps
    gate2 --> backlogged : Reject
    gate2 --> marketing_generating : Approve

    marketing_generating --> gtm_review_pending : Brief ready for Gate 3

    state gate3 <<choice>>
    gtm_review_pending --> gate3 : Gate 3 — GTM Review
    gate3 --> marketing_generating : Revise
    gate3 --> backlogged : Reject
    gate3 --> launched : Approve

    launched --> feedback_monitoring : Feedback Agent active

    feedback_monitoring --> signal_detected : Signal found
    signal_detected --> iteration_proposed : Proposal generated

    state gate4 <<choice>>
    iteration_proposed --> gate4 : Gate 4 — Iteration Review
    gate4 --> feedback_monitoring : No action — continue monitoring
    gate4 --> iteration_proposed : Revise proposal
    gate4 --> idea_submitted : Approve → new cycle

    backlogged --> idea_submitted : Resurfaced from backlog
    backlogged --> [*] : Remains in backlog
```

---

## 7. Approval Gate Detail

```mermaid
flowchart TD
    A[Agent Generates Artifact] --> B[Artifact + Reasoning Trace\nPresented to Configured Approvers]

    B --> P{Approval Policy}
    P -->|Single-Decider| SD[One role decides\nothers advisory]
    P -->|Majority| MJ[>50% of required\napprovers must approve]
    P -->|Unanimous| UN[All required\napprovers must approve]

    SD --> C{Decision}
    MJ --> C
    UN --> C

    C -->|✅ Approve| D[Artifact Finalized]
    D --> D1[Stored in Context Graph]
    D1 --> D2[gate_decision event emitted\n— approved]
    D2 --> D3[Time-savings calibration:\n'How long would this\nhave taken manually?']
    D3 --> D4[Next Stage Triggered]

    C -->|✏️ Revise| E[Approver Provides\nSpecific Feedback]
    E --> E1[gate_decision event emitted\n— revised]
    E1 --> F[Originating Agent\nRe-generates with\nRevision Context]
    F --> B

    C -->|❌ Reject| G[Idea → Prioritized Backlog]
    G --> G1[Rejection rationale\nattached to idea]
    G1 --> G2[gate_decision event emitted\n— rejected]
    G2 --> G3[Submitter notified\nwith explanation]

    NV([⏰ No-Vote Timeout]) -.-> NVH{No-Vote\nPolicy}
    NVH -.->|Abstain| C
    NVH -.->|Block| G
    NVH -.->|Auto-escalate| ESC([Backup Approver\nNotified])
    ESC -.-> C

    style D fill:#4AD97A,color:#fff
    style G fill:#E8943A,color:#fff
    style E fill:#F5A623,color:#fff
    style NV fill:#888,color:#fff
```

---

## 8. Work Item Hierarchy

```mermaid
flowchart TD
    subgraph Generated by Product Agent
        IDEA([💡 Idea\nOriginal product concept\nfrom user input])
    end

    subgraph Generated by Engineering Agent — depth configurable
        IDEA --> EP1[📦 Epic\nMajor feature area]
        IDEA --> EP2[📦 Epic\nMajor feature area]

        EP1 --> ST1[📝 Story\nUser-facing value increment\n'As a user, I want...']
        EP1 --> ST2[📝 Story]
        EP2 --> ST3[📝 Story]

        ST1 --> TK1[🔧 Task\nImplementable unit\n3 story points]
        ST1 --> TK2[🔧 Task\n2 story points]
        ST2 --> TK3[🔧 Task\n5 story points]
        ST3 --> TK4[🔧 Task\n1 story point]
        ST3 --> TK5[🔧 Task\n3 story points]
    end

    subgraph Configurable Depth
        M1[Minimal — solo founder\nIdea → Tasks]
        M2[Standard — small team\nIdea → Epics → Stories → Tasks]
        M3[Expanded — larger teams\nIdea → Themes → Epics → Stories → Sub-tasks]
    end

    TK1 -.->|dependency| TK3
    TK4 -.->|dependency| TK2

    style IDEA fill:#4A90D9,color:#fff
    style EP1 fill:#7B68EE,color:#fff
    style EP2 fill:#7B68EE,color:#fff
    style ST1 fill:#4AD97A,color:#fff
    style ST2 fill:#4AD97A,color:#fff
    style ST3 fill:#4AD97A,color:#fff
    style M1 fill:#eee,color:#333
    style M2 fill:#eee,color:#333
    style M3 fill:#eee,color:#333
```

---

## 9. Agent Roles & Ownership Map

```mermaid
flowchart LR
    subgraph WHAT & WHY
        PA[🎯 Product Agent\nProduct Manager\n— PRDs, user stories,\nprioritization]
    end

    subgraph HOW — Technical
        EA[⚙️ Engineering Agent\nTech Lead\n— work items, complexity,\ntechnical approach]
    end

    subgraph WHERE — Infrastructure
        DA[🚀 DevOps Agent\nDevOps Engineer\n— deploy configs, CI/CD,\ninfra specs, monitoring]
    end

    subgraph HOW — Go-to-Market
        MA[📣 Marketing Agent\nProduct Marketing Mgr\n— positioning, messaging,\nlaunch briefs]
    end

    subgraph LEARN & ITERATE
        FA[📊 Feedback Agent\nProduct Analyst\n— signal synthesis,\niteration proposals]
    end

    subgraph SUPPORT OPERATIONS
        SO[📞 Support Ops Agent\nSupport Ops Manager\n— classify & route:\nbug / feature / UX confusion]
        SE[🔍 Service Eng Agent\nSupport Engineer\n— investigate, reproduce,\nroot cause analysis]
    end

    PA -->|approved PRD| EA
    EA -->|engineering plan| DA
    PA -->|approved PRD| MA
    EA -.->|❓ question| PA
    DA -.->|❓ question| PA
    DA -.->|❓ question| EA
    SO -->|bugs + context| SE
    SE -->|enriched bugs| EA
    SO -->|feature requests| FA
    SO -->|UX confusion| PA
    SO -->|UX confusion| EA
    FA -->|iteration proposal| PA

    style PA fill:#4A90D9,color:#fff
    style EA fill:#7B68EE,color:#fff
    style DA fill:#4AD97A,color:#fff
    style MA fill:#F5A623,color:#fff
    style FA fill:#E8943A,color:#fff
    style SO fill:#D94A8A,color:#fff
    style SE fill:#D94A8A,color:#fff
```

---

*These diagrams render in any Mermaid-compatible viewer: GitHub (natively), VS Code with Mermaid extension, or [mermaid.live](https://mermaid.live) for preview.*
