"""
Tier 1 - Executive Index builder.
"""
from typing import List
from models import Topic, Source
from utils import format_markdown_table


class Tier1Builder:
    """Builds the executive index (Tier 1) of the knowledge ledger."""
    
    def build(self, topics: List[Topic], sources: List[Source]) -> str:
        """
        Build the executive index section.
        
        Args:
            topics: List of extracted topics
            sources: List of all sources
            
        Returns:
            Markdown string for Tier 1
        """
        sections = []
        
        sections.append("# Knowledge Ledger")
        sections.append("")
        sections.append("## Executive Index")
        sections.append("")
        
        # Core Topics section
        sections.append("### Core Topics")
        sections.append("")
        
        if topics:
            for i, topic in enumerate(topics, 1):
                # Show topic with description and relevance
                sources_count = len(topic.source_ids)
                sections.append(f"{i}. **{topic.name}** - {topic.description} "
                              f"(mentioned in {sources_count} source{'s' if sources_count != 1 else ''})")
        else:
            sections.append("*No topics extracted*")
        
        sections.append("")
        
        # Source Map section
        sections.append("### Source Map")
        sections.append("")
        
        if sources:
            # Build table data
            headers = ["ID", "Source Name", "Type", "Authority", "Location"]
            rows = []
            
            for source in sources:
                # Truncate location if too long (URLs/paths)
                location = source.location
                if len(location) > 60:
                    location = location[:57] + "..."
                
                rows.append([
                    source.id,
                    source.name,
                    source.source_type.value,
                    str(source.authority_score),
                    location
                ])
            
            table = format_markdown_table(headers, rows)
            sections.append(table)
        else:
            sections.append("*No sources*")
        
        sections.append("")
        sections.append("---")
        sections.append("")
        
        return '\n'.join(sections)
