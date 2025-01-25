# Wolfram Hypergraph Simulation with Brain-like Structure
import networkx as nx
import plotly.graph_objects as go
import random

# Define organic initial connections
hypergraph = [
    [1, 2], [2, 3], [3, 1],           # Núcleo central
    [1, 4], [2, 5], [3, 6],           # Ramificaciones primarias
    [4, 7], [5, 8], [6, 9],           # Ramificaciones secundarias
    [7, 10], [8, 11], [9, 12],        # Conexiones terciarias
    [4, 8], [5, 9], [6, 7], [10, 11] # Conexiones cruzadas caóticas
]

# Función de evolución del hipergrafo
def evolve_hypergraph(hypergraph, steps):
    current_max_node = max([node for edge in hypergraph for node in edge], default=0)
    for _ in range(steps):
        new_hypergraph = []
        for edge in hypergraph:
            transformed_edges, current_max_node = apply_rule(edge, current_max_node)
            new_hypergraph.extend(transformed_edges)
        hypergraph = new_hypergraph
        yield hypergraph

# Regla de evolución orgánica
def apply_rule(hyperedge, current_max_node):
    if len(hyperedge) == 2:
        x, y = hyperedge
        new_node = current_max_node + 1
        if random.random() > 0.5:
            return [[x, y], [x, new_node], [y, new_node], [new_node, random.choice([x, y])]], new_node
        else:
            return [[x, y], [x, new_node], [y, new_node]], new_node
    return [hyperedge], current_max_node

# Conversión a grafo estándar
def hypergraph_to_graph(hypergraph):
    G = nx.Graph()
    for edge in hypergraph:
        for i in range(len(edge)):
            for j in range(i + 1, len(edge)):
                G.add_edge(edge[i], edge[j])
    return G

# Visualización 3D con apertura en navegador
def visualize_hypergraph_3d(hypergraph):
    G = hypergraph_to_graph(hypergraph)
    pos = nx.spring_layout(G, dim=3, iterations=500, k=0.3, seed=42)
    
    x_nodes = [pos[n][0] for n in G.nodes]
    y_nodes = [pos[n][1] for n in G.nodes]
    z_nodes = [pos[n][2] for n in G.nodes]
    
    x_edges, y_edges, z_edges = [], [], []
    for edge in G.edges:
        x_edges += [pos[edge[0]][0], pos[edge[1]][0], None]
        y_edges += [pos[edge[0]][1], pos[edge[1]][1], None]
        z_edges += [pos[edge[0]][2], pos[edge[1]][2], None]
    
    edge_trace = go.Scatter3d(
        x=x_edges, y=y_edges, z=z_edges,
        mode='lines',
        line=dict(color='#70A9FF', width=0.3)
    )
    
    node_trace = go.Scatter3d(
        x=x_nodes, y=y_nodes, z=z_nodes,
        mode='markers',
        marker=dict(size=2, color='#FF6E6E')#, opacity=0.7)
    )
    
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(scene=dict(
        xaxis=dict(showbackground=False),
        yaxis=dict(showbackground=False),
        zaxis=dict(showbackground=False),
        bgcolor='#1A1A1A'
    ))
    fig.show(renderer='browser')  # Renderizador explícito

# Función de timelapse
def visualize_timelapse_3d(hypergraph, steps):
    for i, state in enumerate(evolve_hypergraph(hypergraph, steps)):
        print(f"Step {i + 1}/{steps}")
        visualize_hypergraph_3d(state)

# Ejecutar
steps = 4
visualize_timelapse_3d(hypergraph, steps)