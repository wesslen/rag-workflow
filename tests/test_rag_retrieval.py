"""
Automatically generated test cases for RAG retrieval.
Generated on: 2025-01-12 00:27:54
"""
import pytest
import time
from typing import List

def normalize_text(text: str) -> str:
    """Normalize text for comparison."""
    return ' '.join(text.lower().split())

# Performance test constants
TEST_QUERIES = [
    "What are the requirements for medical licenses?",
    "How should employees handle confidential information?",
    "What are the policies on conflicts of interest?"
]

def test_retrieval_performance(rag_engine):
    """Test overall retrieval performance."""
    times = []
    for query in TEST_QUERIES:
        start_time = time.time()
        results = rag_engine.retrieve(query)
        retrieval_time = time.time() - start_time
        times.append(retrieval_time)

        assert len(results) > 0, f"No results returned for query: {query}"

    avg_time = sum(times) / len(times)
    assert avg_time < 2.0, f"Average retrieval time too high: {avg_time:.2f}s"


def test_retrieval_4(rag_engine):
    """Test retrieval for query: Reporting channels for accounting and auditing concerns"""
    query = 'Reporting channels for accounting and auditing concerns'
    expected_chunk = '7  Reporting channels . 7  Duty to cooperate . 7  Reporting concerns that are not misconduct . 7  Nonretaliation commitment . 8  Accounting, internal controls, or auditing matters .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6396450996398926, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_5(rag_engine):
    """Test retrieval for query: Reporting safety concerns to management."""
    query = 'Reporting safety concerns to management.'
    expected_chunk = '8  Accounting, internal controls, or auditing matters . 8  Safety concerns . 8  Required employee self-reporting . 8  Do what is right   Upholding our ethical and legal obligations .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6274938583374023, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_7(rag_engine):
    """Test retrieval for query: what are examples of potential conflicts of interest"""
    query = 'what are examples of potential conflicts of interest'
    expected_chunk = 'mitigate, disclose, or pre-clear conflicts . 9  Examples of potential conflicts . 10   Fair and honest business dealings . 13   Insider trading and other trading restrictions . 13   Anti-bribery and anti-corruption .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.879608154296875, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.88s"


def test_retrieval_8(rag_engine):
    """Test retrieval for query: Anti-bribery and anti-corruption policies worldwide"""
    query = 'Anti-bribery and anti-corruption policies worldwide'
    expected_chunk = '13   Anti-bribery and anti-corruption . 14   Competition and antitrust laws . 14   Global compliance . 15   Financial crimes and money laundering . 15   Sanctions, embargos,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.754209041595459, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.75s"


def test_retrieval_10(rag_engine):
    """Test retrieval for query: Information security and electronic communications policy"""
    query = 'Information security and electronic communications policy'
    expected_chunk = '16   Information security and electronic . .   communications . 16   Intellectual property . 17   Accurate records and disclosures . 17   Our workplace . 18   Anti-harassment and anti-discrimination .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.689291000366211, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.69s"


def test_retrieval_11(rag_engine):
    """Test retrieval for query: Valuing human rights in the workplace."""
    query = 'Valuing human rights in the workplace.'
    expected_chunk = '17   Our workplace . 18   Anti-harassment and anti-discrimination . 18   Hiring and advancement opportunities . 18   Workplace safety . 18   Human rights   Valuing human rights .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.641709327697754, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_12(rag_engine):
    """Test retrieval for query: Valuing human rights in the workplace safety policy."""
    query = 'Valuing human rights in the workplace safety policy.'
    expected_chunk = '18   Workplace safety . 18   Human rights   Valuing human rights . 18   Closing thoughts . 19   Waivers and exceptions . 19   Violations .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.649644374847412, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_17(rag_engine):
    """Test retrieval for query: CEO thanking employees for commitment to Code of Conduct"""
    query = 'CEO thanking employees for commitment to Code of Conduct'
    expected_chunk = 'Thank you for your commitment to our Code of Conduct, and thank you for the work you do to support our success.   Charles W. Scharf   CEO,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7948694229125977, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_18(rag_engine):
    """Test retrieval for query: Wells Fargo CEO Code of Conduct requirements"""
    query = 'Wells Fargo CEO Code of Conduct requirements'
    expected_chunk = 'Charles W. Scharf   CEO, Wells Fargo & Company Our Code   Our Code of Conduct (Code) applies to all employees, including executive officers,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6637639999389648, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_19(rag_engine):
    """Test retrieval for query: Wells Fargo Board of Directors definition"""
    query = 'Wells Fargo Board of Directors definition'
    expected_chunk = 'including executive officers, and in some cases the Board of Directors of Wells Fargo & Company (collectively referred to in this document as “the Board”).'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6756625175476074, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_20(rag_engine):
    """Test retrieval for query: Compliance with company policies and applicable laws."""
    query = 'Compliance with company policies and applicable laws.'
    expected_chunk = 'Employees are expected to adhere to the Code, Employee Handbook, and company policies and to comply with applicable laws and regulations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6787614822387695, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_21(rag_engine):
    """Test retrieval for query: What happens if company policies conflict with local laws?"""
    query = 'What happens if company policies conflict with local laws?'
    expected_chunk = 'Wells Fargo operates globally, and if, at any time, the Code 1 or our policies differ with local laws and regulations, the more restrictive guidance applies.   Whenever an expectation is unclear, employees should speak with their manager.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7085413932800293, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_22(rag_engine):
    """Test retrieval for query: What to do when an expectation is unclear at work."""
    query = 'What to do when an expectation is unclear at work.'
    expected_chunk = 'Whenever an expectation is unclear, employees should speak with their manager. If employees are uncomfortable speaking with their manager they can contact Employee Relations (ER), or the Ethics Office.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6568756103515625, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_25(rag_engine):
    """Test retrieval for query: What are Wells Fargo\'s employee code of conduct expectations?"""
    query = 'What are Wells Fargo\'s employee code of conduct expectations?'
    expected_chunk = 'Employees are expected to:   • Abide by the Code and seek guidance when uncertain.   • Comply with company policies.   • Represent Wells Fargo accurately and professionally.   • Manage risk in alignment with the company’s Risk Management Framework.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6834444999694824, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_26(rag_engine):
    """Test retrieval for query: Leaders risk management responsibility"""
    query = 'Leaders risk management responsibility'
    expected_chunk = '• Manage risk in alignment with the company’s Risk Management Framework.   As leaders, managers have an even greater level of responsibility.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6903905868530273, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.69s"


def test_retrieval_27(rag_engine):
    """Test retrieval for query: Managers\' responsibilities in leading with integrity."""
    query = 'Managers\' responsibilities in leading with integrity.'
    expected_chunk = 'As leaders, managers have an even greater level of responsibility. In addition to their responsibilities as employees, managers are expected to:   • Lead with integrity, demonstrating and reinforcing the Code.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7294540405273438, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_29(rag_engine):
    """Test retrieval for query: Reporting misconduct anonymously without fear of retaliation."""
    query = 'Reporting misconduct anonymously without fear of retaliation.'
    expected_chunk = '• Foster a work environment where employees feel comfortable speaking up without fear of retaliation.   • Listen to employees and report concerns that may be misconduct as soon as possible, with appropriate confidentiality.   • Develop high performing teams.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.648237705230713, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_30(rag_engine):
    """Test retrieval for query: What language versions of the Code of Conduct exist?"""
    query = 'What language versions of the Code of Conduct exist?'
    expected_chunk = '• Develop high performing teams.    > 1The Code is translated into several languages. If there is a conflict or inconsistency between the translations, the English version prevails, where applicable. > 4 of 19 Code of Conduct >'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7332587242126465, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_32(rag_engine):
    """Test retrieval for query: Company culture and values at Wells Fargo."""
    query = 'Company culture and values at Wells Fargo.'
    expected_chunk = 'culture   # Who we are   Wells Fargo is committed to a culture that attracts and retains the best people who help us become a better, stronger company.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6403675079345703, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_33(rag_engine):
    """Test retrieval for query: Risk Management Framework company culture components"""
    query = 'Risk Management Framework company culture components'
    expected_chunk = 'a culture that attracts and retains the best people who help us become a better, stronger company. Adherence to the Risk Management Framework and effective risk management are key components of our company’s culture.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6482248306274414, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_34(rag_engine):
    """Test retrieval for query: What drives our customer-centric company culture?"""
    query = 'What drives our customer-centric company culture?'
    expected_chunk = 'Our culture is also guided by a customer-centric focus informed by employee engagement and feedback and reinforced by clear employee expectations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6584811210632324, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_35(rag_engine):
    """Test retrieval for query: What are Wells Fargo\'s employee expectations?"""
    query = 'What are Wells Fargo\'s employee expectations?'
    expected_chunk = 'Our employee expectations are designed to be clear and straightforward, to drive the highest standards of integrity and operational excellence, and to provide guidance for doing what’s right and doing it well.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7287688255310059, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_36(rag_engine):
    """Test retrieval for query: Champion diversity equity and inclusion policy"""
    query = 'Champion diversity equity and inclusion policy'
    expected_chunk = 'These expectations are:   • Embrace candor   • Do what’s right   • Be great at execution   • Learn and grow   • Champion diversity, equity, and inclusion   • Build high-performing teams ( for managers )  # Diversity,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7520785331726074, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.75s"


