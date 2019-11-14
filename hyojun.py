import math
import nni
def run_trial(params):
    objective = math.sin(params["x"]) + params["x"]**2 + math.sin(params["y"]) + params["y"]**2 
    nni.report_final_result(objective)

if __name__ == '__main__':
    params = nni.get_next_parameter()
    run_trial(params)