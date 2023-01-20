from common.methods import set_progress


def run(job, *args, **kwargs):
    parameters = job.job_parameters.cast()
    for server in parameters.servers.all():
        set_progress(f"Powering off {server.hostname}")
        server.power_off()
        
    return "SUCCESS", "", ""
