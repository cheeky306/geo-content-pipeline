"""
Tier 2 - Source Content builder.
"""
from typing import List
from models import Source
from utils import extract_references


class Tier2Builder:
    """Builds the source content section (Tier 2) of the knowledge ledger."""
    
    def build(self, sources: List[Source]) -> str:
        """
        Build the source content section.
        
        Args:
            sources: List of all sources
            
        Returns:
            Markdown string for Tier 2
        """
        sections = []
        
        sections.append("## Source Content")
        sections.append("")
        
        for source in sources:
            # Source header with metadata
            sections.append(f"### [{source.id}] {source.title or source.name}")
            sections.append("")
            
            # Metadata line
            metadata_parts = [
                f"**Type**: {source.source_type.value}",
                f"**Authority**: {source.authority_score}"
            ]
            
            # Add location based on type
            if source.location.startswith('http'):
                metadata_parts.append(f"**URL**: {source.location}")
            else:
                metadata_parts.append(f"**File**: {source.location}")
            
            sections.append(' | '.join(metadata_parts))
            sections.append("")
            
            # Original content (preserved exactly)
            sections.append("#### Original Content")
            sections.append("")
            sections.append(source.content)
            sections.append("")
            
            # References section
            if source.references:
                sections.append("#### References from Source")
                sections.append("")
                for ref in source.references:
                    sections.append(f"- {ref}")
                sections.append("")
            
            # Cross-reference tag
            sections.append(f"**Cross-Reference**: [{source.id}]")
            sections.append("")
            sections.append("---")
            sections.append("")
        
        return '\n'.join(sections)
