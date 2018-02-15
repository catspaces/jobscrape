from urllib.parse import urlparse

def generate_urls(path="lever_sites.csv"):
    """ 
    generate_urls : str -> [urlparseresult] 
  
    Return a list of urlparse results. 
    """
    file = open(path, "r")
    urls_str = file.read()
    urls = urls_str.split(",") 
    return [urlparse(url) for url in urls]

def probably_uuid4(test_str):
    """
    probably_uuid4 : str -> boolean
    Lever uses uuid4s for job links
    Utility function for filtering bunk results from lever links and extracting the company root. 
    Uses the heuristic that a str is probably a uuid4 if it has 32 or 36 chars. 
    """
    return len(test_str) == 32 or len(test_str) == 36
    
def construct_endpoint_set(parse_results):
    """
    select_endpoints : [urlparseresult] -> set(string)
    lever URLs are of the form jobs.lever.co/COMPANY 
    Takes a list of URLParseResults and attempts to single out the company root path for each item.
    Returns a set of strings. 
    """
    endpoints = []
    for url in parse_results:
        for component in url.path.split("/"):
            stripped_component = component.strip().strip('"')
            if stripped_component in {"https:", "jobs.lever.co", '', "..."} or probably_uuid4(stripped_component): 
                pass
            else:
                endpoint = stripped_component
                endpoints.append(endpoint)
                break
    return set(endpoints)

def construct_link_set(endpoint_set):
    return { "https://jobs.lever.co/" + endpoint for endpoint in endpoint_set }

