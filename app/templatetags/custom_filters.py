from django import template

register = template.Library()

@register.filter
def ensure_absolute_url(url):
    """
    Ensures that a URL is absolute.
    - Prepends http://hdl.handle.net/ if it starts with 'handle/'
    - Prepends https:// if it starts with 'www.'
    - Prepends http:// if it's missing a protocol and doesn't look like a handle
    """
    if not url:
        return ""
    
    url = str(url).strip()
    
    if url.startswith("http://") or url.startswith("https://"):
        return url
    
    if url.startswith("handle/"):
        return f"http://hdl.handle.net/{url}"
        
    if url.startswith("www."):
        return f"https://{url}"
        
    # Default fallback for other incomplete URLs
    return f"http://{url}"
