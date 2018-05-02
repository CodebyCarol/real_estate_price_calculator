class PriceCalculator:

    AVG_SQM_PRICE = 2500000

    DISTRICT_WEIGHT = {
        1: 1.1,
        2: 1.2,
        3: 1.3,
        4: 1.4,
        5: 1.5,
        6: 1.6,
        7: 1.7,
        8: 1.8,
        9: 1.9,
        10: 1.1
    }



    @classmethod
    def calculate(cls, district, squaremeter):
        if district > 10 or district < 1:
            raise ValueError("no such district")
        if squaremeter < 1:
            raise ValueError("squaremeter should be above 0")
        return cls.AVG_SQM_PRICE * squaremeter * cls.DISTRICT_WEIGHT[district]
        