
class CSPConstraint():
    def __init__(self, id=None, constraint="x + y > 2 * z", variables=[]):
        self.id = id
        self.constraint = constraint
        self.variables = variables

    def getID(self):
        return self.id

    def getCoonstraint(self):
        return self.constraint

    def setConstraint(self, constraint):
        self.constraint = constraint
