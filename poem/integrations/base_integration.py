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

"""Abstract integration interface.

All external tool integrations implement this interface.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseIntegration(ABC):
    """Abstract base class for external tool integrations."""

    @abstractmethod
    async def connect(self, config: dict) -> bool:
        """Establish connection to the external tool."""
        pass

    @abstractmethod
    async def push(self, data: dict) -> dict:
        """Push data to the external tool."""
        pass

    @abstractmethod
    async def pull(self, query: dict) -> dict:
        """Pull data from the external tool."""
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the integration is healthy."""
        pass
