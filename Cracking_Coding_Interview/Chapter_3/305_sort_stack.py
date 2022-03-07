def SortStack(stack):

    holder = []

    while stack:
        tmp = stack.pop()

        while holder and holder.peek() > tmp:
            stack.push(holder.pop())

        holder.push(tmp)

    # copy the elements from holder back to stack
    while holder:
        stack.push(holder.pop())

"""

stack: [1, ]
holder: [3, 7, 9]
tmp: 5

"""