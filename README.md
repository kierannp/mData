# mData package

This is a package that enables batch loading of multi-graph datapoints using a subclass of the [PyTorch Geometric Data class](https://pytorch-geometric.readthedocs.io/en/latest/modules/data.html) .

## In this README :point_down:
- [Installation](#install)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

```python 
git clone https://github.com/kierannp/mData.git
cd mData
pip install .
```

## Usage

```python 
from mData import Multi_Data, Multi_Coord_Data
for g_triplet in dataset:
    h_0, h_1, h_2 = get_node_features(g_triplet)
    edges_0, edges_1, edges_2 = get_edge_indexes(g_triplet)
    x_0, x_1, x_2 = get_coordinates(g_triplet)
    n_0, n_1, n_2 = get_n_nodes(g_triplet)
    y = get_property(g_triplet)
    if not use_coord:
        datapoint = Multi_Data(
                        n_graphs = 3,
                        node_features = [h_0, h_1, h_2],
                        edge_indexs = [edges_0, edges_1, edges_2],
                        n_nodes = [n_0, n_1, n_2],
                        y = y)
    else:
        datapoint = Multi_Coord_Data(
                        n_graphs = 3,
                        node_features = [h_0, h_1, h_2],
                        coordinates = [x_0, x_1, x_2], 
                        edge_indexs = [edges_0, edges_1, edges_2],
                        n_nodes = [n_0, n_1, n_2],
                        y = y)
    datapoint_list.append(datapoint)
PyG.InMemoryDataset.collate(datapoint_list)
```
Follow the [PyTorch Geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/tutorial/create_dataset.html) for usage of a collation function to create a new dataset. After the dataset is processed multi-graph datapoints can then be batch loaded for model training. 
## Contributing

If you find a bug :bug:, please open a [bug report](https://github.com/kierannp/mData/issues/new?assignees=&labels=bug&template=bug_report.md&title=).
If you have an idea for an improvement or new feature :rocket:, please open a [feature request](https://github.com/kierannp/mData/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).

## Author 
[Kieran Nehil-Puleo](https://kierannp.github.io/)