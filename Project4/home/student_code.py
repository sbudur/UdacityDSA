from math import sin, cos, sqrt, atan2, radians

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.f = 0
        self.g = 0
        self.h = 0
        

def calculate_distance(coord_1, coord_2):
    # approximate radius of earth in km
    R = 6373.0
    
    lat1 = radians(coord_1[0])
    lon1 = radians(coord_1[1])
    lat2 = radians(coord_2[0])
    lon2 = radians(coord_2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
    distance = R * c

    #print("Result:", distance)
    
    return distance

def shortest_path(M,start,goal):
    #print("shortest path called")
    
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    #print('start - ', start_node.position)
    end_node = Node(None, goal)
    end_node.g = end_node.h = end_node.f = 0
    #print('end - ', end_node.position)
    # Initialize both open and closed list
    open_list = []
    closed_list = []
    
    # Add the start node
    open_list.append(start_node)
    
    #ctr = 7
    #idx = 0
    # Loop until you find the end
    while len(open_list) > 0:
        #if idx == ctr:
        #    break
        #print('-----------iteration ', idx, '-----------------')
        # Get the current node
        current_node = open_list[0]
        current_index = 0
    
        #print('current node - open_list[0]', current_node.position ,'current_node.f' , current_node.f)
        # let the currentNode equal the node with the least f value remove the currentNode from the openList
        for index, item in enumerate(open_list):
            #print('open_list_item ', item.position ,' - item.f', item.f)
            if item.f < current_node.f:
                current_node = item
                current_index = index
            
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
    
        #print('now the current_node ', current_node.position)
        
        # Found the goal
        if current_node.position == end_node.position:
            #print('found goal')
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path
        
        for child in M.roads[current_node.position]:
            
            child_node = Node(current_node, child)
            #print('child node ', child_node.position)
            
            # if child is in the closedList, continue to beginning of for loop
            if len([closed_child for closed_child in closed_list if child_node.position == closed_child.position])>0:
                    #print('child ', child_node.position, ' already in closed list, continue to beginning of for loop')
                    continue
                    
            
            # Create the f, g, and h values
            child_node.g = current_node.g + calculate_distance(M.intersections[current_node.position], M.intersections[child_node.position])
            child_node.h = calculate_distance(M.intersections[child_node.position], M.intersections[end_node.position])
            child_node.f = child_node.g + child_node.h
            
            #print('calculating values ...')
            #print(child_node.g)
            #print(child_node.h)
            #print(child_node.f)
            
            # Child is already in the open list, continue to beginning of for loop
            if len([open_node for open_node in open_list if child_node.position == open_node.position and child_node.g >= open_node.g])>0:
                #print('child ', child_node.position, ' already in open list, continue to beginning of for loop')
                continue
            
            #print('adding to open list....')
            # Add the child to the open list
            open_list.append(child_node)
            #print('open list')
            #for each in open_list:
                #print(each.position)
            #print('closed list')
            #for each in closed_list:
                #print(each.position)
        
        #idx = idx+1
        
    
    return

"""
References for understanding algorithm and how it works:
1. https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
2. https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
"""

