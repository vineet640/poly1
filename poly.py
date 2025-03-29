"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Aarnav Chitari and Vineet Burugu, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ac84787
UT EID 2: vsb433
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """
    a
    """
    def __init__(self):
        """
        a
        """
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        a
        """
        if coeff == 0:
            return
        a = Node(coeff, exp)
        if self.head is None:
            self.head = a
            return
        if self.head.exp < exp:
            a.next = self.head
            self.head = a
            return
        b = None
        c = self.head
        while True:
            if c is None or c.exp <= exp:
                break
            b = c
            c = c.next
        if c and c.exp == exp:
            c.coeff = c.coeff + coeff
            if c.coeff == 0 and b:
                b.next = c.next
            elif c.coeff == 0 and not b:
                self.head = c.next
        else:
            a.next = c
            if not b:
                self.head = a
            else:
                b.next = a

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        a
        """
        a = LinkedList()
        b = self.head
        c = p.head
        while b and c:
            if b.exp < c.exp:
                a.insert_term(c.coeff, c.exp)
                c = c.next
            elif c.exp < b.exp:
                a.insert_term(b.coeff, b.exp)
                b = b.next
            else:
                d = c.coeff + b.coeff
                a.insert_term(d, b.exp)
                b = b.next
                c = c.next
        for node in (b, c):
            while node:
                a.insert_term(node.coeff, node.exp)
                node = node.next
        return a

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        a
        """
        result = LinkedList()
        a = self.head
        while a:
            b = p.head
            while b:
                x = a.coeff * b.coeff
                y = a.exp + b.exp
                result.insert_term(x, y)
                b = b.next
            a = a.next
        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        """
        a
        """
        terms = []
        if not self.head:
            return ""
        h = self.head
        while h:
            terms.append(f"({h.coeff}, {h.exp})")
            h = h.next
        return " + ".join(terms)

def main():
    """
    a
    """
    p = LinkedList()
    n = int(input())
    pinput = [input().split() for i in range(n)]
    for coeff, exp in pinput:
        p.insert_term(int(coeff), int(exp))

    input()

    q = LinkedList()
    m = int(input())
    qinput = [input().split() for i in range(m)]
    for coeff, exp in qinput:
        q.insert_term(int(coeff), int(exp))

    sum_result = p.add(q)
    print(sum_result)

    product_result = p.mult(q)
    print(product_result)


if __name__ == "__main__":
    main()
