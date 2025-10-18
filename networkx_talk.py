"""
NetworkX Talk - Evening of Python Coding
October 21, 2025

This module demonstrates different types of graphs and how they can be used
to represent social media relationships and common computer science data structures.
"""

import networkx as nx
import matplotlib.pyplot as plt


def create_facebook_graph():
    """
    Create a Graph to represent Facebook friendships.
    In Facebook, friendships are bidirectional (undirected edges).
    """
    print("\n=== Facebook Friend Network (Graph) ===")
    G = nx.Graph()
    
    # Add users as nodes
    users = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    G.add_nodes_from(users)
    
    # Add friendships as edges (bidirectional)
    friendships = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Diana"),
        ("Charlie", "Diana"),
        ("Diana", "Eve"),
        ("Eve", "Frank"),
        ("Frank", "Alice")
    ]
    G.add_edges_from(friendships)
    
    print(f"Nodes: {G.nodes()}")
    print(f"Edges: {G.edges()}")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    
    # Visualize
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', 
            node_size=1500, font_size=10, font_weight='bold',
            edge_color='gray', width=2)
    plt.title("Facebook Friend Network (Undirected Graph)")
    plt.tight_layout()
    plt.savefig('facebook_graph.png')
    plt.close()
    
    return G


def create_twitter_digraph():
    """
    Create a DiGraph to represent Twitter following relationships.
    In Twitter, following is directional (directed edges).
    """
    print("\n=== Twitter Following Network (DiGraph) ===")
    DG = nx.DiGraph()
    
    # Add users as nodes
    users = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    DG.add_nodes_from(users)
    
    # Add following relationships (directional: follower -> followed)
    # Alice follows Bob and Charlie
    # Bob follows Charlie
    # Charlie follows Diana
    # Diana follows Alice and Eve
    # Eve follows Alice
    following = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Charlie"),
        ("Charlie", "Diana"),
        ("Diana", "Alice"),
        ("Diana", "Eve"),
        ("Eve", "Alice")
    ]
    DG.add_edges_from(following)
    
    print(f"Nodes: {DG.nodes()}")
    print(f"Edges: {DG.edges()}")
    print(f"Alice follows: {list(DG.successors('Alice'))}")
    print(f"Alice is followed by: {list(DG.predecessors('Alice'))}")
    
    # Visualize
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(DG, seed=42)
    nx.draw(DG, pos, with_labels=True, node_color='lightcoral',
            node_size=1500, font_size=10, font_weight='bold',
            edge_color='darkred', width=2, arrows=True,
            arrowsize=20, arrowstyle='->')
    plt.title("Twitter Following Network (Directed Graph)")
    plt.tight_layout()
    plt.savefig('twitter_digraph.png')
    plt.close()
    
    return DG


def create_multigraph_example():
    """
    Create a MultiGraph to show multiple relationships between same nodes.
    Example: Different types of connections (friend, colleague, neighbor).
    """
    print("\n=== Multi-Relationship Network (MultiGraph) ===")
    MG = nx.MultiGraph()
    
    # Add nodes
    people = ["Alice", "Bob", "Charlie"]
    MG.add_nodes_from(people)
    
    # Add multiple edges between same nodes with different relationship types
    MG.add_edge("Alice", "Bob", relationship="friend")
    MG.add_edge("Alice", "Bob", relationship="colleague")
    MG.add_edge("Bob", "Charlie", relationship="neighbor")
    MG.add_edge("Bob", "Charlie", relationship="friend")
    MG.add_edge("Alice", "Charlie", relationship="colleague")
    
    print(f"Nodes: {MG.nodes()}")
    print(f"Edges: {MG.edges()}")
    print(f"Number of edges between Alice and Bob: {MG.number_of_edges('Alice', 'Bob')}")
    
    # Visualize
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(MG, seed=42)
    nx.draw(MG, pos, with_labels=True, node_color='lightgreen',
            node_size=1500, font_size=10, font_weight='bold',
            edge_color='green', width=2)
    plt.title("Multi-Relationship Network (MultiGraph)")
    plt.tight_layout()
    plt.savefig('multigraph.png')
    plt.close()
    
    return MG