def test_retrieval_37(rag_engine):
    """Test retrieval for query: Building diverse high performing teams at Wells Fargo."""
    query = 'Building diverse high performing teams at Wells Fargo.'
    expected_chunk = 'equity, and inclusion   • Build high-performing teams ( for managers )  # Diversity, equity, and inclusion   We are committed to creating a culture with broad representation of who we are, how we think, and how we make decisions.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.695185661315918, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_38(rag_engine):
    """Test retrieval for query: Increasing diverse representation in the company culture."""
    query = 'Increasing diverse representation in the company culture.'
    expected_chunk = 'how we think, and how we make decisions. We are focused on increasing diverse representation at all levels of the company through an inclusive culture and workplace environment; better serving and growing relationships with diverse customers in each line of business; and supporting our spend with diverse suppliers company-wide.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.628312587738037, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_39(rag_engine):
    """Test retrieval for query: Wells Fargo expectations for diversity and inclusion."""
    query = 'Wells Fargo expectations for diversity and inclusion.'
    expected_chunk = 'One of our expectations is to champion diversity, equity, and inclusion.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6244707107543945, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_40(rag_engine):
    """Test retrieval for query: Benefits of a diverse workforce at Wells Fargo."""
    query = 'Benefits of a diverse workforce at Wells Fargo.'
    expected_chunk = 'One of our expectations is to champion diversity, equity, and inclusion. We believe a diverse and inclusive workforce drives creativity, insight, and innovation in our business, and allows us to respond effectively to the evolving needs of our customers, colleagues, and communities.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.695540428161621, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_41(rag_engine):
    """Test retrieval for query: Creating a safe and inclusive workplace environment."""
    query = 'Creating a safe and inclusive workplace environment.'
    expected_chunk = 'Employees are encouraged to:   • Contribute to a safe, inclusive environment where differences are respected.   • Educate themselves about unconscious bias.   • Solicit diverse ideas that challenge thinking.   > 5 of 19 Code of'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6974000930786133, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_42(rag_engine):
    """Test retrieval for query: Challenge thinking in decision making processes"""
    query = 'Challenge thinking in decision making processes'
    expected_chunk = '• Solicit diverse ideas that challenge thinking.   > 5 of 19 Code of Conduct > TOC  Decision making  Speak Up Introduction  Do what is right  Closing  # Decision making   Wells Fargo’s employees make decisions each'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6789331436157227, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_43(rag_engine):
    """Test retrieval for query: What decisions should I make if they don\'t align with the Code?"""
    query = 'What decisions should I make if they don\'t align with the Code?'
    expected_chunk = 'Do what is right  Closing  # Decision making   Wells Fargo’s employees make decisions each day and must evaluate whether those decisions align with the Code.   If the answer to any of these questions is no, do not proceed .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7411022186279297, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_44(rag_engine):
    """Test retrieval for query: When should I seek guidance on a workplace decision?"""
    query = 'When should I seek guidance on a workplace decision?'
    expected_chunk = 'with the Code.   If the answer to any of these questions is no, do not proceed .  # Seek guidance when not sure   While every decision matters, no single document can cover every possible situation or govern every decision made in the workplace.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8148622512817383, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.81s"


def test_retrieval_45(rag_engine):
    """Test retrieval for query: Is employee code guidance provided by manager legal"""
    query = 'Is employee code guidance provided by manager legal'
    expected_chunk = 'Employees are expected to use good judgement in applying the Code. If they are uncertain of the right course of action, they should seek guidance from their manager.   Questions to ask:   1) Is it legal?'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7890453338623047, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_47(rag_engine):
    """Test retrieval for query: Is our decision consistent with customer and shareholder obligations?"""
    query = 'Is our decision consistent with customer and shareholder obligations?'
    expected_chunk = '3) Is it consistent with our expectations?   4) Does it align with our obligations to our customers or shareholders?   5) Are we comfortable if our decision is made public?   Yes to all.   Decision is likely   ethical.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8816909790039062, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.88s"


def test_retrieval_48(rag_engine):
    """Test retrieval for query: What is the correct response when unsure about a decision?"""
    query = 'What is the correct response when unsure about a decision?'
    expected_chunk = 'Yes to all.   Decision is likely   ethical.   Not sure.   Seek guidance.   No to any.   Do not   proceed.   > TOC  Decision making  Speak Up Introduction  Do what is right'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6820306777954102, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_51(rag_engine):
    """Test retrieval for query: Reporting misconduct in the Code of Conduct"""
    query = 'Reporting misconduct in the Code of Conduct'
    expected_chunk = 'Code of Conduct  # Speaking up   Employees are responsible for speaking up promptly when becoming aware of potential misconduct, including potential violations of the Code, even if the employee is not directly involved or affected by the behavior.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6350421905517578, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_52(rag_engine):
    """Test retrieval for query: Investigating allegations of misconduct in the workplace."""
    query = 'Investigating allegations of misconduct in the workplace.'
    expected_chunk = 'even if the employee is not directly involved or affected by the behavior. Allegations of misconduct are investigated and managed in an objective, thorough, consistent, and timely manner with the goal of understanding and resolving concerns.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.636559009552002, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_53(rag_engine):
    """Test retrieval for query: Reporting potential misconduct to manager or other channels"""
    query = 'Reporting potential misconduct to manager or other channels'
    expected_chunk = '# Resources to report potential misconduct   Employees are expected to report potential misconduct to their manager. If employees are uncomfortable doing so, they can report through the other reporting channels listed below.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7916531562805176, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_55(rag_engine):
    """Test retrieval for query: How to report ethics concerns by phone in the US."""
    query = 'How to report ethics concerns by phone in the US.'
    expected_chunk = 'To the   • EthicsLine by phone extent permitted by local or applicable laws and   − U.S. and Canada (800) 382-7250 regulations, employees may choose to remain   − non-U.S.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6498985290527344, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_56(rag_engine):
    """Test retrieval for query: Reporting anonymous tip internationally"""
    query = 'Reporting anonymous tip internationally'
    expected_chunk = 'use link and select country for specific anonymous.   dialing instructions   • EthicsLine Online Reporting (https://wellsfargo.ethicspoint.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6602392196655273, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_57(rag_engine):
    """Test retrieval for query: Reporting misconduct to regulatory bodies outside the US"""
    query = 'Reporting misconduct to regulatory bodies outside the US'
    expected_chunk = 'ethicspoint.com/ )  Nothing prohibits an employee from reporting potential misconduct or potential noncompliance with laws and regulations by Wells Fargo directly to the applicable regulatory bodies or government agencies or authorities.   Additional information for non-U.S.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6307411193847656, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_58(rag_engine):
    """Test retrieval for query: Reporting procedures for non US employees grievance resolution"""
    query = 'Reporting procedures for non US employees grievance resolution'
    expected_chunk = 'Additional information for non-U.S. based employees   Where applicable, follow local grievance resolution or reporting procedures. If there is no specific grievance resolution or reporting procedure, use a reporting channel listed above.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6711335182189941, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_59(rag_engine):
    """Test retrieval for query: Cooperation with internal or external investigations at Wells Fargo."""
    query = 'Cooperation with internal or external investigations at Wells Fargo.'
    expected_chunk = 'If there is no specific grievance resolution or reporting procedure, use a reporting channel listed above.   Duty to cooperate   Wells Fargo employees are expected to fully cooperate in any internal or external investigation that is being conducted or directed by Wells Fargo.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7244610786437988, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.72s"


