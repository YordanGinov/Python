from urllib.parse import urlparse

def read_url_from_file(file_name):
    """Read URLs from a file and yield each line."""
    with open(file_name, 'r') as urls_file:
        for line in urls_file:
            yield line.strip()

def extract_domain_from_netloc(url_string):
    """Extract the domain from a URL's netloc."""
    url_parts = url_string.split('.')
    if len(url_parts) > 1:
        return f"{url_parts[-2]}.{url_parts[-1]}"
    return url_string

def process_urls(file_name):
    """Process URLs from a file and return a sorted list of domains and their counts."""
    urls_dict = {}

    for line in read_url_from_file(file_name):
        parsed_url = urlparse(line)
        if parsed_url.netloc:
            url_string = extract_domain_from_netloc(parsed_url.netloc)
            if url_string not in urls_dict:
                urls_dict[url_string] = 0
            urls_dict[url_string] += 1

    # Sort the dictionary by count in descending order
    return sorted(urls_dict.items(), key=lambda x: x[1], reverse=True)