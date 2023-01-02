class Value():
    def __init__(self):
        """
        'value' : weight
        -> str : float
        """
        value_dict = {
            '사랑' : 0,
            '돈': 0,
            '전문성' : 0,
            '명예' : 0,
            '안정' : 0,
            '즐거움' : 0,
            '선함' : 0,
            '도덕' : 0,
            '배려' : 0,
            '자유' : 0,
            '발전' : 0,
            '완벽' : 0,
            '시간' : 0,
            '도전' : 0,
            '책임' : 0,
            '현재' : 0,
            '미래' : 0,
            '쾌락' : 0,
            '승리' : 0,
            '편안함' : 0,
            '규칙' : 0,
            '외모' : 0,
            '건강' : 0,
            '가족' : 0,
            '학습' : 0,
            '여행' : 0,
        }

    def get_value_count(self):
        return len(self.value_dict)
    

    def get_value_list(self):
        return list(self.value_dict.keys)