def test_retrieval_60(rag_engine):
    """Test retrieval for query: Tampering with information during internal investigations."""
    query = 'Tampering with information during internal investigations.'
    expected_chunk = 'Employees must not withhold or tamper with information, or in any way attempt to influence others participating in the investigation.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6501073837280273, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_61(rag_engine):
    """Test retrieval for query: Reporting non misconduct concerns at work"""
    query = 'Reporting non misconduct concerns at work'
    expected_chunk = '# Reporting concerns that are not misconduct   Concerns unrelated to misconduct such as performance feedback, workplace disputes, inadvertent errors, business processes, or not following procedures should also be raised.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6521077156066895, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_62(rag_engine):
    """Test retrieval for query: Reporting channels for workplace disputes and performance concerns."""
    query = 'Reporting channels for workplace disputes and performance concerns.'
    expected_chunk = 'Managers are the starting point to help resolve these concerns or guide employees to the appropriate reporting channel. Employees should consider the following reporting channels:   • Employee Relations for performance concerns or workplace disputes.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6386442184448242, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_63(rag_engine):
    """Test retrieval for query: Reporting channels for workplace disputes at Wells Fargo."""
    query = 'Reporting channels for workplace disputes at Wells Fargo.'
    expected_chunk = 'Employees should consider the following reporting channels:   • Employee Relations for performance concerns or workplace disputes.   • Control Management or Independent Risk Management for risks, errors, or business process concerns.   • Wells Fargo Employee Assistance Consulting (U.S.)'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.906254768371582, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.91s"


def test_retrieval_64(rag_engine):
    """Test retrieval for query: Employee Assistance Program support for work difficulties"""
    query = 'Employee Assistance Program support for work difficulties'
    expected_chunk = '• Wells Fargo Employee Assistance Consulting (U.S.) and Employee Assistance Program (International) for support in resolving personal and work-related difficulties.   • Loudspeaker for ideas and business process improvements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6684179306030273, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_65(rag_engine):
    """Test retrieval for query: Improvement ideas through loudspeaker system"""
    query = 'Improvement ideas through loudspeaker system'
    expected_chunk = '• Loudspeaker for ideas and business process improvements.   • Policy Governance Platform (PGP) for identified policy violations, in accordance with the Policy Management Procedures.   > 7 of 19 Code of Conduct > TOC  Decision making'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6521692276000977, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_68(rag_engine):
    """Test retrieval for query: Retaliation against employees who report policy violations."""
    query = 'Retaliation against employees who report policy violations.'
    expected_chunk = 'potential violations of company policies, procedures, this Code, or potential noncompliance with law. Similarly, Wells Fargo prohibits retaliation against any employee who assists or participates in an investigation, proceeding, or hearing, or exercises any right protected by law.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6757655143737793, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_69(rag_engine):
    """Test retrieval for query: Reporting financial reporting code violations"""
    query = 'Reporting financial reporting code violations'
    expected_chunk = 'Employees must report potential retaliation using methods listed under Resources to report potential misconduct.   # Accounting, internal controls, or auditing matters   If an employee becomes aware of Code violations related to Wells Fargo’s financial reporting, accounting, internal controls,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.59775972366333, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.60s"


def test_retrieval_70(rag_engine):
    """Test retrieval for query: Reporting internal control or audit violations to whom"""
    query = 'Reporting internal control or audit violations to whom'
    expected_chunk = 'accounting, internal controls, or audit matters, then they must report such violations using a reporting channel listed under Resources to report potential misconduct or directly to the Audit Committee of the Board.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6426610946655273, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_71(rag_engine):
    """Test retrieval for query: Communicating with Board directors or committees process"""
    query = 'Communicating with Board directors or committees process'
    expected_chunk = 'Information about communicating with directors or other committees of the Board and the process for reviewing communications sent to the Board or its members is available on the Leadership and Governance page of wellsfargo.com .'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6816844940185547, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_72(rag_engine):
    """Test retrieval for query: What to do in case of workplace violence threat"""
    query = 'What to do in case of workplace violence threat'
    expected_chunk = '# Safety concerns   Acts of violence, threats or perceived threats should be taken seriously. In the event of immediate danger, employees should contact local law enforcement at 911 or other designated emergency number.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7595314979553223, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_73(rag_engine):
    """Test retrieval for query: Report non-emergency security threats to Wells Fargo."""
    query = 'Report non-emergency security threats to Wells Fargo.'
    expected_chunk = 'Non-emergency threats can be reported to the Wells Fargo Security Response Center at U.S. (877) 494-9355, non-U.S. call   001‑480‑437‑7599 , or to a manager.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.858717441558838, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.86s"


def test_retrieval_75(rag_engine):
    """Test retrieval for query: Criminal background check requirements for new hires"""
    query = 'Criminal background check requirements for new hires'
    expected_chunk = 'Wells Fargo offers of employment are contingent upon the candidate successfully passing a criminal background check. Wells Fargo may also conduct additional background checks during employment. Unless prohibited by local law, employees must notify Employee Relations if they are convicted of,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6289997100830078, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_76(rag_engine):
    """Test retrieval for query: crime convictions involving dishonesty or breach of trust"""
    query = 'crime convictions involving dishonesty or breach of trust'
    expected_chunk = 'Unless prohibited by local law, employees must notify Employee Relations if they are convicted of, or enter a plea of guilty or no contest to, any crime involving dishonesty, breach of trust, money laundering, or the manufacture, sale, distribution,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.661851406097412, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_77(rag_engine):
    """Test retrieval for query: Offenses impacting employment eligibility criteria"""
    query = 'Offenses impacting employment eligibility criteria'
    expected_chunk = 'breach of trust, money laundering, or the manufacture, sale, distribution, or trafficking of controlled substances so that Wells Fargo can assess whether the offense impacts the employee’s employment eligibility.   > 8 of 19 Code of Conduct > TOC'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6762309074401855, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_79(rag_engine):
    """Test retrieval for query: conflicts of interest in Wells Fargo policies"""
    query = 'conflicts of interest in Wells Fargo policies'
    expected_chunk = 'Upholding our ethical and legal obligations   # Identify and avoid conflicts of interest   Wells Fargo is committed to identifying and either preventing or managing conflicts of interest.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6440272331237793, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_80(rag_engine):
    """Test retrieval for query: Conflict of interest company reputation jeopardy"""
    query = 'Conflict of interest company reputation jeopardy'
    expected_chunk = 'of interest   Wells Fargo is committed to identifying and either preventing or managing conflicts of interest. Employees need to recognize that certain activities can cause an actual, potential, or perceived conflict of interest, or jeopardize the company’s integrity or reputation.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.642636775970459, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_83(rag_engine):
    """Test retrieval for query: pre-clearance of personal activities under company policies"""
    query = 'pre-clearance of personal activities under company policies'
    expected_chunk = 'Some employees are subject to additional requirements and restrictions, including pre-clearance of personal activities under company business policies and procedures.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6209001541137695, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_84(rag_engine):
    """Test retrieval for query: pre-clearing employee activities with potential conflicts"""
    query = 'pre-clearing employee activities with potential conflicts'
    expected_chunk = '# Manage, mitigate, disclose, or pre -  # clear conflicts   Employees need to pre-clear any activity that may give rise to a conflict prior to engaging in the activity. In addition, certain relationships and activities require disclosure to mitigate risk.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.698183536529541, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_85(rag_engine):
    """Test retrieval for query: Compliance instructions for mitigating conflict of interest"""
    query = 'Compliance instructions for mitigating conflict of interest'
    expected_chunk = 'In addition, certain relationships and activities require disclosure to mitigate risk. Once the pre-clearance or disclosure is processed, Compliance provides specific instructions on how to mitigate or manage any potential conflict of interest.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6427550315856934, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_86(rag_engine):
    """Test retrieval for query: Conflict of interest definition Wells Fargo employees"""
    query = 'Conflict of interest definition Wells Fargo employees'
    expected_chunk = 'Definitions   A personal conflict of interest occurs when an employee acts, or appears to act, in their personal interest rather than acting in the interest of Wells Fargo or its customers.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6292357444763184, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_87(rag_engine):
    """Test retrieval for query: Using company property for personal benefit"""
    query = 'Using company property for personal benefit'
    expected_chunk = 'Examples of personal conflicts:   • An employee receives an improper benefit or gift because of their position with Wells Fargo.   • An employee uses company property, information, or position for personal benefit or to compete or divert business from Wells Fargo.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6378755569458008, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_88(rag_engine):
    """Test retrieval for query: Conflict of interest in advisory services and financing transactions."""
    query = 'Conflict of interest in advisory services and financing transactions.'
    expected_chunk = 'A business conflict of interest occurs when Wells Fargo’s interests conflict with those of a customer.   Examples of business conflicts:   • Providing advisory services to a customer on a transaction while providing financing to another customer on the same transaction.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.654076099395752, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_89(rag_engine):
    """Test retrieval for query: acting as trustee to debt security investors"""
    query = 'acting as trustee to debt security investors'
    expected_chunk = '• Acting as trustee to investors on a debt security and acting as a lender to the security issuer.   > TOC  Decision making  Speak Up Introduction  Do what is right  Closing  Did you know?'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7031631469726562, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_90(rag_engine):
    """Test retrieval for query: disclosing conflicts after engaging in activities"""
    query = 'disclosing conflicts after engaging in activities'
    expected_chunk = 'Sometimes a conflict arises after engaging in an activity. In these situations, the conflict must be disclosed as soon as possible.   > 9 of 19 Code of Conduct 10 of 19 Code of Conduct  # Examples of potential conflicts'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7167305946350098, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.72s"


