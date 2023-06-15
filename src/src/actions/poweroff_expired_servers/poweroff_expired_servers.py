from common.methods import set_progress


def run(job, servers, **kwargs):
    for server in servers:
        set_progress(f"Powering off {server.hostname}")
        server.power_off()
        
    return "SUCCESS", "", ""
