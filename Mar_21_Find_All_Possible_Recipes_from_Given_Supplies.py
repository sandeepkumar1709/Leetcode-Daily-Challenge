
"""
Approach:
    The approach is to create a directed graph where each ingredient points to the recipes that can be made with it.
    we also maintain an indegree count for each recipe, which is the number of ingredients required to make that recipe.
    Now, we start with the supplies and for each supply, we check if it is an ingredient for any recipe.
    If it is, we reduce the indegree count for that recipe by 1. If the indegree count becomes 0, 
    it means that all ingredients for that recipe are available, so we can add that recipe to the supplies.
Time complexity:
    O(n + m) where n is the number of recipes and m is the number of ingredients.
Space complexity:
    O(n + m) for the graph and indegree count.
"""


from collections import deque, defaultdict
def findAllRecipes(recipes, ingredients, supplies):


    graph,indegree = defaultdict(list), defaultdict(int)

    for index, values in enumerate(ingredients):
        for each_value in values:
            # print(index)
            graph[each_value].append(recipes[index])
            indegree[recipes[index]] += 1
    
    supplies,ans = deque(supplies), []


    while supplies:
        current_supply = supplies.popleft()

        if current_supply in graph:
            for each_recepie in graph[current_supply]:
                if each_recepie in indegree:
                    indegree[each_recepie] -=1
                    if indegree[each_recepie] == 0:
                        ans.append(each_recepie)
                        supplies.appendleft(each_recepie)

    return ans