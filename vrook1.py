# This is different from TSP

from collections import defaultdict as dd

# input of data from stdout into a 
# defaultdict which stores distance 
# between all the places


table=dd(dd)
inp=input()
while(inp!=""):
    temp,cost=inp.split("=")
    start,end=temp.split("to")
    table[start.strip()][end.strip()]=cost.strip()
    table[end.strip()][start.strip()]=cost.strip()
    inp=input()

# route is the order of places which has to covered to have minimum distance
route,minimum_distance=[],100000000

# This finding minimum distance of all the places
for k,v in table.items():
    for K,V in v.items():
        V=int(V)
        if(V<minimum_distance):
            minimum_distance=V
            start=k
            end=K
route.append(start)
route.append(end)
length=int(table[start][end])

# from here on joining places to the start or end of the route depending on the minimum distances untill all the plcaes are covered
while(len(table)!=len(route)):
    # finding a place which is at minimum distance from start place
    minimum_distance_from_starting_node=10000000000
    for k,v in table[route[0]].items():
        v=int(v)
        if(v<minimum_distance_from_starting_node and k not in route):
            minimum_distance_from_starting_node=v
            st=k
    
    # finding a place which is at minimum distance from end place

    minimum_distance_from_ending_node=10000000000 
    for k,v in table[route[-1]].items():
        v=int(v)

        if(v<minimum_distance_from_ending_node and k not in route):
            minimum_distance_from_ending_node=v
            en=k

    # joining the place to the route which is at minimum distance
    if(minimum_distance_from_ending_node<minimum_distance_from_starting_node):
        route.append(en)
        del table[route[-2]][route[-1]]
        del table[route[-1]][route[-2]]

        length+=minimum_distance_from_ending_node
    else:
        route.insert(0,st)
        del table[route[0]][route[1]]
        del table[route[1]][route[0]]

        length+=minimum_distance_from_starting_node


for i in route:
    print(i,end="-> ")
print("= "+str(length))