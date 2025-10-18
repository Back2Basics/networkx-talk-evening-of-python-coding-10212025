"""
Example usage of individual functions from networkx_talk module.

This script demonstrates how to import and use specific graph demonstrations
from the main networkx_talk module.
"""

from networkx_talk import (
    create_facebook_graph,
    create_twitter_digraph,
    create_linked_list,
    create_tree
)


def main():
    """
    Example of using individual functions from the networkx_talk module.
    """
    
    # Create only the Facebook graph
    print("Creating Facebook friend network...")
    facebook_g = create_facebook_graph()
    print(f"Facebook graph has {facebook_g.number_of_nodes()} users")
    
    # Create only the Twitter directed graph
    print("\nCreating Twitter following network...")
    twitter_dg = create_twitter_digraph()
    print(f"Twitter graph has {twitter_dg.number_of_edges()} following relationships")
    
    # Create only the linked list
    print("\nCreating Linked List...")
    ll = create_linked_list()
    print(f"Linked list has {ll.number_of_nodes()} nodes")
    
    # Create only the tree
    print("\nCreating Binary Tree...")
    tree = create_tree()
    print(f"Tree has {tree.number_of_nodes()} nodes and {tree.number_of_edges()} edges")


if __name__ == "__main__":
    main()