def test_retrieval_91(rag_engine):
    """Test retrieval for query: Examples of potential conflicts of interest in the Code of Conduct."""
    query = 'Examples of potential conflicts of interest in the Code of Conduct.'
    expected_chunk = 'of 19 Code of Conduct 10 of 19 Code of Conduct  # Examples of potential conflicts   Below are some common situations where conflicts of interest may be present and how employees are expected to avoid the conflict of interest by not engaging in prohibited activities'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8293156623840332, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.83s"


def test_retrieval_92(rag_engine):
    """Test retrieval for query: What situations require pre-clearance to avoid conflict of interest?"""
    query = 'What situations require pre-clearance to avoid conflict of interest?'
    expected_chunk = 'may be present and how employees are expected to avoid the conflict of interest by not engaging in prohibited activities or obtaining pre-clearance when required. The list of situations is not meant to be a complete list of every place a conflict can occur.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7149558067321777, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_93(rag_engine):
    """Test retrieval for query: Competing business owned by Wells Fargo employees."""
    query = 'Competing business owned by Wells Fargo employees.'
    expected_chunk = 'Outside activities   Employees generally may not:   • Own or operate a business that competes with Wells Fargo.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6233611106872559, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_94(rag_engine):
    """Test retrieval for query: Wells Fargo conflict of interest secondary employment rules"""
    query = 'Wells Fargo conflict of interest secondary employment rules'
    expected_chunk = '• Accept secondary employment or perform consulting services with any entity that competes with Wells Fargo, otherwise conflicts with their Wells Fargo duties, or diverts Wells Fargo business.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6611433029174805, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_95(rag_engine):
    """Test retrieval for query: Salesperson conflict of interest own residence purchase"""
    query = 'Salesperson conflict of interest own residence purchase'
    expected_chunk = '• Act as a real estate salesperson, broker, or agent, except for the purchase or sale of their own residence.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6224207878112793, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_96(rag_engine):
    """Test retrieval for query: director positions without pre clearance"""
    query = 'director positions without pre clearance'
    expected_chunk = '• Accept a position with any for-profit business as a director, trustee, officer, general partner, or similar position of influence without pre-clearance.   • Be compensated directly or indirectly for providing investment or legal advice.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6343069076538086, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_98(rag_engine):
    """Test retrieval for query: Wells Fargo volunteer and charitable activities policy"""
    query = 'Wells Fargo volunteer and charitable activities policy'
    expected_chunk = '• Speak on the company’s behalf in the media without prior approval or publish works related to their role or the company without prior approval.   Volunteer and charitable activities   Wells Fargo encourages employees to be active volunteers in the community.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6419615745544434, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_99(rag_engine):
    """Test retrieval for query: Volunteer activities requiring pre-clearance at Wells Fargo"""
    query = 'Volunteer activities requiring pre-clearance at Wells Fargo'
    expected_chunk = 'Volunteer and charitable activities   Wells Fargo encourages employees to be active volunteers in the community. While many volunteer activities do not require pre-clearance, to avoid actual, potential, or perceived conflicts,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6589293479919434, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_100(rag_engine):
    """Test retrieval for query: Nonprofit financial management approval requirements."""
    query = 'Nonprofit financial management approval requirements.'
    expected_chunk = 'to avoid actual, potential, or perceived conflicts, employees must review pre-clearance requirements and when required obtain approval prior to engaging in certain nonprofit activities, including:   • Managing the finances or investments of the nonprofit.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7907428741455078, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_102(rag_engine):
    """Test retrieval for query: Soliciting funds from customers or employees for a nonprofit."""
    query = 'Soliciting funds from customers or employees for a nonprofit.'
    expected_chunk = '• Receiving compensation for service.   Employees may not solicit Wells Fargo customers, employees, or third-party service providers when raising funds for a nonprofit.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7084670066833496, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_103(rag_engine):
    """Test retrieval for query: workplace relationships interfering with job responsibilities"""
    query = 'workplace relationships interfering with job responsibilities'
    expected_chunk = 'Personal r elationships   Personal relationships in the workplace may interfere with job responsibilities and decision making. For this reason, all employees, new hires,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6532721519470215, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_104(rag_engine):
    """Test retrieval for query: Wells Fargo employee personal relationship disclosure policy."""
    query = 'Wells Fargo employee personal relationship disclosure policy.'
    expected_chunk = 'For this reason, all employees, new hires, or rehires are required to disclose personal relationships (as defined in the Personal and Family Relationships at Work Policy) with other Wells Fargo employees or contingent resources so the relationship may be reviewed for potential conflicts.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.681589126586914, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_105(rag_engine):
    """Test retrieval for query: Related Person Transaction Policy and Procedures requirements"""
    query = 'Related Person Transaction Policy and Procedures requirements'
    expected_chunk = 'Additional requireme nts for the Board, executive officers, and certain stockholders and their immediate family members are outlined in the Related Person Transaction Policy and Procedures. 11 of 19 Code of Conduct   # Examples of potential conflicts,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.666313648223877, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_106(rag_engine):
    """Test retrieval for query: Wells Fargo gift and entertainment policies."""
    query = 'Wells Fargo gift and entertainment policies.'
    expected_chunk = '11 of 19 Code of Conduct   # Examples of potential conflicts, continued   Gifts and entertainment   Wells Fargo permits giving and receiving business gifts and entertainment provided there is no reasonable inference that the gift or entertainment could influence the performance or decision making of any employee.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6871075630187988, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.69s"


def test_retrieval_107(rag_engine):
    """Test retrieval for query: Gifts and entertainment with business associates guidelines"""
    query = 'Gifts and entertainment with business associates guidelines'
    expected_chunk = 'The gift or entertainment with any one individual or entity should occur infrequently and be consistent with accepted, lawful business practices and customs.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6602225303649902, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_108(rag_engine):
    """Test retrieval for query: Gifts for business referrals or advantages"""
    query = 'Gifts for business referrals or advantages'
    expected_chunk = 'Employees should conduct themselves in accordance with the following expectations:   • Refrain from giving and receiving gifts offered in exchange for business referrals or other business advantages.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.643669605255127, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_109(rag_engine):
    """Test retrieval for query: Gifts that are not allowed by Wells Fargo policy"""
    query = 'Gifts that are not allowed by Wells Fargo policy'
    expected_chunk = '• Never give or receive gifts that are cash or cash equivalents, cannabis-related, or otherwise do not comply with our policies.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8439364433288574, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.84s"


def test_retrieval_110(rag_engine):
    """Test retrieval for query: preclearing gifts with government officials globally"""
    query = 'preclearing gifts with government officials globally'
    expected_chunk = '• Follow requirements to pre-clear the exchange of any gift or entertainment with government officials or government entities through the Global Preclearance System. Gifts or entertainment provided to government officials or government entities are controlled by strict laws and regulations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8250370025634766, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.83s"


