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

"""Abstract LLM provider interface.

All LLM providers (Anthropic, OpenAI, Azure) implement this interface
so they can be swapped via config.yaml.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate a completion from the LLM."""
        pass

    @abstractmethod
    async def generate_structured(self, prompt: str, schema: dict, **kwargs) -> dict:
        """Generate a structured (JSON) completion from the LLM."""
        pass
