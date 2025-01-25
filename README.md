# Wolfram Hypergraph Simulator (v0.1) 🌐

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)


A 2D implementation of Wolfram-style hypergraph evolution with dynamic visualization, demonstrating fundamental pattern generation through simple rules.

![Hypergraph Evolution Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDl4NnB6ZGZ3M2V4M2V5dW4wdjJ3eW1qY2Z6eGp4M3BvZ2l2eHZ0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ftAyb0CG1FNAIZt4SO/giphy.gif)

## Features ✨
- **Wolfram Rule Implementation**: Basic hyperedge evolution following Stephen Wolfram's models
- **Dynamic 2D Visualization**: Spring-layout organization with Matplotlib
- **Timelapse Evolution**: Step-through observation of pattern growth
- **Simple Interface**: Straightforward parameter adjustment for experimentation

## Installation ⚙️

```bash
# Clone repository
git clone https://github.com/yourusername/wolfram-hypergraphs.git

# Install requirements
pip install -r requirements.txt

# Core dependencies:
networkx >= 3.0
matplotlib >= 3.5
```
# Basic Usage 🚀
```python
from hypergraph_simulator import visualize_timelapse

# Initialize with sample hypergraph
initial_state = [[1,2], [2,3], [3,4], [2,4]]

# Run simulation with 10 evolution steps
visualize_timelapse(initial_state, steps=10, delay=0.3)
```
# Key Components 🔧
## Hypergraph Evolution Rule
```python
def apply_rule(hyperedge, current_max_node):
    """Wolfram-style edge transformation"""
    if len(hyperedge) == 2:
        x, y = hyperedge
        new_node = current_max_node + 1
        return [[x, y], [x, new_node], [y, new_node]], new_node
    return [hyperedge], current_max_node
```

## Visualization Parameters 🔧  
| Parameter          | Default      | Description                                  |  
|--------------------|--------------|----------------------------------------------|  
| `node_size`        | 50           | Node diameter in pixels                      |  
| `edge_color`       | `#87CEEB`    | Light blue (skyblue) for edge visualization  |  
| `background_color` | `#39312F`    | Dark gray (RGB 57,49,47) canvas background    |  
| `delay`            | 0.5 seconds  | Pause duration between evolution steps       |  
| `font_size`        | 8            | Node label text size                         |  

## Common Challenges & Solutions 🚨  
| Issue                      | Resolution                                  | Code Snippet                          |  
|----------------------------|---------------------------------------------|---------------------------------------|  
| Overlapping nodes          | Increase node repulsion                    | `nx.spring_layout(k=0.7)`             |  
| Unreadable labels          | Enlarge text size                          | `nx.draw(..., font_size=12)`          |  
| Fast animation             | Extend step delay                          | `visualize_timelapse(delay=1.5)`      |  
| Hyperedge visualization    | Convert N-ary edges to pairwise            | `hypergraph_to_graph()`               |  
| Background color reset     | Explicitly set facecolor                   | `plt.figure(facecolor='#39312F')`     |  

## Development Roadmap 🧭  
- [x] **v0.1 Base Implementation** (Current)  
  - Core evolution rules  
  - 2D spring layout visualization  
  - Step-through timelapse  
  
## Images of the exectutions

![Figure_1](https://github.com/user-attachments/assets/8e77c3be-c5a6-48b7-9963-4d9f9e591b64)
![Figure_2](https://github.com/user-attachments/assets/220ae338-996a-4a26-8e5d-aa82ec2826cb)
![Figure_3](https://github.com/user-attachments/assets/e21db71c-dca7-42cc-a53b-77401a0552c7)
![Figure_4](https://github.com/user-attachments/assets/43a73fa2-d248-47f8-9441-e4bf746194b9)
![Figure_5](https://github.com/user-attachments/assets/16646597-246d-4d2f-894b-d3dad92f6807)
![Figure_6](https://github.com/user-attachments/assets/3b656fa7-dbdf-49a3-a151-99a2535add95)

##After this step it turns chaotic I57
![Figure_7](https://github.com/user-attachments/assets/d17c872a-1483-454f-87fe-e3d9ef3819e4)

![Figure_8](https://github.com/user-attachments/assets/9d2ae298-51a9-403c-a48f-5c8c6c24e55a)

![Figure_9](https://github.com/user-attachments/assets/a0ac07ee-4f19-40fd-972b-b266d1a40ef3)


--- 
  