def test_retrieval_111(rag_engine):
    """Test retrieval for query: Reporting payments to labor organizations or their representatives."""
    query = 'Reporting payments to labor organizations or their representatives.'
    expected_chunk = 'Gifts or entertainment provided to government officials or government entities are controlled by strict laws and regulations.   • Report a payment, loan, gift, entertainment, or anything else of value provided to labor organizations or their representatives, as these transactions are also subject to strict laws and regulations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6735434532165527, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_112(rag_engine):
    """Test retrieval for query: gifts or entertainment in contract negotiations"""
    query = 'gifts or entertainment in contract negotiations'
    expected_chunk = '• Consult with a manager before providing gifts or entertainment to individuals or entities involved in contract negotiations or competitive bidding with Wells Fargo.   Interactions with third parties   When engaging with a third party on behalf of Wells Fargo,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.652780532836914, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_113(rag_engine):
    """Test retrieval for query: Third party relationships creating conflict of interest risks"""
    query = 'Third party relationships creating conflict of interest risks'
    expected_chunk = 'Interactions with third parties   When engaging with a third party on behalf of Wells Fargo, employees must confirm that the third party relationship does not create undue risks, including a conflict of interest,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6489968299865723, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_114(rag_engine):
    """Test retrieval for query: Third party relationships creating undue risks to internal controls."""
    query = 'Third party relationships creating undue risks to internal controls.'
    expected_chunk = 'employees must confirm that the third party relationship does not create undue risks, including a conflict of interest, or impair the quality and independence of Wells Fargo’s internal controls, or the ability of relevant authorities to oversee and supervise compliance with regulatory requirements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.663114070892334, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_115(rag_engine):
    """Test retrieval for query: Employee participation in political activities allowed."""
    query = 'Employee participation in political activities allowed.'
    expected_chunk = 'or the ability of relevant authorities to oversee and supervise compliance with regulatory requirements.   Political activities   Employees have the right to participate in the political process and to support candidates, parties, or initiatives of their choice.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6081414222717285, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.61s"


def test_retrieval_117(rag_engine):
    """Test retrieval for query: Wells Fargo employee political activity disclosure requirements"""
    query = 'Wells Fargo employee political activity disclosure requirements'
    expected_chunk = 'Political activity is strictly regulated under   U.S. lobbying and pay-to-play laws. Employees must:   • Be clear that personal political opinions and activities are not represented as those of Wells Fargo.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7343978881835938, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_118(rag_engine):
    """Test retrieval for query: Public office candidate pre-clearance approval requirements"""
    query = 'Public office candidate pre-clearance approval requirements'
    expected_chunk = '• Obtain pre-clearance approval before becoming, agreeing to become, or announcing intention to become a candidate or appointee to a public office.   • Obtain pre-clearance approval before communicating with U.S.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7443675994873047, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_119(rag_engine):
    """Test retrieval for query: pre clearance approval for government business solicitations"""
    query = 'pre clearance approval for government business solicitations'
    expected_chunk = '• Obtain pre-clearance approval before communicating with U.S. government officials or entities for the purpose of soliciting new government business.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7770934104919434, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.78s"


def test_retrieval_120(rag_engine):
    """Test retrieval for query: Company political contributions without government relations approval"""
    query = 'Company political contributions without government relations approval'
    expected_chunk = 'government officials or entities for the purpose of soliciting new government business.   • Never make political contributions on behalf of the company without prior approval from the Government Relations and Public Policy team.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6996545791625977, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_121(rag_engine):
    """Test retrieval for query: Wells Fargo campaign contribution policy Political Action Committees"""
    query = 'Wells Fargo campaign contribution policy Political Action Committees'
    expected_chunk = 'Company funds are never used for any campaign contributions, candidate campaign committees, political parties, caucuses, or independent expenditure committees. Wells Fargo supports U.S. candidates seeking public office only through Wells Fargo-sponsored Political Action Committees.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.647986888885498, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_122(rag_engine):
    """Test retrieval for query: Wells Fargo employee political activity approval process."""
    query = 'Wells Fargo employee political activity approval process.'
    expected_chunk = 'candidates seeking public office only through Wells Fargo-sponsored Political Action Committees.   Covered employees and their family members are subject to additional requirements and restrictions, including approval of outside political activities, contributions, and fundraising under applicable laws.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6564722061157227, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_123(rag_engine):
    """Test retrieval for query: Wells Fargo employee professional designations requirements"""
    query = 'Wells Fargo employee professional designations requirements'
    expected_chunk = '12 of 19 Code of Conduct   # Examples of potential conflicts, continued   Use of professional designations   Wells Fargo acknowledges employees may maintain specialized, professional designations that may not relate to their duties with the company.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6738786697387695, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_124(rag_engine):
    """Test retrieval for query: Professional licenses and certifications required by employees."""
    query = 'Professional licenses and certifications required by employees.'
    expected_chunk = 'These include but are not limited to legal, medical, notary, accounting, and investment licenses and certifications.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.609222412109375, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.61s"


def test_retrieval_125(rag_engine):
    """Test retrieval for query: Fiduciary duties and professional designation requirements"""
    query = 'Fiduciary duties and professional designation requirements'
    expected_chunk = 'Employees must not misrepresent or use their professional designation if it is not appropriate for their role or if prohibited by company policy or applicable laws and regulations.   Fiduciary and investment duties   When executing fiduciary duties or responsibilities,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6497130393981934, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_126(rag_engine):
    """Test retrieval for query: Fiduciary duties when acting as investment manager"""
    query = 'Fiduciary duties when acting as investment manager'
    expected_chunk = 'Fiduciary and investment duties   When executing fiduciary duties or responsibilities, acting as a trustee, investment manager, or in any similar capacity in which the company possesses investment discretion on behalf of another,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.669050693511963, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_127(rag_engine):
    """Test retrieval for query: Wells Fargo investment manager fiduciary duty policy."""
    query = 'Wells Fargo investment manager fiduciary duty policy.'
    expected_chunk = 'investment manager, or in any similar capacity in which the company possesses investment discretion on behalf of another, Wells Fargo acts in the best interest of our clients. If a conflict arises, the company puts the client’s interests ahead of its own.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.654581069946289, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_128(rag_engine):
    """Test retrieval for query: executor appointments in employee roles"""
    query = 'executor appointments in employee roles'
    expected_chunk = 'If a conflict arises, the company puts the client’s interests ahead of its own.   Employees may accept appointments as an executor, personal representative, administrator, guardian, trustee,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7879490852355957, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_129(rag_engine):
    """Test retrieval for query: Executor appointments for personal relationships."""
    query = 'Executor appointments for personal relationships.'
    expected_chunk = 'Employees may accept appointments as an executor, personal representative, administrator, guardian, trustee, or any similar fiduciary capacity only for those with whom they have a personal relationship, unless the personal relationship developed in the context of a Wells Fargo customer relationship.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6179161071777344, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_130(rag_engine):
    """Test retrieval for query: Wells Fargo employee personal finance compliance laws."""
    query = 'Wells Fargo employee personal finance compliance laws.'
    expected_chunk = 'unless the personal relationship developed in the context of a Wells Fargo customer relationship.   Personal finances, borrowing, and lending   Wells Fargo expects all employees to handle their personal finances in compliance with laws and regulations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7553386688232422, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_131(rag_engine):
    """Test retrieval for query: Conflict of interest transactions for personal relationships"""
    query = 'Conflict of interest transactions for personal relationships'
    expected_chunk = 'To avoid a conflict of interest employees must not:   • Process transactions for themselves or anyone with whom they have a personal relationship, except for certain permitted brokerage transactions.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.613196849822998, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.61s"


def test_retrieval_132(rag_engine):
    """Test retrieval for query: Wells Fargo repossessed property purchase policy"""
    query = 'Wells Fargo repossessed property purchase policy'
    expected_chunk = '• Purchase real or personal property that Wells Fargo has repossessed or foreclosed or is marketing at its direction.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6214451789855957, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_133(rag_engine):
    """Test retrieval for query: Borrowing funds from employees or customers conflict of interest"""
    query = 'Borrowing funds from employees or customers conflict of interest'
    expected_chunk = '• Borrow or lend personal funds to employees, customers, or third parties when it creates an actual, potential, or perceived conflict of interest.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6231207847595215, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_134(rag_engine):
    """Test retrieval for query: Investing in customers or third parties without pre-clearance approval."""
    query = 'Investing in customers or third parties without pre-clearance approval.'
    expected_chunk = '• Invest in customers or third parties of Wells Fargo beyond permitted circumstances and without obtaining pre-clearance approval, when required.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6529345512390137, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_135(rag_engine):
    """Test retrieval for query: Who is subject to regulatory credit extension provisions?"""
    query = 'Who is subject to regulatory credit extension provisions?'
    expected_chunk = 'The Board, executive officers, and certain other employees expressly identified and notified by our General Counsel, or the Corporate Secretary, are subject to regulatory provisions related to extension of credit from Wells Fargo and its subsidiaries.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7330045700073242, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_136(rag_engine):
    """Test retrieval for query: Business practices compliance Wells Fargo standards"""
    query = 'Business practices compliance Wells Fargo standards'
    expected_chunk = 'Fair and honest business dealings   Wells Fargo is committed to engaging in fair and honest business practices and being a responsible provider of credit in all our markets.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7538223266601562, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.75s"


