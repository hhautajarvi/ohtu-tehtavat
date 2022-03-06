from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, build=All()):
        self.query = build

    def build(self):
        return And(self.query)

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def oneOf(self, *query):
        return QueryBuilder(Or(*query))