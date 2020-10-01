from factory.fuzzy import BaseFuzzyAttribute, FuzzyInteger


class FuzzyPhoneNumber(BaseFuzzyAttribute):
    def fuzz(self):
        return "+88" + str(FuzzyInteger(low=10000000000, high=99999999999).fuzz())
