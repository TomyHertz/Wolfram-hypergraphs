# Wolfram Hypergraph Simulation with Timelapse Visualization
import networkx as nx
import matplotlib.pyplot as plt
import time

# Define the initial hypergraph following the example in the website
hypergraph = [[1, 2], [2, 3], [3, 4], [2, 4]]  # Example initial state

# Define the rule for hypergraph evolution
def apply_rule(hyperedge, current_max_node):
    """
    Apply the Wolfram rule:
    {x, y}, {x, z} -> {x, z}, {x, w}, {y, w}, {z, w}
    """
    if len(hyperedge) == 2:  # Only match edges of size 2
        x, y = hyperedge
        new_node = current_max_node + 1
        return [[x, y], [x, new_node], [y, new_node]], new_node
    return [hyperedge], current_max_node

# Apply the rules iteratively and update the hypergraph
def evolve_hypergraph(hypergraph, steps):
    """Apply the evolution rule for a given number of steps."""
    current_max_node = max([node for edge in hypergraph for node in edge], default=0)
    for _ in range(steps):
        new_hypergraph = []
        for edge in hypergraph:
            transformed_edges, current_max_node = apply_rule(edge, current_max_node)
            new_hypergraph.extend(transformed_edges)
        hypergraph = new_hypergraph
        yield hypergraph  # Yield the hypergraph state after each step

# Convert hypergraph to a NetworkX graph for visualization
def hypergraph_to_graph(hypergraph):
    """Convert hypergraph to a standard graph for visualization."""
    G = nx.Graph()
    for edge in hypergraph:
        for i in range(len(edge)):
            for j in range(i + 1, len(edge)):
                G.add_edge(edge[i], edge[j])
    return G

# Visualize the hypergraph with a spring layout for better structure
def visualize_hypergraph(hypergraph):
    """Visualize the hypergraph as a structured graph."""
    G = hypergraph_to_graph(hypergraph)
    pos = nx.spring_layout(G)  # Use spring layout
    plt.figure(figsize=(15, 15), facecolor=(57/255, 49/255, 47/255))  # Set background color
    nx.draw(
        G,
        pos=pos,  # Spring layout for better structure
        with_labels=True,
        node_color="lightblue",
        node_size=50,
        font_size=8,
        edge_color="skyblue",  # Edge color set to light blue
    )
    plt.show()

# Visualize the evolution as a timelapse
def visualize_timelapse(hypergraph, steps, delay=0.5):
    """Visualize the evolution of the hypergraph as a timelapse."""
    for i, state in enumerate(evolve_hypergraph(hypergraph, steps)):
        print(f"Step {i + 1}/{steps}")
        visualize_hypergraph(state)
        time.sleep(delay)  # Pause between steps

# Initial visualization
print("Initial Hypergraph:", hypergraph)
visualize_hypergraph(hypergraph)

# Evolve and visualize as a timelapse
steps = 10
delay = 0.5  # Delay in seconds between steps
visualize_timelapse(hypergraph, steps, delay)