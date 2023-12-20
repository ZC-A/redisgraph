from multiprocessing import Pool
import subprocess


cmd = ['./redisgraph-benchmark-go -n 100000 -graph-key graph -query "CREATE (u:User)" -a wikiredis 2>&1 | tee mylog.log', './redisgraph-benchmark-go -n 100000 -graph-key graph2 -query "CREATE (u:User)" -a wikiredis 2>&1 | tee mylog2.log']


def run_command(command):
    subprocess.Popen(command, shell=True)


if __name__ == '__main__':
    with Pool(processes=len(cmd)) as pool:
        pool.map(run_command, cmd)
