### Repository Title
**Inverted Index Search Engine**

---

### README.md

# Inverted Index Search Engine

This repository contains a Python implementation of an Inverted Index Search Engine that allows users to efficiently search across multiple documents. The project leverages Natural Language Processing (NLP) techniques such as stemming, lemmatization, and stopword removal to normalize documents and search queries, improving the accuracy of search results.

## Features

- **Inverted Index Construction:** Automatically creates an inverted index for a set of documents, making it easy to retrieve relevant documents based on query terms.
- **Query Normalization:** Handles stopword removal, stemming, and lemmatization to ensure consistent search results.
- **Document Matching:** Retrieves documents containing all the query terms and calculates precision and recall for the search query.
- **Performance Metrics:** Outputs performance metrics like precision, recall, and the number of retrieved and relevant documents.

## Files in the Repository

- **`main.py`**: The main script that loads documents, builds the inverted index, processes search queries, and outputs the results.
- **`inverted_index.py`**: Contains the `InvIndex` class which handles the creation of the inverted index, query normalization, and document matching logic.
- **Document Files (`D1.txt`, `D2.txt`, `D3.txt`, `D4.txt`)**: Sample text files that are used as the dataset for indexing and search.

## Dependencies

To run the project, make sure you have the following libraries installed:
- `nltk`
- `re`
- `collections`

You can install these libraries using pip:
```bash
pip install nltk
```

Ensure that you have the necessary NLTK data files downloaded:
```bash
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
```

## Usage

1. Place your text files in the repository directory.
2. Run the `main.py` script:
   ```bash
   python main.py
   ```
3. Enter a query when prompted, and the system will retrieve and display the documents that match the query.

## Example

Input Query:
```
Enter Query: home sales in July
```

Output:
```
Match in Doc Exists: [D1.txt, D2.txt]
Precision: 0.5
Recall: 1.0
```

## Future Enhancements

- **Phrase Query Support:** Adding support for phrase queries where users can search for exact sequences of words.
- **Document Ranking:** Implementing a ranking algorithm like TF-IDF to rank the documents based on relevance.
- **Larger Dataset Handling:** Optimize for larger datasets with more advanced indexing techniques.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you need any modifications or further customization for your README!