def test_retrieval_137(rag_engine):
    """Test retrieval for query: Fair lending and sales practices expectations for employees."""
    query = 'Fair lending and sales practices expectations for employees.'
    expected_chunk = 'Employees and the Board are expected to deal fairly with Wells Fargo’s customers, suppliers, competitors, and employees, and engage in responsible lending and permissible sales practices.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.775710105895996, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.78s"


def test_retrieval_138(rag_engine):
    """Test retrieval for query: Wells Fargo consumer fairness principles guidelines"""
    query = 'Wells Fargo consumer fairness principles guidelines'
    expected_chunk = 'Wells Fargo’s Treating Consumers Fairly Principles are standards to guide employee interactions with our customers and help ensure that consumer fairness considerations are central to the decisions we make about our products and services.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8040223121643066, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.80s"


def test_retrieval_140(rag_engine):
    """Test retrieval for query: Prohibited discriminatory practices in the code of conduct."""
    query = 'Prohibited discriminatory practices in the code of conduct.'
    expected_chunk = '• Discriminating on the basis of race, ethnicity, age, gender, or other protected characteristics.   • Engaging in unfair, deceptive, abusive, misleading, or fraudulent practices.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7098841667175293, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_141(rag_engine):
    """Test retrieval for query: Employee trading restrictions and insider trading policies."""
    query = 'Employee trading restrictions and insider trading policies.'
    expected_chunk = '• Engaging in unfair, deceptive, abusive, misleading, or fraudulent practices.   Insider trading and other trading restrictions   Employees must never buy, sell,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6307315826416016, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_142(rag_engine):
    """Test retrieval for query: Trading securities with material nonpublic information."""
    query = 'Trading securities with material nonpublic information.'
    expected_chunk = 'Insider trading and other trading restrictions   Employees must never buy, sell, or otherwise transact in securities when they have material nonpublic information (MNPI) about the issuer of the securities,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6402101516723633, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_145(rag_engine):
    """Test retrieval for query: What are employee trading policies and restrictions?"""
    query = 'What are employee trading policies and restrictions?'
    expected_chunk = 'Employees must:   • Understand and follow any trading policies, firewall, and other restrictions that apply to them and their business.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6315674781799316, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_146(rag_engine):
    """Test retrieval for query: Reporting MNPI to Global Compliance Control Group"""
    query = 'Reporting MNPI to Global Compliance Control Group'
    expected_chunk = '• Report to the Global Compliance Control Group as soon as possible the receipt of any MNPI about customers or third parties.   • Report to the Global Compliance Control Group any inadvertent disclosure or receipt of MNPI.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7952189445495605, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.80s"


def test_retrieval_147(rag_engine):
    """Test retrieval for query: Wells Fargo securities trading restrictions for employees."""
    query = 'Wells Fargo securities trading restrictions for employees.'
    expected_chunk = '• Report to the Global Compliance Control Group any inadvertent disclosure or receipt of MNPI.   Employees and the Board are prohibited from engaging in derivative or hedging transactions involving any company securities, including Wells Fargo common stock.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7559847831726074, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_148(rag_engine):
    """Test retrieval for query: Derivatives hedging prohibited in employee transactions"""
    query = 'Derivatives hedging prohibited in employee transactions'
    expected_chunk = 'This hedging prohibition applies to any type of transaction in securities that limits investment risk through the use of derivatives, such as options, puts, calls, futures contracts, or other similar instruments.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7375469207763672, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_149(rag_engine):
    """Test retrieval for query: Quarterly black-out periods for company securities employees"""
    query = 'Quarterly black-out periods for company securities employees'
    expected_chunk = 'The Board, executive officers, and certain other employees expressly identified and notified by the Personal Account Dealing Team in coordination with the Legal Department are subject to quarterly black-out or freeze periods involving company securities.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6384143829345703, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_150(rag_engine):
    """Test retrieval for query: Trading plans and U.S. securities law requirements"""
    query = 'Trading plans and U.S. securities law requirements'
    expected_chunk = 'Certain transactions that comply with applicable securities laws may be subject to specific exceptions from these requirements, including transactions under a trading plan that complies with U.S. securities law requirements. In addition to complying with U.S.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.636009693145752, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_151(rag_engine):
    """Test retrieval for query: Wells Fargo securities law preapproval requirements"""
    query = 'Wells Fargo securities law preapproval requirements'
    expected_chunk = 'securities law requirements. In addition to complying with U.S. securities laws, a trading plan must be preapproved by Wells Fargo’s General Counsel or Corporate Secretary.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7445197105407715, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_152(rag_engine):
    """Test retrieval for query: What is Wells Fargo\'s policy on bribery and corruption?"""
    query = 'What is Wells Fargo\'s policy on bribery and corruption?'
    expected_chunk = '> 13 of 19 Code of Conduct > TOC  Decision making  Speak Up Introduction  Do what is right  Closing  Anti-bribery and anti-corruption   Wells Fargo does not tolerate bribery or corruption in any form.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7087163925170898, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_153(rag_engine):
    """Test retrieval for query: bribes prohibited in the workplace"""
    query = 'bribes prohibited in the workplace'
    expected_chunk = 'Such conduct is against the law and the company prohibits it. Further, employees are prohibited from offering, accepting, or utilizing third parties to facilitate bribes.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.653005599975586, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_154(rag_engine):
    """Test retrieval for query: Reporting suspected bribery or corruption policy"""
    query = 'Reporting suspected bribery or corruption policy'
    expected_chunk = 'Further, employees are prohibited from offering, accepting, or utilizing third parties to facilitate bribes.   Employees must:   • Report suspected bribery or corruption in accordance with the Anti-Bribery and Corruption Policy.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.611905574798584, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.61s"


def test_retrieval_157(rag_engine):
    """Test retrieval for query: antitrust laws employee behavior restrictions"""
    query = 'antitrust laws employee behavior restrictions'
    expected_chunk = 'To comply with antitrust and competition laws, employees must not engage in anticompetitive behavior including:   • Agreeing with competitors to price fix, rig bids, allocate customers or territories, or restrict supply.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6307268142700195, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_158(rag_engine):
    """Test retrieval for query: Anti competitive business practices with competitors"""
    query = 'Anti competitive business practices with competitors'
    expected_chunk = '• Exchanging non-public, sensitive information with competitors outside of approved collaborations or activities.   • Colluding with competitors to boycott certain customers, suppliers, or other third parties.   • Abusing a position of market dominance.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6352324485778809, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_159(rag_engine):
    """Test retrieval for query: Anti-competitive agreements with other companies."""
    query = 'Anti-competitive agreements with other companies.'
    expected_chunk = '• Abusing a position of market dominance.   • Agreeing with another company not to hire or solicit each other’s employees or to restrict the terms of employee compensation.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6209039688110352, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_160(rag_engine):
    """Test retrieval for query: Escalating anticompetitive discussions with customers."""
    query = 'Escalating anticompetitive discussions with customers.'
    expected_chunk = 'If a competitor, customer, or third-party attempts to engage an employee in an anticompetitive discussion, that employee must stop the discussion and promptly escalate the matter according to the Anticompetitive Behavior Policy.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6539239883422852, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_162(rag_engine):
    """Test retrieval for query: Compliance with international trade and tax laws."""
    query = 'Compliance with international trade and tax laws.'
    expected_chunk = 'sanctions, trade, and tax laws and regulations.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6643767356872559, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_163(rag_engine):
    """Test retrieval for query: Wells Fargo money laundering responsibilities globally."""
    query = 'Wells Fargo money laundering responsibilities globally.'
    expected_chunk = 'sanctions, trade, and tax laws and regulations.   Financial crimes and money laundering   As a global financial institution, Wells Fargo has important responsibilities to help combat money laundering and other financial crimes including tax evasion, terrorist financing, identity theft, bribery, corruption, sanctions evasion, and fraud.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6856155395507812, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.69s"


