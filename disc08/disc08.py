# Question 2.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)


# Question 2.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    """
    # Solution #1
    out_lnk_first = Link(1)
    out_lnk = out_lnk_first
    while all([lnk is not Link.empty for lnk in lst_of_lnks]):
        for i in range(0, len(lst_of_lnks)):
            out_lnk.first *= lst_of_lnks[i].first
            lst_of_lnks[i] = lst_of_lnks[i].rest
        if all([lnk is not Link.empty for lnk in lst_of_lnks]):
            out_lnk.rest = Link(1)
            out_lnk = out_lnk.rest
    return out_lnk_first
    """
    # Solution #2
    val = 1
    new_lst = []
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return lnk
        val *= lnk.first
        new_lst.append(lnk.rest)
    return Link(val, rest = multiply_lnks(new_lst))


# Question 2.3
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        lnk = lnk.rest
        if lnk.rest is Link.empty:
            return
        else:
            flip_two(lnk.rest)


# Question 2.4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    """
    # Solution #1, w/ while loop
    while link is not Link.empty:
        if f(link.first):
            yield link.first            
        link = link.rest
    """
    # Solution #2, w/o while loop
    if link is Link.empty:
        return
    else:
        #RECURSION
        if f(link.first):
            yield link.first
        yield from filter_link(link.rest, f)
    """
    # Solution #3, using return instead of yield
    # NOTE: the current doctest will fail, as it's not a generator func
    if link is Link.empty:
        return []
    out = [link.first] if f(link.first) else []
    for o in filter_link(link.rest, f):
        out.extend(o)
    return out
    """
    
    
# Question 3.1
def make_even(t):
    """
    Define a function make even which takes in a tree t whose values are integers, and
    mutates the tree such that all the odd integers are increased by 1 and all the even
    integers remain the same.
    
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 0:
        pass
    else:
        t.label += 1
    for b in t.branches:
        make_even(b)



# Question 3.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label = t.label ** 2
    for b in t.branches:
        square_tree(b)
        
        


# Question 3.3
def find_paths(t, entry):
    """
    Define the procedure find paths that, given a Tree t and an entry,
    returns a list of lists containing the nodes along each path from the root of t to
    entry. You may return the paths in any order.

    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    """
    # generator func version:
    if t.label == entry:
        yield [t.label]
    
    for b in t.branches:
        for p in find_paths(b, entry):
            yield [t.label] + p
    """
    # this is an interesting class of Tree recursion problems; several lab questions have the same design
    # what if the entry has to be a leaf?
    """
    # if the entry has to be a leaf
    if t.is_leaf() and t.label == entry:
        yield [t.label]
    for b in t.branches:
        for p in find_paths(b, entry):
            yield [t.label] + p

    ## return version:
    # paths = []
    # if t.is_leaf() and t.label == entry:
    #     paths.append([t.label])
    # for b in t.branches:
    #     for p in find_paths(b, entry):
    #         paths.append([t.label] + p)
    # return paths
    """

    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for p in find_paths(b, entry):
            # if there is any hint
            paths.append([t.label] + p)
    return paths
    


from operator import mul
# Question 3.4
def combine_tree(t1, t2, combiner):
    """
    Write a function that combines the values of two trees t1 and t2 together with the
    combiner function. Assume that t1 and t2 have identical structure. This function
    should return a new tree.
    
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    return Tree(combiner(t1.label, t2.label),
                    branches = [combine_tree(b1, b2, combiner)
                                for b1, b2 in zip(t1.branches, t2.branches)])
    



# Question 3.5
def alt_tree_map(t, map_fn):
    """
    Implement the alt tree map function that, given a function and a Tree, applies the
    function to all of the data at every other level of the tree, starting at the root.
    
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    
    t.label = map_fn(t.label)
    for b in t.branches:
        for grand_b in b.branches:
            alt_tree_map(grand_b, map_fn)
    return t
    
##################
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        #return f"Link({self.first}, {self.rest})"
        out = f"Link(" + repr(self.first)
        if self.rest is not Link.empty:
            out += f", " + repr(self.rest) + ")"
        else:
            out += ")"
        return out

    def __str__(self):
        #current = self
        out = f"<"
        while self.rest is not Link.empty:
        #while current.rest is not Link.empty:
            #out += f"{current.first}" + " "
            out += f"{self.first}" + " "
            #current = current.rest
            self = self.rest
        #out += f"{current.first}>"
        out += f"{self.first}>"
        return out
    
    

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()