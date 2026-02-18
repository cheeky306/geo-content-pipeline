"""
Data models for the Knowledge Ledger Agent.
"""
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class SourceType(Enum):
    """Types of content sources."""
    BLOG = "Blog"
    RESEARCH = "Research"
    OPINION = "Opinion"
    NEWS = "News"
    DOCUMENTATION = "Documentation"
    ACADEMIC = "Academic"
    UNKNOWN = "Unknown"


@dataclass
class Source:
    """Represents a single source (URL or document)."""
    id: str  # e.g., SOURCE-001
    name: str
    source_type: SourceType
    authority_score: int  # 0-100
    location: str  # URL or file path
    content: str
    title: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    references: List[str] = field(default_factory=list)
    extracted_at: datetime = field(default_factory=datetime.now)


@dataclass
class ContentChunk:
    """Represents a chunk of processed content."""
    text: str
    heading: Optional[str] = None
    level: int = 0  # Heading level (0 = no heading)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ProcessedContent:
    """Cleaned and chunked content from a source."""
    source_id: str
    chunks: List[ContentChunk]
    cleaned_text: str
    topics: List[str] = field(default_factory=list)


@dataclass
class Topic:
    """Represents a core topic across sources."""
    name: str
    description: str
    keywords: List[str]
    source_ids: List[str]  # Which sources mention this topic
    relevance_score: float  # 0-1


@dataclass
class KnowledgeLedger:
    """Complete knowledge ledger structure."""
    sources: List[Source]
    processed_contents: List[ProcessedContent]
    topics: List[Topic]
    created_at: datetime = field(default_factory=datetime.now)
    
    def get_source_by_id(self, source_id: str) -> Optional[Source]:
        """Get a source by its ID."""
        for source in self.sources:
            if source.id == source_id:
                return source
        return None
