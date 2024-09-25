# news-google-api

A Python library to fetch and parse Google News feeds.

## Installation

```
pip install news-google-api
```

## Usage

### As a library

```python
from googlenews import GoogleNews

news = GoogleNews()

# Get top news
top_news = news.top_news()

# Get topic headlines
tech_news = news.topic_headlines('TECHNOLOGY')

# Search news
search_results = news.search('Python programming')

# Print results
for entry in top_news['entries']:
    print(f"Title: {entry['title']}")
    print(f"Link: {entry['link']}")
    print(f"Published: {entry['published']}")
    print("---")
```


## Features

- Fetch top news from Google News
- Get headlines for specific topics
- Search for news articles
- Command-line interface for quick access to news

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Amos Maru

## Acknowledgments

- Google News for providing the RSS feeds
- All contributors who help improve this library