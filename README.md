# POEM: Product → Operations → Engineering → Marketing

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Commercial License](https://img.shields.io/badge/License-Commercial-green.svg)](COMMERCIAL_LICENSE.md)

**An Agentic AI System for Full Product Lifecycle Orchestration**

POEM automates the cross-functional coordination that solo founders and small teams spend 60-70% of their time on. Instead of losing context between product discovery, engineering, and go-to-market — POEM maintains a living context graph across the entire lifecycle and closes the feedback loop.

## The Flywheel

```
Idea → PRD → Ops Spec → Engineering Tickets → Marketing Brief → Launch → Feedback ─┐
 ↑                                                                                   │
 └───────────────────────────────────────────────────────────────────────────────────┘
```

Most AI tools optimize a single stage. POEM connects them all — and the feedback loop is what makes it compound.

## Key Features

- **6 Specialized Agents** — Product, Operations, Engineering, Marketing, Feedback, and an Orchestrator that coordinates them all
- **Persistent Context Graph** — Every decision, rationale, and connection is stored and accessible across stages
- **Human Approval Gates** — AI suggests, you decide. No artifact proceeds without your sign-off
- **Explainable Outputs** — Every generated artifact includes reasoning traces showing *why*
- **Provider Agnostic** — Swap LLMs (Claude, GPT, Azure) and vector DBs (pgvector, Pinecone, Qdrant) via config
- **Self-Hostable** — Run on your own infrastructure with Docker

## Quick Start

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (for self-hosting)
- An LLM API key (Anthropic or OpenAI)

### Setup

```bash
# Clone the repo
git clone https://github.com/sreynolds100/poem-core.git
cd poem-core

# Copy config template
cp config.example.yaml config.yaml

# Edit config with your API keys and preferences
# (config.yaml is gitignored — your secrets stay local)

# Run with Docker
docker compose up
```

### Configuration

All settings are externalized to `config.yaml`. See `config.example.yaml` for all available options.

## Architecture

POEM is built as a multi-agent system using LangChain + LangGraph:

```
poem-core/
├── poem/
│   ├── orchestrator/     # State machine, context graph
│   ├── agents/           # Product, Ops, Engineering, Marketing, Feedback
│   ├── providers/        # LLM and vector DB abstractions
│   └── integrations/     # External tool connectors
├── prompts/              # Externalized prompt templates
└── tests/
```

## Licensing

POEM is dual-licensed:

- **[AGPL v3](LICENSE)** — Free for individuals, small teams, and anyone willing to open source their modifications
- **[Commercial License](COMMERCIAL_LICENSE.md)** — For proprietary use, SaaS deployment, or enterprise support

See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) for details on when you need a commercial license.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first. All contributors must sign our [CLA](CLA.md) (automated via CLA Assistant on your first PR).

## Status

🚧 **Active Development** — POEM is in early development. The MVP targets demonstrating one complete flywheel cycle with shallow depth across all stages.

## Contact

- **Author:** Samantha Reynolds
- **Email:** poem.pdm@gmail.com
- **License inquiries:** See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md)
