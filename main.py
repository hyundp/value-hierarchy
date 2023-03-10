from HierarchySystem import HierarchySystem

choice = input("선택지를 설명해주세요")

hierarchy = HierarchySystem()

input_val = hierarchy.set_input_val()
input_time = hierarchy.set_input_time()
result = hierarchy.cal_obj_function(input_val, input_time)

print(f"{choice}의 점수는 \n {result}입니다.")


