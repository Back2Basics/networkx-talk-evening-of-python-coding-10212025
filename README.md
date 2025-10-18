# NetworkX Talk - Evening of Python Coding
NetworkX talk for evening of Python coding October 21, 2025

## Overview

This repository demonstrates how to use NetworkX to model various graph types and common computer science data structures. The talk covers:

### Part 1: Social Media Networks
- **Graph (Undirected)**: Facebook friend relationships (bidirectional friendships)
- **DiGraph (Directed)**: Twitter following relationships (directional following)
- **MultiGraph**: Multiple relationship types between the same people
- **MultiDiGraph**: Multiple directed interactions between users

### Part 2: Computer Science Data Structures as Graphs
- **Linked List**: Represented as a path graph
- **Tree**: Binary tree as an acyclic directed graph
- **Stack**: Last-In-First-Out (LIFO) structure
- **Deque**: Double-Ended Queue allowing insertion/deletion from both ends

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script to generate all visualizations:
```bash
python networkx_talk.py
```

This will:
- Print detailed information about each graph structure to the console
- Generate PNG visualization files for each data structure:
  - `facebook_graph.png`
  - `twitter_digraph.png`
  - `multigraph.png`
  - `multidigraph.png`
  - `linked_list.png`
  - `tree.png`
  - `stack.png`
  - `deque.png`

## Requirements

- Python 3.7+
- NetworkX 3.0+
- Matplotlib 3.5.0+

## Key Concepts Demonstrated

### Graph Types
- **Graph**: Undirected edges (mutual relationships)
- **DiGraph**: Directed edges (one-way relationships)
- **MultiGraph**: Multiple undirected edges between same nodes
- **MultiDiGraph**: Multiple directed edges between same nodes

### Data Structure Representations
- **Path Graph**: Linear sequence of nodes (linked list)
- **Acyclic Graph**: Tree structure with no cycles
- **Vertical Layout**: Stack visualization (LIFO)
- **Horizontal Layout**: Deque visualization (access both ends)

## Learning Resources

- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Graph Theory Basics](https://en.wikipedia.org/wiki/Graph_theory)
- [Data Structures and Algorithms](https://en.wikipedia.org/wiki/Data_structure)
