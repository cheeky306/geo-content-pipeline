"""
Authority scoring for sources.
"""
from typing import Dict, Any
from models import SourceType
import re


class AuthorityScorer:
    """Scores sources based on type, domain, and content indicators."""
    
    # Base scores by source type
    TYPE_SCORES = {
        SourceType.ACADEMIC: 90,
        SourceType.RESEARCH: 85,
        SourceType.DOCUMENTATION: 75,
        SourceType.NEWS: 65,
        SourceType.BLOG: 55,
        SourceType.OPINION: 40,
        SourceType.UNKNOWN: 50,
    }
    
    def score(self, source_type: SourceType, content: str, 
              metadata: Dict[str, Any]) -> int:
        """
        Calculate authority score for a source.
        
        Args:
            source_type: Type of source
            content: Source content
            metadata: Source metadata
            
        Returns:
            Authority score (0-100)
        """
        # Start with base score for type
        score = self.TYPE_SCORES.get(source_type, 50)
        
        # Adjust based on domain (if URL)
        if 'url' in metadata:
            score += self._score_domain(metadata['url'])
        
        # Adjust based on content indicators
        score += self._score_content(content)
        
        # Adjust based on metadata indicators
        score += self._score_metadata(metadata)
        
        # Clamp to 0-100
        return max(0, min(100, score))
    
    def classify_type(self, content: str, metadata: Dict[str, Any]) -> SourceType:
        """
        Classify source type based on content and metadata.
        
        Args:
            content: Source content
            metadata: Source metadata
            
        Returns:
            Classified SourceType
        """
        content_lower = content.lower()
        
        # Check URL patterns
        if 'url' in metadata:
            url = metadata['url'].lower()
            
            if any(domain in url for domain in ['.edu', '.ac.uk', 'scholar.google', 'arxiv.org']):
                return SourceType.ACADEMIC
            
            if any(domain in url for domain in ['research', 'journal', 'paper']):
                return SourceType.RESEARCH
            
            if any(domain in url for domain in ['docs.', 'documentation', 'api.']):
                return SourceType.DOCUMENTATION
            
            if any(domain in url for domain in ['news', 'times', 'post', 'bbc', 'cnn', 'reuters']):
                return SourceType.NEWS
            
            if any(domain in url for domain in ['blog', 'medium.com', 'substack']):
                return SourceType.BLOG
        
        # Check PDF metadata
        if metadata.get('type') == 'pdf':
            # Look for research paper indicators
            if any(term in content_lower[:1000] for term in ['abstract', 'methodology', 'introduction', 'references']):
                # Check for academic structure
                if re.search(r'\babstract\b.*\bintroduction\b.*\bmethodology\b', content_lower, re.DOTALL):
                    return SourceType.RESEARCH
        
        # Check content indicators
        if re.search(r'\b(journal|peer.?review|doi:|issn:)\b', content_lower):
            return SourceType.ACADEMIC
        
        if any(term in content_lower[:500] for term in ['in my opinion', 'i think', 'i believe', 'personal view']):
            return SourceType.OPINION
        
        # Default to unknown if can't classify
        return SourceType.UNKNOWN
    
    def _score_domain(self, url: str) -> int:
        """Score based on domain authority."""
        url_lower = url.lower()
        
        # High authority domains
        if any(tld in url_lower for tld in ['.edu', '.gov', '.ac.uk']):
            return 15
        
        # Medium authority
        if any(domain in url_lower for domain in ['.org', 'arxiv', 'scholar', 'ieee', 'acm']):
            return 10
        
        # Established tech/news
        if any(domain in url_lower for domain in ['nytimes', 'wsj', 'bbc', 'reuters', 
                                                    'stackoverflow', 'github']):
            return 5
        
        return 0
    
    def _score_content(self, content: str) -> int:
        """Score based on content quality indicators."""
        score = 0
        content_lower = content.lower()
        
        # Has references/citations
        if re.search(r'(references|bibliography|citations)', content_lower):
            score += 10
        
        # Has data/statistics
        if re.search(r'\b\d+%|\b\d+\.\d+\b|figure \d+|table \d+', content):
            score += 5
        
        # Has methodology section
        if re.search(r'\b(methodology|methods|approach)\b', content_lower):
            score += 5
        
        # Has author credentials
        if re.search(r'\b(ph\.?d|professor|dr\.|researcher)\b', content_lower):
            score += 5
        
        # Penalty for clickbait indicators
        if re.search(r'\b(you won\'t believe|shocking|amazing|unbelievable)\b', content_lower):
            score -= 5
        
        return score
    
    def _score_metadata(self, metadata: Dict[str, Any]) -> int:
        """Score based on metadata."""
        score = 0
        
        # Has author
        if metadata.get('author'):
            score += 3
        
        # Has publish date
        if metadata.get('published_date'):
            score += 2
        
        # Has subject/description
        if metadata.get('subject') or metadata.get('description'):
            score += 2
        
        return score
