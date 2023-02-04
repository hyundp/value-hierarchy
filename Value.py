class Value():
    def __init__(self):
        """
        'value' : weight
        -> str : float
        """
        value_dict = {
            # 그 일은 나에게 어떤 가치를 주는가? (0.5)
            '사랑' : 8,
            '자산': 9,
            '능력' : 10,
            '건강' : 7,
            '안정' : 6,
            '즐거움' : 4,
            '자유' : 5,
            '책임' : 6,
        }

        time_dict = {
            # 그 일은 어떤 시점에 가치를 주는가?
            '현재' : 6,
            '미래' : 10,
        }

    def get_value_count(self):
        return len(self.value_dict)
    

    def get_value_name(self):
        return list(self.value_dict.keys)

    def get_value_dict(self):
        return self.value_dict

    def get_time_dict(self):
        return self.time_dict