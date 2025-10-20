def extract_domain(netloc):
  """Extracts the domain name from a netloc string."""
  parts = netloc.split(".")
  if len(parts) > 1:
    return parts[-2]  # Get the second part from the end (ignoring subdomain)
  else:
    return None  # Invalid format

# Example usage
netloc = "swiftkey-sync-production.touchtype-fluency.com"
domain = extract_domain(netloc)

if domain:
  print(f"Extracted domain: {domain}")
else:
  print("Invalid netloc or could not extract domain.")