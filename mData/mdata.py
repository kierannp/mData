from torch_geometric.data import Data

class Multi_Data(Data):
    """
    A class for loading multiple datapoints from a pytorch geometric dataset

    ...

    Attributes
    ----------
    h : list, tensor, array
        the features of each node in the graph
    edge_index : list, tensor, array
        defines the connectiveity of the graph
    y : float, int, list
        the output value
    n_nodes : int
        the number of nodes for the corredponidng graph 
    """
    def __init__(
            self, 
            n_graphs=None, 
            node_features=None,
            edge_indexs=None,
            n_nodes=None,
            y=None):
        super().__init__()
        if n_graphs is None:
            setattr(self, f'edge_index', None)
            setattr(self, f'h', None)
            setattr(self, f'n_nodes', None)
        else:
            for i in range(n_graphs):
                setattr(self, f'edge_index_{i}', edge_indexs[i])
                setattr(self, f'h_{i}', node_features[i])
                setattr(self, f'n_nodes_{i}', n_nodes[i])

        self.y = y

class Multi_Coord_Data(Multi_Data):
    """
    A class for loading multiple datapoints from a pytorch geometric dataset

    ...

    Attributes
    ----------
    n_graphs : int
        number of graphs needed for datapoint
    node_features : list, tensor, array
        the features each node in the graph
    edge_index : list, tensor, array
        defines the connectiveity of the graph
    coordinates : lilst, tensor, array
        the coordinates of the nodes
    y : float, int, list
        the output value
    """
    def __init__(
            self,
            n_graphs=None, 
            node_features=None,
            coordinates=None,
            edge_indexs=None,
            n_nodes=None,
            y=None):
        super().__init__(
            n_graphs=n_graphs, 
            node_features=node_features,
            edge_indexs=edge_indexs,
            n_nodes=n_nodes,
            y=y
        )
        if n_graphs is None:
            setattr(self, f'x', None)
        else:
            for i in range(n_graphs):
                setattr(self, f'x_{i}', coordinates[i])

