from multi_worker.content_writer import run_content_writer
from multi_worker.email_writer import run_email_writer_agent
from multi_worker.summary_generator import run_summary_generator
from multi_worker.idea_brainstormer import run_brainstormer_agent  


def Distributed_task(task):
    task_lower = task.lower()

    if "content" in task_lower:
        return run_content_writer
    elif "email" in task_lower:
        return run_email_writer_agent
    elif "summary" in task_lower:
        return run_summary_generator
    elif "idea" in task_lower or "brainstorm" in task_lower:
        return run_brainstormer_agent
    else:
        return None
