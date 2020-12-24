from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8' )
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')



indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs =indeed_jobs + so_jobs
save_to_file(jobs)
