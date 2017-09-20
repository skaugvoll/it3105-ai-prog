import itertools


class NonogramVariable():
    def __init__(self, type, length, variable):
        self.type = type
        self.lenght = length
        self.variable = variable
        self.domain = self.generate_domain(length, variable)
        self.common = {}
        self.findCommon()

    def __repr__(self):
        # return str(self.variable) + "Domain: " + str(self.domain)
        return str(self.variable) + " Common: " + str(self.common) + "\nLen:" + str(len(self.domain)) + " Domain: " + str(self.domain) +"\n"

    def setValues(self, values):
        self.values = values

    def getValues(self):
        return self.values


    def generate_domain(self, length, variable):
        # generate minimum placement
        domain = []
        min_placement = []
        for s in variable:
            for i in range(s):
                min_placement.append(1)
            min_placement.append(0)
        min_placement.pop(len(min_placement) - 1)

        insert_indices = [i + 1 for i, x in enumerate(min_placement) if x == 0]
        insert_indices.extend([0, len(min_placement)])
        combinations = itertools.combinations_with_replacement(insert_indices, length - len(min_placement))
        for c in combinations:
            result = min_placement[:]
            insert_positions = list(c)
            insert_positions.sort()
            offset = 0
            for index in insert_positions:
                result.insert(index + offset, 0)
                offset += 1
            domain.append(result)
        return domain


    def findCommon(self):
        self.common = {}
        index = 0
        checkValue = None
        while index < self.lenght:
            checkValue = self.domain[0][index]
            for list in self.domain:
                valid = True
                if list[index] != checkValue :
                    valid = False
                    break
            if valid:
                self.common[index] = checkValue
            index += 1


    def setDomain(self, domain):
        self.domain = domain