def test_retrieval_164(rag_engine):
    """Test retrieval for query: Compliance with global anti-money laundering regulations."""
    query = 'Compliance with global anti-money laundering regulations.'
    expected_chunk = 'We are committed to complying with all applicable global laws and regulations related to anti-money laundering, sanctions, countering the financing of terrorism, bribery, and corruption, and following applicable tax rules.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6369729042053223, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_165(rag_engine):
    """Test retrieval for query: Financial crimes due diligence requirements for employees."""
    query = 'Financial crimes due diligence requirements for employees.'
    expected_chunk = 'Employees must:   • Complete all financial crimes-related due diligence and know your customer requirements.   • Be alert to—and report—any unusual activity according to applicable procedures.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7450547218322754, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.75s"


def test_retrieval_166(rag_engine):
    """Test retrieval for query: tax evasion reporting procedures"""
    query = 'tax evasion reporting procedures'
    expected_chunk = '• Be alert to—and report—any unusual activity according to applicable procedures.   • Avoid knowingly assisting in any form of tax evasion, including providing advice on how to avoid tax obligations.   Sanctions, embargos,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7946858406066895, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.79s"


def test_retrieval_167(rag_engine):
    """Test retrieval for query: Countries we are prohibited from doing business with"""
    query = 'Countries we are prohibited from doing business with'
    expected_chunk = 'Sanctions, embargos, and antiboycott   Wells Fargo is committed to following applicable sanctions, trade and tax laws, and regulations that prohibit the company from doing business with certain countries, groups, or individuals,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7223901748657227, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.72s"


def test_retrieval_168(rag_engine):
    """Test retrieval for query: prohibited business countries and groups associated with terrorism"""
    query = 'prohibited business countries and groups associated with terrorism'
    expected_chunk = 'and regulations that prohibit the company from doing business with certain countries, groups, or individuals, including those associated with terrorism, narcotics trafficking, or nuclear weapons proliferation.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.676832675933838, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_169(rag_engine):
    """Test retrieval for query: Compliance with sanctions and antiboycott laws globally."""
    query = 'Compliance with sanctions and antiboycott laws globally.'
    expected_chunk = 'groups, or individuals, including those associated with terrorism, narcotics trafficking, or nuclear weapons proliferation. We do this by establishing and maintaining policies and procedures that are reasonably designed to comply with sanctions, antiboycott laws, and regulatory guidance in jurisdictions in which we operate.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6451263427734375, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_170(rag_engine):
    """Test retrieval for query: International boycott cooperation policy antiboycott laws"""
    query = 'International boycott cooperation policy antiboycott laws'
    expected_chunk = 'The company does not cooperate with unsanctioned international boycott requests or actions taken to evade antiboycott laws.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6295228004455566, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_173(rag_engine):
    """Test retrieval for query: Protecting company assets from theft and misuse."""
    query = 'Protecting company assets from theft and misuse.'
    expected_chunk = 'This includes protecting the company’s reputation by identifying and mitigating potential risks.   Employee responsibilities include:   • Protecting company assets under their control from theft, waste, misuse, loss, and damage.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6762738227844238, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_174(rag_engine):
    """Test retrieval for query: securing company devices while working remotely"""
    query = 'securing company devices while working remotely'
    expected_chunk = '• Keeping company-owned laptops, mobile devices, and digital storage media safe and secure whether in the office, working remotely, or traveling.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7624759674072266, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_175(rag_engine):
    """Test retrieval for query: Wells Fargo asset use for business purposes"""
    query = 'Wells Fargo asset use for business purposes'
    expected_chunk = '• Using Wells Fargo assets and the company name, logo, and trademarks only for legitimate Wells Fargo business purposes.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.8379030227661133, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.84s"


def test_retrieval_176(rag_engine):
    """Test retrieval for query: personal use of company devices policy"""
    query = 'personal use of company devices policy'
    expected_chunk = 'Limited personal use of company-owned phones, computers, electronics, and company networks is allowed, but good judgment must be used to ensure that personal use does not interfere with the work environment or in any way violate our policies or security requirements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6413469314575195, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_177(rag_engine):
    """Test retrieval for query: Corporate card usage for business expenses only"""
    query = 'Corporate card usage for business expenses only'
    expected_chunk = '• Using their corporate card in a responsible manner and only for business-related expenses.   Employees are not permitted to:   • Allow unauthorized persons to use Wells Fargo equipment or access Wells Fargo facilities.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7427945137023926, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_178(rag_engine):
    """Test retrieval for query: Information security responsibilities at Wells Fargo."""
    query = 'Information security responsibilities at Wells Fargo.'
    expected_chunk = '• Sell, lend, or donate company assets without the appropriate approval.   Information security and electronic communications   Wells Fargo employees and the Board have responsibilities to keep Wells Fargo information safe and secure.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6738815307617188, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_179(rag_engine):
    """Test retrieval for query: Protecting employee credentials and personal identification numbers."""
    query = 'Protecting employee credentials and personal identification numbers.'
    expected_chunk = 'This includes information about Wells Fargo, consumers, customers, employees, our third parties, and legal or regulatory matters.   Employee responsibilities include:   • Safeguard and protect credentials including user identification numbers, passwords, and personal identification numbers.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6742887496948242, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_180(rag_engine):
    """Test retrieval for query: Protecting customer personal data confidentiality"""
    query = 'Protecting customer personal data confidentiality'
    expected_chunk = '• Secure and maintain the confidentiality of Wells Fargo information and use only for legitimate business purposes. Did you know?   • Protect Personally Identifiable Information and The concept of Confidential Supervisory   personal data of consumers, customers,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6493124961853027, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_183(rag_engine):
    """Test retrieval for query: Protecting confidential supervisory information owned by regulators."""
    query = 'Protecting confidential supervisory information owned by regulators.'
    expected_chunk = 'attempts. CSI is the property of federal banking regulators,   • Protect confidential supervisory information (CSI). even if the CSI is in the possession of Wells   • Preserve the confidentiality of Wells Fargo attorney- Fargo.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6656618118286133, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.67s"


def test_retrieval_184(rag_engine):
    """Test retrieval for query: Reporting compromised client data to Compromised Data team."""
    query = 'Reporting compromised client data to Compromised Data team.'
    expected_chunk = 'client privileged or work product protected information.   • Identify and report possible compromised data incidents to Compromised Data.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7570805549621582, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_185(rag_engine):
    """Test retrieval for query: Protecting company intellectual property guidelines"""
    query = 'Protecting company intellectual property guidelines'
    expected_chunk = '• Identify and report possible compromised data incidents to Compromised Data.   > 16 of 19 Code of Conduct > TOC  Decision making  Speak Up Introduction  Do what is right  Closing  Intellectual property   Employees must protect and use appropriately intellectual property,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7383432388305664, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.74s"


def test_retrieval_186(rag_engine):
    """Test retrieval for query: Wells Fargo intellectual property disclosure requirements"""
    query = 'Wells Fargo intellectual property disclosure requirements'
    expected_chunk = 'including patents, copyright, trademarks, and trade secrets. All intellectual property that is developed while working for Wells Fargo must be disclosed to Wells Fargo and it cannot be used externally or published without written permission.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.70158052444458, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_187(rag_engine):
    """Test retrieval for query: Using proprietary information from previous employer."""
    query = 'Using proprietary information from previous employer.'
    expected_chunk = 'Employee responsibilities include:   Did you know? • Not using proprietary information acquired while working at another company, and not pressuring Employee social media guidelines include:   other employees to do so.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6539254188537598, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_188(rag_engine):
    """Test retrieval for query: Wells Fargo proprietary information confidentiality after leaving."""
    query = 'Wells Fargo proprietary information confidentiality after leaving.'
    expected_chunk = '• Avoid posting anything obscene, threatening,   • Not disclosing or using Wells Fargo proprietary harassing, discriminatory, abusive, or disparaging   information after leaving the company. to customers or employees.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7256317138671875, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_189(rag_engine):
    """Test retrieval for query: What information is considered confidential at Wells Fargo?"""
    query = 'What information is considered confidential at Wells Fargo?'
    expected_chunk = 'to customers or employees.   • Not sharing internal use, confidential, or restricted information.   • Maintain the confidentiality of Wells Fargo trade secrets and confidential information.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7626681327819824, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_190(rag_engine):
    """Test retrieval for query: accounting standards for employees at Wells Fargo"""
    query = 'accounting standards for employees at Wells Fargo'
    expected_chunk = '• Maintain the confidentiality of Wells Fargo trade secrets and confidential information.   Accurate records and disclosures   Wells Fargo and its employees must follow applicable accounting standards, policies, procedures, internal controls, and legal requirements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.640732765197754, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_191(rag_engine):
    """Test retrieval for query: Maintaining accurate data in employee responsibilities."""
    query = 'Maintaining accurate data in employee responsibilities.'
    expected_chunk = 'The company is committed to accurate, timely, and clear disclosures to regulatory authorities, customers, shareholders, and the public.   Employee responsibilities include:   • Never falsifying data or information.   • Maintaining accurate data or information.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6799397468566895, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.68s"


