import os
import psutil
import resource
import subprocess
import time
GB_MEMORY=1024*1024*1024

def run_command_with_rlimits(command,in_path,out_path,time_limit,memory_limit_GB):
    memory_limit_in_byte=int(2*memory_limit_GB*GB_MEMORY)
    result={'cpu_time': 0, 'real_time': 0, 'memory': 0, 'signal': 0, 'exit_code': 0, 'error': 0, 'result': 0}
    timeDelta=0
    def preexec_fn():
        resource.setrlimit(resource.RLIMIT_CPU, (time_limit, time_limit*2))
        resource.setrlimit(resource.RLIMIT_AS,(memory_limit_in_byte,2*memory_limit_in_byte))
    try:
        stdout=open(out_path,"w")
        stdin=open(in_path,"r")
        timeStarted = time.time() 

        sub_user_cmd="  ".join(command) 
        p = subprocess.Popen(["su", "code", "-c", sub_user_cmd], preexec_fn=preexec_fn,stdout=stdout,stdin=stdin)
        p.wait()
        timeDelta = int((time.time() - timeStarted)*1000)
        #print(timeDelta)
        stdout.close()
        stdin.close()
    except Exception as e:
        return result
    result["cpu_time"]=timeDelta
    result["real_time"]=timeDelta
    return result

if __name__ == "__main__":
    command=['/usr/bin/python3',"/code/Tests/code_runner_test.py"]
    in_path="/code/Tests/in.txt"
    out_path="/code/Tests/out.txt"
    time_limit=100
    memory_limit_GB=10
    result=run_command_with_rlimits(command,in_path,out_path,time_limit,memory_limit_GB)
    print(result)
