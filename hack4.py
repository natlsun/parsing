#4 dolar
def float(dolarize()):
    dollarize(123456.78901) -> "$123,456.80"
    dollarize(-123456.7801) -> "-$123,456.78"
    dollarize(1000000) -> "$1,000,000"
class MoneyFmt:
    def __init__(self, dolarize):
        