def create_multidigraph_example():
    """
    Create a MultiDiGraph for multiple directed relationships.
    Example: Different types of interactions (message, like, share).
    """
    print("\n=== Multi-Directional Interactions (MultiDiGraph) ===")
    MDG = nx.MultiDiGraph()
    
    # Add nodes
    users = ["Alice", "Bob", "Charlie"]
    MDG.add_nodes_from(users)
    
    # Add multiple directed edges with different interaction types
    MDG.add_edge("Alice", "Bob", interaction="message")
    MDG.add_edge("Alice", "Bob", interaction="like")
    MDG.add_edge("Bob", "Alice", interaction="message")
    MDG.add_edge("Bob", "Charlie", interaction="share")
    MDG.add_edge("Charlie", "Bob", interaction="like")
    MDG.add_edge("Charlie", "Bob", interaction="message")
    
    print(f"Nodes: {MDG.nodes()}")
    print(f"Edges: {MDG.edges()}")
    print(f"Number of edges from Alice to Bob: {MDG.number_of_edges('Alice', 'Bob')}")
    
    # Visualize
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(MDG, seed=42)
    nx.draw(MDG, pos, with_labels=True, node_color='lightyellow',
            node_size=1500, font_size=10, font_weight='bold',
            edge_color='orange', width=2, arrows=True,
            arrowsize=20, arrowstyle='->')
    plt.title("Multi-Directional Interactions (MultiDiGraph)")
    plt.tight_layout()
    plt.savefig('multidigraph.png')
    plt.close()
    
    return MDG


def create_linked_list():
    """
    Create a Linked List as a path graph.
    A linked list is a sequence of nodes where each node points to the next.
    """
    print("\n=== Linked List (Path Graph) ===")
    # Create a path graph with 5 nodes
    LL = nx.path_graph(5, create_using=nx.DiGraph())
    
    # Relabel nodes to represent list elements
    mapping = {i: f"Node_{i}" for i in range(5)}
    LL = nx.relabel_nodes(LL, mapping)
    
    print(f"Nodes: {list(LL.nodes())}")
    print(f"Edges: {list(LL.edges())}")
    print("Structure: Node_0 -> Node_1 -> Node_2 -> Node_3 -> Node_4")
    
    # Visualize
    plt.figure(figsize=(10, 3))
    pos = nx.spring_layout(LL, seed=42)
    # Create a linear layout for linked list
    pos = {node: (i, 0) for i, node in enumerate(LL.nodes())}
    nx.draw(LL, pos, with_labels=True, node_color='lightpink',
            node_size=1500, font_size=9, font_weight='bold',
            edge_color='purple', width=2, arrows=True,
            arrowsize=20, arrowstyle='->')
    plt.title("Linked List (Path Graph)")
    plt.tight_layout()
    plt.savefig('linked_list.png')
    plt.close()
    
    return LL


def create_tree():
    """
    Create a Tree as an acyclic graph.
    Trees are connected acyclic graphs commonly used in CS.
    """
    print("\n=== Binary Tree (Acyclic Graph) ===")
    # Create a balanced binary tree
    Tree = nx.balanced_tree(2, 3, create_using=nx.DiGraph())
    
    print(f"Number of nodes: {Tree.number_of_nodes()}")
    print(f"Number of edges: {Tree.number_of_edges()}")
    print(f"Is acyclic: {nx.is_directed_acyclic_graph(Tree)}")
    print(f"Is tree: {nx.is_tree(Tree)}")
    
    # Visualize with hierarchical layout
    plt.figure(figsize=(10, 8))
    
    # Create a hierarchical layout for the tree
    def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """Create hierarchical layout for tree"""
        if root is None:
            root = [n for n in G.nodes() if G.in_degree(n) == 0][0]
        
        def _hierarchy_pos(G, node, left, right, pos, parent=None, parsed=[]):
            if node not in parsed:
                parsed.append(node)
                neighbors = list(G.successors(node))
                if len(neighbors) != 0:
                    dx = (right - left) / len(neighbors)
                    nextx = left + dx / 2
                    for neighbor in neighbors:
                        pos = _hierarchy_pos(G, neighbor, nextx - dx / 2, nextx + dx / 2, 
                                            pos, node, parsed)
                        nextx += dx
                pos[node] = ((left + right) / 2, vert_loc)
            return pos
        
        return _hierarchy_pos(G, root, 0, width, {}, None, [])
    
    pos = hierarchy_pos(Tree, root=0)
    # Flip y-axis so root is at top
    pos = {k: (v[0], -v[1]) for k, v in pos.items()}
    
    nx.draw(Tree, pos, with_labels=True, node_color='lightcyan',
            node_size=800, font_size=8, font_weight='bold',
            edge_color='teal', width=2, arrows=True,
            arrowsize=15, arrowstyle='->')
    plt.title("Binary Tree (Acyclic Directed Graph)")
    plt.tight_layout()
    plt.savefig('tree.png')
    plt.close()
    
    return Tree


