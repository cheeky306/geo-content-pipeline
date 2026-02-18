"""
Main ledger builder that coordinates tier builders.
"""
from models import KnowledgeLedger
from .tier1_builder import Tier1Builder
from .tier2_builder import Tier2Builder


class LedgerBuilder:
    """Assembles the complete knowledge ledger."""
    
    def __init__(self):
        self.tier1_builder = Tier1Builder()
        self.tier2_builder = Tier2Builder()
    
    def build(self, ledger: KnowledgeLedger) -> str:
        """
        Build the complete knowledge ledger markdown.
        
        Args:
            ledger: KnowledgeLedger with all data
            
        Returns:
            Complete markdown document
        """
        sections = []
        
        # Tier 1: Executive Index
        tier1 = self.tier1_builder.build(ledger.topics, ledger.sources)
        sections.append(tier1)
        
        # Tier 2: Source Content
        tier2 = self.tier2_builder.build(ledger.sources)
        sections.append(tier2)
        
        # Footer
        sections.append("---")
        sections.append("")
        sections.append(f"*Generated on {ledger.created_at.strftime('%Y-%m-%d %H:%M:%S')}*")
        sections.append("")
        
        return '\n'.join(sections)
    
    def validate(self, markdown: str, ledger: KnowledgeLedger) -> bool:
        """
        Validate that the generated ledger is complete.
        
        Args:
            markdown: Generated markdown
            ledger: Original ledger data
            
        Returns:
            True if valid
        """
        # Check that all source IDs are present
        for source in ledger.sources:
            if f"[{source.id}]" not in markdown:
                return False
        
        # Check that sections are present
        required_sections = [
            "# Knowledge Ledger",
            "## Executive Index",
            "### Core Topics",
            "### Source Map",
            "## Source Content"
        ]
        
        for section in required_sections:
            if section not in markdown:
                return False
        
        return True
