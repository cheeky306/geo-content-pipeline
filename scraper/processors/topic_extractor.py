"""
Topic extraction using TF-IDF and keyword analysis.
"""
from typing import List, Dict
from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from models import Topic, ProcessedContent


class TopicExtractor:
    """Extracts core topics from content using TF-IDF."""
    
    def __init__(self, max_topics: int = 10, min_sources: int = 1):
        """
        Initialize topic extractor.
        
        Args:
            max_topics: Maximum number of topics to extract
            min_sources: Minimum number of sources a topic must appear in
        """
        self.max_topics = max_topics
        self.min_sources = min_sources
    
    def extract_topics(self, processed_contents: List[ProcessedContent]) -> List[Topic]:
        """
        Extract core topics across all sources.
        
        Args:
            processed_contents: List of processed content
            
        Returns:
            List of Topic objects
        """
        if not processed_contents:
            return []
        
        # Prepare documents for TF-IDF
        documents = []
        source_ids = []
        
        for pc in processed_contents:
            documents.append(pc.cleaned_text)
            source_ids.append(pc.source_id)
        
        # Extract keywords using TF-IDF
        keywords_by_source = self._extract_keywords_tfidf(documents)
        
        # Cluster keywords into topics
        topics = self._cluster_keywords(keywords_by_source, source_ids)
        
        return topics[:self.max_topics]
    
    def _extract_keywords_tfidf(self, documents: List[str], top_n: int = 15) -> List[List[str]]:
        """
        Extract top keywords from each document using TF-IDF.
        
        Args:
            documents: List of document texts
            top_n: Number of top keywords per document
            
        Returns:
            List of keyword lists (one per document)
        """
        try:
            # Use TF-IDF to extract important terms
            vectorizer = TfidfVectorizer(
                max_features=500,
                stop_words='english',
                ngram_range=(1, 2),  # Unigrams and bigrams
                min_df=1,
                max_df=0.8
            )
            
            tfidf_matrix = vectorizer.fit_transform(documents)
            feature_names = vectorizer.get_feature_names_out()
            
            # Get top keywords for each document
            keywords_by_doc = []
            for doc_idx in range(len(documents)):
                # Get TF-IDF scores for this document
                doc_vector = tfidf_matrix[doc_idx].toarray().flatten()
                
                # Get indices of top scoring terms
                top_indices = doc_vector.argsort()[-top_n:][::-1]
                
                # Get the actual keywords
                keywords = [feature_names[i] for i in top_indices if doc_vector[i] > 0]
                keywords_by_doc.append(keywords)
            
            return keywords_by_doc
            
        except Exception as e:
            # Fallback to simple word frequency if TF-IDF fails
            return [self._extract_keywords_fallback(doc, top_n) for doc in documents]
    
    def _extract_keywords_fallback(self, text: str, top_n: int = 15) -> List[str]:
        """Fallback keyword extraction using word frequency."""
        # Simple word tokenization
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        
        # Common stop words
        stop_words = {'this', 'that', 'with', 'from', 'have', 'will', 'would', 
                      'could', 'should', 'about', 'their', 'there', 'these', 'those'}
        
        # Filter and count
        filtered = [w for w in words if w not in stop_words]
        counter = Counter(filtered)
        
        return [word for word, _ in counter.most_common(top_n)]
    
    def _cluster_keywords(self, keywords_by_source: List[List[str]], 
                         source_ids: List[str]) -> List[Topic]:
        """
        Group keywords into topics.
        
        Args:
            keywords_by_source: Keywords for each source
            source_ids: Corresponding source IDs
            
        Returns:
            List of Topic objects
        """
        # Count how many sources each keyword appears in
        keyword_sources = {}
        for source_id, keywords in zip(source_ids, keywords_by_source):
            for keyword in keywords:
                if keyword not in keyword_sources:
                    keyword_sources[keyword] = []
                if source_id not in keyword_sources[keyword]:
                    keyword_sources[keyword].append(source_id)
        
        # Create topics from keywords that appear in multiple sources or are highly relevant
        topics = []
        for keyword, sources in keyword_sources.items():
            if len(sources) >= self.min_sources:
                # Calculate relevance score based on number of sources
                relevance = len(sources) / len(source_ids)
                
                topics.append(Topic(
                    name=keyword.title(),
                    description=f"Topic related to {keyword}",
                    keywords=[keyword],
                    source_ids=sources,
                    relevance_score=relevance
                ))
        
        # Sort by relevance
        topics.sort(key=lambda t: t.relevance_score, reverse=True)
        
        return topics
