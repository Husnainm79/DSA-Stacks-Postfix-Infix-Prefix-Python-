
class ArithmeticEngine:
    def compute_expression(self, expression):
        raise NotImplementedError("Subclasses must implement compute_expression method")


class PostfixArithmeticEngine(ArithmeticEngine):
    def compute_expression(self, expression):
        stack = []
        operators = set(['+', '-', '*', '/', '^'])
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                if len(stack) < 2:
                    raise ValueError("Malformed expression")
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    stack.append(operand1 / operand2)
                elif token == '^':
                    stack.append(operand1 ** operand2)
            else:
                raise ValueError("Invalid token: {}".format(token))
        if len(stack) != 1:
            raise ValueError("Malformed expression")
        return stack.pop()


class InfixToPostfixConverter:
    def __init__(self):
        self.precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
        self.operators = set(['+', '-', '*', '/', '^'])

    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        for token in expression.split():
            if token.isdigit():
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError("Mismatched parentheses")
                stack.pop()  # Remove '('
            elif token in self.operators:
                while stack and self.precedence.get(stack[-1], 0) >= self.precedence.get(token, 0):
                    postfix.append(stack.pop())
                stack.append(token)
            else:
                raise ValueError("Invalid token: {}".format(token))
        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            postfix.append(stack.pop())
        return ' '.join(postfix)


class InfixArithmeticEngine(ArithmeticEngine):
    def compute_expression(self, expression):
        converter = InfixToPostfixConverter()
        postfix_expression = converter.infix_to_postfix(expression)
        postfix_evaluator = PostfixArithmeticEngine()
        return postfix_evaluator.compute_expression(postfix_expression)


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def simulate_movie_ticket_booking(N, num_persons):
    queues = [CustomQueue() for _ in range(N)]

    # Enqueue persons into queues
    for queue in queues:
        for i in range(num_persons):
            queue.enqueue("Person {}".format(i))

    ticket_collector_time = 0
    while True:
        all_empty = True
        for i in range(N - 1, -1, -1):
            if not queues[i].is_empty():
                all_empty = False
                person = queues[i].dequeue()
                print("Ticket collector processing:", person)
                ticket_collector_time += 2  # Time taken to process a person
                if i != 0:
                    queues[i - 1].enqueue(person)
        if all_empty:
            break

    print("Total time taken by the ticket collector:", ticket_collector_time)


def evaluate_paper(scores):
    num_reviewers = len(scores)
    num_criteria = len(scores[0])

    # Calculate average score for each reviewer
    reviewer_averages = [sum(scores[i]) / num_criteria for i in range(num_reviewers)]

    # Check rule 1: If any reviewer's average is below 5, reject the paper
   
class ArithmeticEngine:
    def compute_expression(self, expression):
        raise NotImplementedError("Subclasses must implement compute_expression method")


class PostfixArithmeticEngine(ArithmeticEngine):
    def compute_expression(self, expression):
        stack = []
        operators = set(['+', '-', '*', '/', '^'])
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                if len(stack) < 2:
                    raise ValueError("Malformed expression")
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    stack.append(operand1 / operand2)
                elif token == '^':
                    stack.append(operand1 ** operand2)
            else:
                raise ValueError("Invalid token: {}".format(token))
        if len(stack) != 1:
            raise ValueError("Malformed expression")
        return stack.pop()


class InfixToPostfixConverter:
    def __init__(self):
        self.precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
        self.operators = set(['+', '-', '*', '/', '^'])

    def infix_to_postfix(self, expression):
        stack = []
        postfix = []
        for token in expression.split():
            if token.isdigit():
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise ValueError("Mismatched parentheses")
                stack.pop()  # Remove '('
            elif token in self.operators:
                while stack and self.precedence.get(stack[-1], 0) >= self.precedence.get(token, 0):
                    postfix.append(stack.pop())
                stack.append(token)
            else:
                raise ValueError("Invalid token: {}".format(token))
        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            postfix.append(stack.pop())
        return ' '.join(postfix)


class InfixArithmeticEngine(ArithmeticEngine):
    def compute_expression(self, expression):
        converter = InfixToPostfixConverter()
        postfix_expression = converter.infix_to_postfix(expression)
        postfix_evaluator = PostfixArithmeticEngine()
        return postfix_evaluator.compute_expression(postfix_expression)


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def simulate_movie_ticket_booking(N, num_persons):
    queues = [CustomQueue() for _ in range(N)]

    # Enqueue persons into queues
    for queue in queues:
        for i in range(num_persons):
            queue.enqueue("Person {}".format(i))

    ticket_collector_time = 0
    while True:
        all_empty = True
        for i in range(N - 1, -1, -1):
            if not queues[i].is_empty():
                all_empty = False
                person = queues[i].dequeue()
                print("Ticket collector processing:", person)
                ticket_collector_time += 2  # Time taken to process a person
                if i != 0:
                    queues[i - 1].enqueue(person)
        if all_empty:
            break

    print("Total time taken by the ticket collector is :", ticket_collector_time, "minutes")


def evaluate_paper(scores):
    num_reviewers = len(scores)
    num_criteria = len(scores[0])

    # Calculate average score for each reviewer
    reviewer_averages = [sum(scores[i]) / num_criteria for i in range(num_reviewers)]

    # Check rule 1: If any reviewer's average is below 5, reject the paper
    if any(avg < 5 for avg in reviewer_averages):
        return "Rejected"

    # Calculate overall average of all reviewers
    overall_average = sum(sum(row) for row in scores) / (num_reviewers * num_criteria)

    # Check rule 2: If overall average is greater than or equal to 7, accept the paper
    if overall_average >= 7:
        return "The result is Accepted because average lies within the given range"

    # Check for borderline case
    if 6 <= overall_average < 7:
        return "Borderline"

    # If neither rejected nor accepted nor borderline, return None
    return None


if __name__ == "__main__":
    # Test the arithmetic engine with infix expression
    infix_arithmetic_engine = InfixArithmeticEngine()
    infix_expression = "4 * 5 - 10"
    try:
        result = infix_arithmetic_engine.compute_expression(infix_expression)
        print("Infix Expression:", infix_expression)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)

    # Test the movie ticket booking simulation
    N = int(input("Enter the number of queues: "))
    num_persons = max(7, int(input("Enter the number of persons in each queue (minimum 7): ")))
    simulate_movie_ticket_booking(N, num_persons)

    # Test the paper evaluation
    scores = [
        [9, 9, 7, 6, 8],
        [7, 8, 5, 7, 8],
        [6, 7, 8, 8, 6],
        [9, 8, 7, 8, 7]
    ]
    result = evaluate_paper(scores)
    if result:
        print("Result:", result)
    else:
        print("Cannot make a decision based on given scores.")

