"""
Content chunking by semantic boundaries.
"""
import re
from typing import List
from models import ContentChunk


class ContentChunker:
    """Chunks content by semantic boundaries (headings, paragraphs)."""
    
    def chunk(self, text: str) -> List[ContentChunk]:
        """
        Split content into semantic chunks.
        
        Args:
            text: Text to chunk
            
        Returns:
            List of ContentChunk objects
        """
        chunks = []
        
        # Split by headings (markdown style)
        sections = self._split_by_headings(text)
        
        for heading, level, content in sections:
            # Further split long sections by paragraphs
            if len(content) > 2000:  # If section is too long
                paragraphs = self._split_by_paragraphs(content)
                for i, para in enumerate(paragraphs):
                    if para.strip():
                        # First paragraph gets the heading
                        chunk_heading = heading if i == 0 else None
                        chunks.append(ContentChunk(
                            text=para.strip(),
                            heading=chunk_heading,
                            level=level
                        ))
            else:
                if content.strip():
                    chunks.append(ContentChunk(
                        text=content.strip(),
                        heading=heading,
                        level=level
                    ))
        
        return chunks
    
    def _split_by_headings(self, text: str) -> List[tuple]:
        """
        Split text by markdown headings.
        
        Returns:
            List of (heading_text, level, content) tuples
        """
        sections = []
        lines = text.split('\n')
        
        current_heading = None
        current_level = 0
        current_content = []
        
        heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
        
        for line in lines:
            match = heading_pattern.match(line)
            if match:
                # Save previous section
                if current_content or current_heading is None:
                    content = '\n'.join(current_content)
                    sections.append((current_heading, current_level, content))
                
                # Start new section
                current_level = len(match.group(1))
                current_heading = match.group(2).strip()
                current_content = []
            else:
                current_content.append(line)
        
        # Save last section
        if current_content or current_heading:
            content = '\n'.join(current_content)
            sections.append((current_heading, current_level, content))
        
        return sections
    
    def _split_by_paragraphs(self, text: str) -> List[str]:
        """Split text by paragraph breaks."""
        # Split on double newlines
        paragraphs = re.split(r'\n\n+', text)
        return [p.strip() for p in paragraphs if p.strip()]