def create_stack():
    """
    Create a Stack representation as a graph.
    A stack is a Last-In-First-Out (LIFO) data structure.
    We represent it as a linear sequence with the top being the most recently added.
    """
    print("\n=== Stack (LIFO Structure) ===")
    Stack = nx.DiGraph()
    
    # Stack elements (bottom to top)
    elements = ["Bottom", "Element_1", "Element_2", "Element_3", "Top"]
    Stack.add_nodes_from(elements)
    
    # Add edges showing the stack order (bottom points to top)
    for i in range(len(elements) - 1):
        Stack.add_edge(elements[i], elements[i + 1])
    
    print(f"Stack elements (bottom to top): {elements}")
    print(f"Nodes: {list(Stack.nodes())}")
    print("Operations: Push adds to top, Pop removes from top")
    
    # Visualize
    plt.figure(figsize=(6, 8))
    # Create a vertical layout for stack
    pos = {node: (0, i) for i, node in enumerate(elements)}
    nx.draw(Stack, pos, with_labels=True, node_color='lavender',
            node_size=2000, font_size=9, font_weight='bold',
            edge_color='indigo', width=2, arrows=True,
            arrowsize=20, arrowstyle='->')
    plt.title("Stack (LIFO - Last In First Out)")
    plt.tight_layout()
    plt.savefig('stack.png')
    plt.close()
    
    return Stack


def create_deque():
    """
    Create a Double-Ended Queue (Deque) representation.
    A deque allows insertion and deletion from both ends.
    """
    print("\n=== Deque (Double-Ended Queue) ===")
    Deque = nx.Graph()  # Undirected since we can access both ends
    
    # Deque elements
    elements = ["Left_End", "Element_1", "Element_2", "Element_3", "Right_End"]
    Deque.add_nodes_from(elements)
    
    # Add edges connecting elements in sequence
    for i in range(len(elements) - 1):
        Deque.add_edge(elements[i], elements[i + 1])
    
    print(f"Deque elements: {elements}")
    print(f"Nodes: {list(Deque.nodes())}")
    print("Operations: Can add/remove from both Left_End and Right_End")
    
    # Visualize
    plt.figure(figsize=(10, 3))
    # Create a horizontal layout for deque
    pos = {node: (i, 0) for i, node in enumerate(elements)}
    nx.draw(Deque, pos, with_labels=True, node_color='peachpuff',
            node_size=1500, font_size=9, font_weight='bold',
            edge_color='brown', width=3)
    plt.title("Deque (Double-Ended Queue)")
    plt.tight_layout()
    plt.savefig('deque.png')
    plt.close()
    
    return Deque


def main():
    """
    Main function to run all demonstrations.
    """
    print("=" * 70)
    print("NetworkX Talk - Evening of Python Coding")
    print("Demonstrating Graphs and Data Structures")
    print("=" * 70)
    
    # Social Media Examples
    print("\n" + "=" * 70)
    print("PART 1: Social Media Networks")
    print("=" * 70)
    
    facebook_graph = create_facebook_graph()
    twitter_digraph = create_twitter_digraph()
    multigraph = create_multigraph_example()
    multidigraph = create_multidigraph_example()
    
    # Computer Science Data Structures
    print("\n" + "=" * 70)
    print("PART 2: Computer Science Data Structures as Graphs")
    print("=" * 70)
    
    linked_list = create_linked_list()
    tree = create_tree()
    stack = create_stack()
    deque = create_deque()
    
    print("\n" + "=" * 70)
    print("All visualizations saved as PNG files!")
    print("=" * 70)
    print("\nGenerated files:")
    print("- facebook_graph.png")
    print("- twitter_digraph.png")
    print("- multigraph.png")
    print("- multidigraph.png")
    print("- linked_list.png")
    print("- tree.png")
    print("- stack.png")
    print("- deque.png")


if __name__ == "__main__":
    main()
