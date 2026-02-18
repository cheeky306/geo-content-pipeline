"""
Document collector for local files (PDFs, text files, etc.).
"""
import os
from pathlib import Path
from typing import Dict, Any
from .base_collector import BaseCollector
import pdfplumber


class DocumentCollector(BaseCollector):
    """Collects content from local documents."""
    
    SUPPORTED_EXTENSIONS = {'.pdf', '.txt', '.md', '.markdown'}
    
    def can_handle(self, location: str) -> bool:
        """Check if this is a supported document."""
        path = Path(location)
        return path.suffix.lower() in self.SUPPORTED_EXTENSIONS
    
    def collect(self, location: str) -> Dict[str, Any]:
        """
        Collect content from a document.
        
        Args:
            location: File path
            
        Returns:
            Dictionary with content, title, and metadata
        """
        path = Path(location)
        
        if not path.exists():
            return {
                'content': f'Error: File not found: {location}',
                'title': path.name,
                'metadata': {'error': 'File not found', 'path': str(path)}
            }
        
        extension = path.suffix.lower()
        
        if extension == '.pdf':
            return self._collect_pdf(path)
        elif extension in {'.txt', '.md', '.markdown'}:
            return self._collect_text(path)
        else:
            return {
                'content': f'Unsupported file type: {extension}',
                'title': path.name,
                'metadata': {'error': 'Unsupported file type', 'path': str(path)}
            }
    
    def _collect_pdf(self, path: Path) -> Dict[str, Any]:
        """Collect content from PDF."""
        try:
            content_parts = []
            metadata = {'path': str(path), 'type': 'pdf'}
            
            with pdfplumber.open(path) as pdf:
                # Get metadata from PDF
                if pdf.metadata:
                    if pdf.metadata.get('Title'):
                        metadata['title_from_pdf'] = pdf.metadata['Title']
                    if pdf.metadata.get('Author'):
                        metadata['author'] = pdf.metadata['Author']
                    if pdf.metadata.get('Subject'):
                        metadata['subject'] = pdf.metadata['Subject']
                
                metadata['pages'] = len(pdf.pages)
                
                # Extract text from all pages
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        content_parts.append(text)
            
            content = '\n\n'.join(content_parts)
            
            # Try to extract title from first page if not in metadata
            title = metadata.get('title_from_pdf', path.stem)
            if not metadata.get('title_from_pdf') and content:
                # Use first line or first significant text as title
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if len(line) > 10 and len(line) < 200:
                        title = line
                        break
            
            return {
                'content': content,
                'title': title,
                'metadata': metadata
            }
            
        except Exception as e:
            return {
                'content': f'Error reading PDF: {str(e)}',
                'title': path.name,
                'metadata': {'error': str(e), 'path': str(path)}
            }
    
    def _collect_text(self, path: Path) -> Dict[str, Any]:
        """Collect content from text file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Try to extract title from first line if markdown
            title = path.stem
            if path.suffix.lower() in {'.md', '.markdown'}:
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
            
            metadata = {
                'path': str(path),
                'type': 'text',
                'extension': path.suffix
            }
            
            return {
                'content': content,
                'title': title,
                'metadata': metadata
            }
            
        except UnicodeDecodeError:
            # Try with different encoding
            try:
                with open(path, 'r', encoding='latin-1') as f:
                    content = f.read()
                return {
                    'content': content,
                    'title': path.stem,
                    'metadata': {'path': str(path), 'type': 'text', 'encoding': 'latin-1'}
                }
            except Exception as e:
                return {
                    'content': f'Error reading file: {str(e)}',
                    'title': path.name,
                    'metadata': {'error': str(e), 'path': str(path)}
                }
        except Exception as e:
            return {
                'content': f'Error reading file: {str(e)}',
                'title': path.name,
                'metadata': {'error': str(e), 'path': str(path)}
            }
