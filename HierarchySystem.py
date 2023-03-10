from Value import Value
from UtilityFunction import normal_utility_function

class HierarchySystem():

    def set_input_val(self):
        input_val = []
        value_name_list = Value().get_value_name()
        for value_name in value_name_list:
            input_val.append(int(input(f"선택지가 가치 '{value_name}'을(를) 얼마나 포함하나요? (1~5)")))
        return input_val
    
    def set_input_time(self):
        input_time = []
        future = int(input(f"선택지가 얼마나 미래지향적입니까? (1~5)"))
        input_time.append(future)
        input_time.append(5-future)
        return input_time
        


    def cal_obj_function(self, input_val, input_time): 


        # utility function을 value의 가중치 결과값마다 적용한다. 
        # ex) 10 + 100 > 40 + 50 이지만, sqrt(10) + sqrt(100) < sqrt(40) + sqrt(50) 인것을 보아 
        # utility function을 value마다 적용하면 그 합의 대소관계가 달라질 수 있기 때문에 유의하다. 
        

        val_result = 0 
        time_result = 0 
        value_weight = Value().get_value_weight()
        time_weight = Value().get_time_weight() 
        for i in range(len(value_weight)): 
            val_result += normal_utility_function(value_weight[i]*input_val[i]) 
        for i in range(len(time_weight)): 
            time_result += time_weight[i]*input_time[i] 
        result = val_result * time_result 
        return result 