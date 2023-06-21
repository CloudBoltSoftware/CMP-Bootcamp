def should_display(server, **kwargs):
    """
    Only display the patch button if the current server has the proper
    custom field and its value is greater than 0.
    """
    if server.acme_patches_available and server.acme_patches_available > 0:
        return True
    
    return False