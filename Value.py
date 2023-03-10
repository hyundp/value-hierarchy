class Value():
    def __init__(self):
        """
        'value' : weight
        -> str : float
        """
        self.value_dict = {
            # 그 일은 나에게 어떤 가치를 주는가?
            '사랑' : 3.7,
            '자산': 4.3,
            '능력' : 3.6,
            '건강' : 5.1,
            '안정' : 2.2,
            '즐거움' : 2.4,
            '자유' : 2.7,
            '책임' : 3.6,
        }

        self.time_dict = {
            # 그 일은 어떤 시점에 가치를 주는가?
            '현재' : 3,
            '미래' : 5,
        }

    def get_value_count(self):
        return len(self.value_dict)
    

    def get_value_name(self):
        return list(self.value_dict.keys())
    
    def get_value_weight(self):
        return list(self.value_dict.values())

    def get_value_dict(self):
        return self.value_dict

    def get_time_dict(self):
        return self.time_dict
    
    def get_time_weight(self):
        return list(self.time_dict.values())