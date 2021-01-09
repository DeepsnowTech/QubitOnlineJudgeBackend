import os
import subprocess
SPJ_WA = 1
SPJ_AC = 0
SPJ_ERROR = -1
PY_SPJ_HOME = "/code/ProblemCenter/PythonSPJ/"


def py_spj_run(spj_src_path, test_in_file_path, user_out_file_path):
    problem_id = get_problem_id(spj_src_path)
    return _py_spj_run(problem_id, test_in_file_path, user_out_file_path)


def _py_spj_run(problem_id, test_in_file_path, user_out_file_path):

    cmd_list = ["python3", PY_SPJ_HOME +
                str(problem_id)+".py", test_in_file_path, user_out_file_path]

    """
    with open("/code/py_spj_log", "a") as f:
        print("in_file",test_in_file_path,file=f)
        print("user_output",user_out_file_path,file=f)
        print("problem_id",problem_id,file=f)
        print("cmd"," ".join(cmd_list),file=f)
    """
    
    

    try:
        spj_program_path = PY_SPJ_HOME+str(problem_id)+".py"
        p_handler = subprocess.Popen(["python3",spj_program_path, test_in_file_path, user_out_file_path])
        p_handler.wait()

        if p_handler.returncode in [SPJ_WA, SPJ_AC, SPJ_ERROR]:
            return p_handler.returncode
        else:
            return SPJ_ERROR
    except Exception as e:
        print(e)
        return SPJ_ERROR


def get_problem_id(spj_src_path):
    with open(spj_src_path, "r") as f:
        line = f.readline()
    line = line.replace("/", "")
    line = line.replace("\n", "")
    return line


if __name__ == "__main__":
    _py_spj_run(1001, "/code/ProblemCenter/PythonSPJ/test.in", "/code/ProblemCenter/PythonSPJ/cmd.txt")
