# Question 1.1
def height(t):
    """Return the height of a tree
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        heights = [1+height(b) for b in branches(t)]
        return max(heights)

height(tree(3, [tree(5, [tree(1)]), tree(2)]))


# Question 1.2
def max_path_sum(t):
    """
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) 
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        sums = [label(t) + max_path_sum(b) for b in branches(t)]
        #print(f"label: {label(t)}, {sums}")
        return max(sums)

max_path_sum(tree(1, [tree(5, [tree(1), tree(3)]), tree(10)]))


# Question 1.3
def square_tree(t):
    if is_leaf(t):
        return tree(label=label(t)**2)
    else:
        #RECURSION
        return tree(label(t)**2, branches=[square_tree(b) for b in branches(t)])
    
square_tree(tree(1, [tree(5, [tree(1), tree(3)]), tree(10)]))
square_tree(tree(1, [
    tree(2, [tree(3), tree(4)]),
    tree(5, [tree(6, [tree(7)]), tree(8)])
]))


# Question 1.4
def find_path(t, x):
    """Find label X in tree T, assume unique labels"""
    if label(t) == x:
        return [label(t)]
    else:
        if is_leaf(t):
            # not found
            return None
        else:
            for b in branches(t):
                if find_path(b, x):
                    return [label(t)] + find_path(b, x)
            return None
        
def find_path(t, x):
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path

t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
find_path(t, 5)



# Question 2.1
def prune_binary(t, nums, word_so_far=''):
    if is_leaf(t):
        if (word_so_far + label(t)) not in nums:
            # prune this branch
            return None
        else:
            return t
    else:
        #RECURSION
        results = [prune_binary(b, nums, word_so_far+label(t)) for b in branches(t)]
        if not any(results):
            # not branches in num
            return None
        else:
            # save only viable branches
            return tree(label(t), [res for res in results if res is not None])


t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
print(t)
prune_binary(t, ['01', '110', '100'])




##################################################
# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])