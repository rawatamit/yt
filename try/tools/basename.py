import sys # 0

# 0 introduce basename

if __name__ == '__main__': # 0 ->
    # print(sys.argv) # 0
    # 0 introduce lists, empty list, indexing, length
    # 0 introduce strings, empty string, indexing, length
    if len(sys.argv) > 1: # 2 ->
        name = sys.argv[1] # 1 ->
        # print(name) # 1, 2
        # 1 introduce variables, simple example
        # 1 why such an indexing is incorrect, what if no path given, e.g. of exception thrown
        # 3 our observation is that the program print the last component of name
        # 3 what if we iterate from the back of the string to the front, and stop when
        # 3 we either find the first / character or we reach the front
        name_index = len(name) - 1 # 3 ->
        while name_index >= 0 and name[name_index] != '/': # 3 ->
            name_index -= 1 # 3 ->
        # print(name_index) # 3
        # 4 run couple of examples with this code, show that index computed are correct
        # 4 show how a while loop works, introduce >, !=, and booleans
        basename = name[name_index+1:] # 5 ->
        print(basename) # 5 ->
        # 5 introduce slicing in strings and lists
        # 5 END this video
    else: # 2 ->
        print(f'usage: {sys.argv[0]} NAME') # 2
        # 2 explain f-strings, a couple of examples inside shell
