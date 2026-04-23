"""
Base MCP Client - Abstract base class for all MCP implementations
Clarifies the MCP concept: structured interface to external APIs with encapsulated HTTP communication.
"""

from abc import ABC, abstractmethod


class MCPClient(ABC):
    """
    Abstract MCP (Model Context Protocol) Client.

    Purpose:
    - Encapsulates HTTP communication with external APIs
    - Provides a structured, typed interface for data access
    - Decouples application logic from HTTP details

    All MCP clients should inherit from this class and implement the execute method.
    """

    @abstractmethod
    async def execute(self):
        """Execute the MCP operation. Must be implemented by subclasses."""
        pass