def test_retrieval_192(rag_engine):
    """Test retrieval for query: Recording payments to third parties accurately."""
    query = 'Recording payments to third parties accurately.'
    expected_chunk = '• Maintaining accurate data or information.   • Accurately recording all payments to, and business transactions with, or conducted by third parties.   • Timely reporting of an error in any of our books or records.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.733776569366455, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.73s"


def test_retrieval_193(rag_engine):
    """Test retrieval for query: Reporting errors in company books or records."""
    query = 'Reporting errors in company books or records.'
    expected_chunk = '• Timely reporting of an error in any of our books or records.   • Obtaining proper authorization or consent for, and never falsifying or improperly altering, legal documents, company forms, applications, or agreements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.778916835784912, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.78s"


def test_retrieval_194(rag_engine):
    """Test retrieval for query: Signing blank or incomplete documents by customers or vendors"""
    query = 'Signing blank or incomplete documents by customers or vendors'
    expected_chunk = '• Never signing a blank or incomplete document or asking a customer or vendor to do so.   • Following records retention guidelines and complying with legal hold notices as appropriate.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 2.1104049682617188, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 2.11s"


def test_retrieval_195(rag_engine):
    """Test retrieval for query: compliance with legal hold notices and expense approval policies"""
    query = 'compliance with legal hold notices and expense approval policies'
    expected_chunk = '• Following records retention guidelines and complying with legal hold notices as appropriate.   • Processing all expenses accurately, timely, and through required channels; reviewing expenses for adherence to policies; and ensuring approvals are provided by someone with the proper authority.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.653576374053955, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_196(rag_engine):
    """Test retrieval for query: Reporting government agency requests to Regulatory Relations."""
    query = 'Reporting government agency requests to Regulatory Relations.'
    expected_chunk = '• Notifying Regulatory Relations as appropriate of any government or regulatory agency requests.   > 17 of 19 Code of Conduct > TOC  Decision making  Speak Up Introduction  Do what is right  Closing TOC  Decision making  Speak'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.633084774017334, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_198(rag_engine):
    """Test retrieval for query: Workplace harassment and discrimination policies Wells Fargo"""
    query = 'Workplace harassment and discrimination policies Wells Fargo'
    expected_chunk = 'Resources  # Our workplace   # Anti-harassment and anti-discrimination   Wells Fargo is dedicated to providing a workplace free from harassment and discrimination based on an individual’s race, ethnicity, age, gender, or other protected characteristics.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6423559188842773, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_199(rag_engine):
    """Test retrieval for query: Prohibited behaviors on company property and communication systems."""
    query = 'Prohibited behaviors on company property and communication systems.'
    expected_chunk = 'discrimination based on an individual’s race, ethnicity, age, gender, or other protected characteristics. This includes, but is not limited to, on company property or company communication systems, during remote work or business travel, at company-sponsored events, or otherwise in connection with company business.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6641969680786133, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_200(rag_engine):
    """Test retrieval for query: Wells Fargo policy on workplace harassment and discrimination."""
    query = 'Wells Fargo policy on workplace harassment and discrimination.'
    expected_chunk = 'Any such harassment or discrimination is against Wells Fargo policy, may violate the law, and will not be tolerated.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6514558792114258, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_201(rag_engine):
    """Test retrieval for query: Reporting harassment or discrimination in the workplace"""
    query = 'Reporting harassment or discrimination in the workplace'
    expected_chunk = 'In the event of harassment or discrimination, employees are required to promptly report it using a reporting channel described in the Resources to report potential misconduct section.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6998071670532227, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.70s"


def test_retrieval_202(rag_engine):
    """Test retrieval for query: Career advancement opportunities at Wells Fargo."""
    query = 'Career advancement opportunities at Wells Fargo.'
    expected_chunk = 'Hiring and advancement opportunities   At Wells Fargo, we strive to provide advancement opportunities for our employees.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6161818504333496, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.62s"


def test_retrieval_206(rag_engine):
    """Test retrieval for query: Workplace safety policy on substance use."""
    query = 'Workplace safety policy on substance use.'
    expected_chunk = '# Workplace safety   Wells Fargo is dedicated to maintaining a safe work environment.   All employees are required to perform their job duties unimpaired by illegal drugs, alcohol, or by the improper use of legal substances.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6255321502685547, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_207(rag_engine):
    """Test retrieval for query: violence in the workplace policy"""
    query = 'violence in the workplace policy'
    expected_chunk = 'Under no circumstances will the company tolerate physical violence or threats. To support a violence-free workplace our employees are not permitted to carry, either openly or in a concealed manner,'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7118034362792969, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.71s"


def test_retrieval_208(rag_engine):
    """Test retrieval for query: Company employees allowed to carry firearms on premises."""
    query = 'Company employees allowed to carry firearms on premises.'
    expected_chunk = 'either openly or in a concealed manner, any weapon (such as a knife or firearm) while on company premises or at company-sponsored events unless they are company-authorized security personnel.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6587486267089844, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.66s"


def test_retrieval_209(rag_engine):
    """Test retrieval for query: Reporting workplace violence safety concerns"""
    query = 'Reporting workplace violence safety concerns'
    expected_chunk = 'Any perceived threats of workplace violence and safety concerns should be reported immediately through the appropriate channel described in the Reporting safety concerns section.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6488499641418457, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"


def test_retrieval_210(rag_engine):
    """Test retrieval for query: Wells Fargo human rights commitment statement"""
    query = 'Wells Fargo human rights commitment statement'
    expected_chunk = '# Valuing human rights   At Wells Fargo, we recognize the responsibility — and opportunity — we have to make a positive impact on society. Wells Fargo is committed to respecting human rights throughout our operations, products, and services.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.7632832527160645, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.76s"


def test_retrieval_213(rag_engine):
    """Test retrieval for query: Reporting human rights abuses in operations or with customers"""
    query = 'Reporting human rights abuses in operations or with customers'
    expected_chunk = '• Support efforts to help prevent human rights abuses including modern slavery and human trafficking.   • Report any suspicion or instance of human rights abuses in our operations or related to any specific customer, investment activity, or the operations of our suppliers.   >'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.806149959564209, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.81s"


def test_retrieval_217(rag_engine):
    """Test retrieval for query: Waivers to Code for executive officers disclosure requirements."""
    query = 'Waivers to Code for executive officers disclosure requirements.'
    expected_chunk = '# Waivers and exceptions   Any waivers or exceptions to the Code for executive officers or the Board may only be made by the Board or designated Board committee and will be promptly disclosed to our shareholders in accordance with legal and regulatory requirements.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6428747177124023, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.64s"


def test_retrieval_218(rag_engine):
    """Test retrieval for query: What are consequences for violating employee code of conduct?"""
    query = 'What are consequences for violating employee code of conduct?'
    expected_chunk = '# Violations   Any violation of the provisions of the Code or the referenced policies and guidelines is grounds for corrective action, which may include termination of employment.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6295833587646484, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.63s"


def test_retrieval_219(rag_engine):
    """Test retrieval for query: What are consequences of violating employee code of conduct?"""
    query = 'What are consequences of violating employee code of conduct?'
    expected_chunk = 'Certain violations may also result in legal proceedings, including prosecution for criminal violations, impacts to the employee’s licensing, and financial industry employment eligibility.'

    # Time the retrieval
    start_time = time.time()
    results = rag_engine.retrieve(query)
    retrieval_time = time.time() - start_time

    # Convert results to text for comparison
    retrieved_texts = [node.text for node in results]

    # Normalize texts for comparison
    normalized_expected = normalize_text(expected_chunk)
    normalized_retrieved = [normalize_text(text) for text in retrieved_texts]

    # Assert the expected chunk is in the results
    assert any(normalized_expected in text for text in normalized_retrieved), \
        f"Expected chunk not found in retrieval results"

    # Assert retrieval time is within acceptable range (2x baseline)
    assert retrieval_time < 1.6465997695922852, \
        f"Retrieval took too long: {retrieval_time:.2f}s > 1.65s"

