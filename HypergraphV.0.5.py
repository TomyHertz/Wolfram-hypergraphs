# Wolfram Hypergraph Simulation with Brain-like Structure
import networkx as nx
import plotly.graph_objects as go
import random

# Define initial hypergraph structure with organic connections
hypergraph = [
    # Central core (triangle)
    [1, 2], [2, 3], [3, 1],
    # Primary branches connecting core to secondary nodes
    [1, 4], [2, 5], [3, 6],
    # Secondary branches
    [4, 7], [5, 8], [6, 9],
    # Tertiary connections
    [7, 10], [8, 11], [9, 12],
    # Chaotic cross-connections to create organic complexity
    [4, 8], [5, 9], [6, 7], [10, 11]
]

def evolve_hypergraph(hypergraph, steps):
    """
    Evolve the hypergraph through multiple steps using depth-first approach
    Args:
        hypergraph (list): Initial hypergraph structure
        steps (int): Number of evolution iterations
    Yields:
        list: Updated hypergraph state after each step
    """
    current_max_node = max([node for edge in hypergraph for node in edge], default=0)
    for _ in range(steps):
        new_hypergraph = []
        for edge in hypergraph:
            # Apply transformation rule to each hyperedge
            transformed_edges, current_max_node = apply_rule(edge, current_max_node)
            new_hypergraph.extend(transformed_edges)
        hypergraph = new_hypergraph
        yield hypergraph  # Return generator for memory efficiency

def apply_rule(hyperedge, current_max_node):
    """
    Wolfram-style organic evolution rule with stochastic branching
    Args:
        hyperedge (list): The hyperedge to transform
        current_max_node (int): Current highest node ID
    Returns:
        tuple: (transformed edges, new maximum node ID)
    """
    if len(hyperedge) == 2:  # Only process binary edges
        x, y = hyperedge
        new_node = current_max_node + 1
        # 50% chance to create extra connection for organic branching
        if random.random() > 0.5:
            return [[x, y], [x, new_node], [y, new_node], 
                    [new_node, random.choice([x, y])]], new_node
        return [[x, y], [x, new_node], [y, new_node]], new_node
    return [hyperedge], current_max_node  # Leave larger hyperedges unchanged

def hypergraph_to_graph(hypergraph):
    """
    Convert hypergraph to standard graph for visualization
    Args:
        hypergraph (list): List of hyperedges
    Returns:
        nx.Graph: NetworkX graph object
    """
    G = nx.Graph()
    for edge in hypergraph:
        # Create pairwise connections from hyperedges
        for i in range(len(edge)):
            for j in range(i + 1, len(edge)):
                G.add_edge(edge[i], edge[j])
    return G

def visualize_hypergraph_3d(hypergraph):
    """
    Generate interactive 3D visualization using Plotly
    Args:
        hypergraph (list): Current hypergraph state
    """
    G = hypergraph_to_graph(hypergraph)
    # Calculate 3D layout with organic spacing
    pos = nx.spring_layout(G, dim=3, iterations=500, k=0.3, seed=42)
    
    # Extract node coordinates
    x_nodes = [pos[n][0] for n in G.nodes]
    y_nodes = [pos[n][1] for n in G.nodes]
    z_nodes = [pos[n][2] for n in G.nodes]
    
    # Build edge coordinates with None separators
    x_edges, y_edges, z_edges = [], [], []
    for edge in G.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]
        z_edges += [pos[edge[0]][2], pos[edge[1]][2], None]

    # Create edge trace with neural-like appearance
    edge_trace = go.Scatter3d(
        x=x_edges, y=y_edges, z=z_edges,
        mode='lines',
        line=dict(color='#70A9FF', width=0.3),  # Synapse blue
        hoverinfo='none'
    )
    
    # Create node trace with biological styling
    node_trace = go.Scatter3d(
        x=x_nodes, y=y_nodes, z=z_nodes,
        mode='markers',
        marker=dict(
            size=1.5,
            color='#FF6E6E',  # Neuron red
            opacity=0.7       # Semi-transparent for depth
        ),
        hoverinfo='none'
    )
    
    # Configure scene layout
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        scene=dict(
            xaxis=dict(showbackground=False),
            yaxis=dict(showbackground=False),
            zaxis=dict(showbackground=False),
            bgcolor='#1A1A1A'  # Dark background for contrast
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    fig.show(renderer='browser')  # Force browser rendering

def visualize_timelapse_3d(hypergraph, steps):
    """
    Visualize hypergraph evolution through multiple steps
    Args:
        hypergraph (list): Initial hypergraph structure
        steps (int): Number of evolution steps
    """
    for i, state in enumerate(evolve_hypergraph(hypergraph, steps)):
        print(f"Visualizing Step {i + 1}/{steps}")
        visualize_hypergraph_3d(state)

# Main execution: Run simulation with 4 evolution steps
if __name__ == "__main__":
    steps = 4
    visualize_timelapse_3d(hypergraph, steps)