from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result != None:
                    return result
                assignment.pop(var)
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    cr, pa, co, ve, gu, su, gufr, ec, pe, br, bo, para, ch, ar, ur = "CR", "PA", "CO", "VE", "GU", "SU", "GUFR", "EC", "PE", "BR", "BO", "PARA", "CH", "AR", "UR"
    values = ['Red', 'Green', 'Blue', "YELLOW"]
    variables = [cr, pa, co, ve, gu, su, gufr, ec, pe, br, bo, para, ch, ar, ur]
    domains = {
        cr: values[:],
        pa: values[:],
        co: values[:],
        ve: values[:],
        gu: values[:],
        su: values[:],
        gufr: values[:],
        ec: values[:],
        pe: values[:],
        br: values[:],
        bo: values[:],
        para: values[:],
        ch: values[:],
        ar: values[:],
        ur: values[:]
    }
    neighbours = {
        cr: [pa],
        pa: [cr, co],
        co: [ec, pe, br, ve],
        ve: [co, br, gu],
        gu: [ve, br, su],
        su: [gu, br, gufr],
        gufr: [su, br],
        ec: [pe, co],
        pe: [ch, bo, br, co, ec],
        br: [gufr, su, gu, ve, co, pe, bo, para, ar, ur],
        bo: [pe, br, para, ar, ch],
        para: [bo, br, ur, ar, ch],
        ch: [pe, bo, ar],
        ar: [ch, bo, para, br, ur],
        ur: [br, ar]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        pa: constraint_function,
        co: constraint_function,
        ve: constraint_function,
        gu: constraint_function,
        su: constraint_function,
        gufr: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        br: constraint_function,
        bo: constraint_function,
        para: constraint_function,
        ch: constraint_function,
        ar: constraint_function,
        ur: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_australia_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
