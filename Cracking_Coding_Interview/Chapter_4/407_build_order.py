from typing import List

def build_order(projects: List, dependencies: List) -> List:
    """
    Assumption: all the projects are names as lowercase characters
    """

    adjacency_list = [[] for _ in range(projects)]

    for p1, p2 in dependencies:
        adjacency_list[p1 - ord('a')].append(p2)

    
        
