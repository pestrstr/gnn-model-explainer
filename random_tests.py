import networkx as nx
import utils.synthetic_structsim as graph_syn
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # First testing some configurations alone

    # ba, _ = graph_syn.ba(start=0, width=10, role_start=0, m=1)
    # house, _ = graph_syn.house(start=0)

    fan, _ = graph_syn.fan(start=0, nb_branches=6)
    nx.draw(fan, with_labels=True, font_weight='bold')
    plt.show()
    plt.close()

    # Now testing the graph builder utility

    nb_shapes = 2
    width_basis = 10
    basis_type = "ba"

    # Arguments for attaching shapes in the graph must be provided in the followind way:
    # list_shapes = [["shape_name1", arg1_1, arg1_2], ["shape_name2", arg2_1, arg2_2]]
    
    list_shapes = [["diamond"]] * nb_shapes

    G, role_id, _ = graph_syn.build_graph(width_basis, basis_type, list_shapes, start=0, m=5)

    print(role_id)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.close()

