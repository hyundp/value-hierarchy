class Value():
    def __init__(self):
        """
        'value' : weight
        -> str : float
        """
        value_dict = {
            '사랑' : 0,
            '자산': 0,
            '능력' : 0,
            '건강' : 0,
            '안정' : 0,
            '즐거움' : 0,
            '자유' : 0,
            '책임' : 0,
            '현재' : 0,
            '미래' : 0,
        }

    def get_value_count(self):
        return len(self.value_dict)
    

    def get_value_name(self):
        return list(self.value_dict.keys)
