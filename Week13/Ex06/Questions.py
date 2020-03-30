'''
1. What is returned by create_australia_csp()?
    it is returning a csp formulation.
2. What is returned by backtracking_search()?
    the solution to the problem - if there is no solution, then a failure, else the "assignment"
3. What is the purpose of assignment variable?
    the assigment variable is containing the current nodes
4. What is the purpose of variable variable?
    The variable variable is the variable, that is currently in the process of being assigned a value
5. What is the purpose of the following statement?
for value in self.order_domain_values(variable, assignment)
    by using the method order_domain_values, one is able to switch up the order of the assigned value,
    meaning that we are able to implement fx. the least constraining value
6. What would the following do?
if self.is_consistent('Q', 'Red', 'NT': 'Blue', 'NSW': 'green'):
assignment[variable] = value
    It checks the given constraints, and if it is upholding all the constraints,
    the variable will be assigned the given value.
7. What would then assignment be?
    {'Q' : 'Red', 'NT': 'Blue', 'NSW': 'green'}
8. What is the effect of del assignment[variable]?
    The output would be the value of the variable
'''