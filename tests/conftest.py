"""
This module provides the test fixtures for RAG testing with LlamaIndex.
"""
import pytest
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai_like import OpenAILike
from pathlib import Path
import shutil
import tempfile

class RAGTestEngine:
    """Wrapper class for RAG functionality to make testing easier."""
    
    def __init__(self, 
                 content_path: str,
                 model_path: str = "/models/NousResearch/Meta-Llama-3.1-8B-Instruct",
                 embed_model_name: str = "BAAI/bge-small-en-v1.5",
                 api_base: str = BASE_URL,
                 api_key: str = API_KEY):
        """Initialize the RAG engine.
        
        Args:
            content_path: Path to the content file/directory
            model_path: Path to the LLM model
            embed_model_name: Name of the embedding model
            api_base: API base URL
            api_key: API key
        """
        self.content_path = content_path
        
        # Initialize embedding model
        self.embed_model = HuggingFaceEmbedding(
            model_name=embed_model_name
        )
        
        # Initialize LLM
        self.llm = OpenAILike(
            model=model_path,
            api_base=api_base,
            api_key=api_key
        )
        
        # Configure global settings
        Settings.embed_model = self.embed_model
        Settings.llm = self.llm
        Settings.chunk_size = 100
        Settings.chunk_overlap = 20
        
        # Load and index content
        self._setup_index()
    
    def _setup_index(self):
        """Set up the vector index."""
        # Load documents
        documents = SimpleDirectoryReader(self.content_path).load_data()
        
        # Create index
        self.index = VectorStoreIndex.from_documents(
            documents,
            embed_model=self.embed_model
        )
        
        # Create query engine
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=2
        )
    
    def retrieve(self, query: str):
        """Retrieve relevant content for a query.
        
        Args:
            query: The search query
            
        Returns:
            List of source nodes from the retrieval
        """
        response = self.query_engine.query(query)
        return response.source_nodes
    
    def cleanup(self):
        """Clean up resources."""
        # Add any cleanup code here if needed
        pass

@pytest.fixture(scope="session")
def test_content():
    """Fixture to provide test content."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    temp_file = Path(temp_dir) / "test_content.txt"
    
    # Write some test content
    with open(temp_file, "w") as f:
        f.write("""
        Under the Wells Fargo Code of Conduct, employees may use their professional
        designations when they maintain all required licenses and certifications.
        However, they must ensure their use complies with company policies and
        professional standards. Medical licenses must be current and valid.
        
        The Code requires all employees to protect confidential information.
        This includes customer data, trade secrets, and proprietary information.
        Employees must never share sensitive data without proper authorization.
        
        Wells Fargo employees must avoid conflicts of interest. This means
        not using company resources for personal gain and disclosing any
        potential conflicts to management.
        """)
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture(scope="session")
def rag_engine(test_content):
    """Fixture to provide a RAG engine instance."""
    # Initialize engine with test content
    engine = RAGTestEngine(
        content_path=test_content,
        api_base=api_base,  # Replace with your API details
        api_key=api_key
    )
    
    yield engine
    
    # Cleanup
    engine.cleanup()

# Example test using the fixture
def test_basic_retrieval(rag_engine):
    """Test basic retrieval functionality."""
    query = "What does the code say about medical licenses?"
    results = rag_engine.retrieve(query)
    
    assert len(results) > 0
    assert any("medical licenses" in node.text.lower() for node in results)
