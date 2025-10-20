import requests

def click_link(link):
    """Visit a link and return the result."""
    try:
        response = requests.get(link)
        if response.status_code == 200:
            return f"Successfully visited {link}"
        else:
            return f"Failed to visit {link}. Error code: {response.status_code}"
    except Exception as e:
        return f"Error with {link}. Error: {e}"

def visit_links(file_name, domains_to_visit=None):
    """Visit links from a file, optionally filtered by a list of domains."""
    results = []
    with open(file_name, 'r') as urls_file:
        for line in urls_file:
            line = line.strip()
            if domains_to_visit:
                for domain in domains_to_visit:
                    if domain in line:
                        result = click_link(line)
                        results.append(result)
                        break
            else:
                result = click_link(line)
                results.append(result)

    # Save the results to a file
    with open("visited_links.txt", "w") as visited_file:
        for result in results:
            visited_file.write(result + "\n")

    return results