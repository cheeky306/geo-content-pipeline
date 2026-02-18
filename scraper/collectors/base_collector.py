"""
Base collector abstract class.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseCollector(ABC):
    """Abstract base class for all collectors."""
    
    @abstractmethod
    def collect(self, location: str) -> Dict[str, Any]:
        """
        Collect content from a source.
        
        Args:
            location: URL or file path
            
        Returns:
            Dictionary containing:
                - content: str - The main text content
                - title: str - Title of the content
                - metadata: dict - Additional metadata
        """
        pass
    
    @abstractmethod
    def can_handle(self, location: str) -> bool:
        """
        Check if this collector can handle the given location.
        
        Args:
            location: URL or file path
            
        Returns:
            True if this collector can handle the location
        """
        pass
