import argparse
from .googlenews import GoogleNews

def main():
    parser = argparse.ArgumentParser(description='PyNews-Google CLI')
    parser.add_argument('action', choices=['top', 'topic', 'search'], help='Action to perform')
    parser.add_argument('--topic', help='Topic for headlines')
    parser.add_argument('--query', help='Search query')
    parser.add_argument('--lang', default='en', help='Language (default: en)')
    parser.add_argument('--country', default='US', help='Country (default: US)')
    args = parser.parse_args()

    news = GoogleNews(lang=args.lang, country=args.country)

    if args.action == 'top':
        result = news.top_news()
    elif args.action == 'topic':
        if not args.topic:
            parser.error("--topic is required when action is 'topic'")
        result = news.topic_headlines(args.topic)
    elif args.action == 'search':
        if not args.query:
            parser.error("--query is required when action is 'search'")
        result = news.search(args.query)

    for entry in result['entries']:
        print(f"Title: {entry['title']}")
        print(f"Link: {entry['link']}")
        print(f"Published: {entry['published']}")
        print("---")

if __name__ == '__main__':
    main()