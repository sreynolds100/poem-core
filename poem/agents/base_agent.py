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

"""Base agent class for all POEM stage agents."""

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """Abstract base class for POEM lifecycle agents.

    All stage agents (Product, Operations, Engineering, Marketing, Feedback)
    inherit from this class and implement the core interface.
    """

    def __init__(self, config: dict, llm_provider: Any, context_graph: Any):
        self.config = config
        self.llm = llm_provider
        self.context = context_graph

    @abstractmethod
    async def process(self, input_data: dict) -> dict:
        """Process input and generate stage-specific artifacts.

        Args:
            input_data: Stage-specific input (e.g., product brief, PRD, feedback)

        Returns:
            Generated artifacts with reasoning traces
        """
        pass

    @abstractmethod
    async def validate(self, output: dict) -> dict:
        """Validate generated output before presenting to human for approval.

        Args:
            output: The generated artifacts

        Returns:
            Validation results with any warnings or issues
        """
        pass

    @abstractmethod
    def get_reasoning_trace(self) -> dict:
        """Return the reasoning trace for the last operation.

        Returns:
            Structured reasoning showing why decisions were made
        """
        pass
