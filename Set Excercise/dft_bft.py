# %%
tree = {
    "node": 1,
    "sub-nodes": [
        {
            "node": 2,
            "sub-nodes": [
                {
                    "node": 3,
                    "sub-nodes": [
                        {
                            "node": 4,
                        }
                    ]
                }
            ]
        },
        {
            "node": 5,
            "sub-nodes": [
                {
                    "node": 6,
                    "sub-nodes": [
                        {
                            "node": 7,
                        }
                    ]
                },
                {
                    "node": 8,
                }
            ]
        },
        {
            "node": 9,
            "sub-nodes": [
                {
                    "node": 10,

                }
            ]
        }
    ]
}


# Depth first traveral which visits the node first
print("Depth First Traversal:")
def dft(node):

    print(node["node"])

    if ("sub-nodes" in node):
        for sub_node in node["sub-nodes"]:
            dft(sub_node)


dft(tree)

# Breadth first traversal which 
def searchByBft(orderLine):

    if(len(orderLine) > 0):

        node = orderLine.pop(0)

        for key, value in node.items():
            if key == "sub-nodes":
                for item in value:
                    orderLine.append(item)
            else:
             
                print("Node:" + str(value))

        searchByBft(orderLine)


print("\nBreadth First Traversal:")
searchByBft([tree])
# %%
