"""This module holds classes related to graphs.

This module contains the `Vertex`, `VertexAttributeError`, `Graph`, and `GraphVertexError` classes. `Vertex` represents
a graph vertex. `VertexAttributeError` is an error raised by `Vertex`. `Graph` represents a directed graph.
`GraphVertexError` is an error raised by `Graph`.

Examples:
    Initializing a `Graph` as well as adding colored vertices and edges:

        g = Graph()
        a = Vertex('a', color='red')
        b = Vertex('b', color='blue')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_edge(a, b)

    The following code will raise a `VertexAttributeError` because `'colour'` is not an attribute of the `Vertex` `a`:

        x = a['colour']
"""

from cormen_lib.sets import Set


class VertexAttributeError(Exception):
    """This class is used by `Vertex` to raise errors regarding invalid attributes."""

    def __init__(self, name, wrong_attribute, attributes):
        """Initializes a `VertexAttributeError`.

        Args:
            name: String name of `Vertex` that erroneous attribute is associated with.
            wrong_attribute: String attribute that does not exist in the `Vertex` referred to by `name`.
            attributes: The valid attributes in the `Vertex` referred to by `name` as a `list` of `str`.
        """
        super().__init__(
            f'vertex {name} does not have attribute {wrong_attribute}, available attributes: [{", ".join(a for a in attributes)}]')


class Vertex:
    """Represents a graph vertex.

    A `Vertex` has a name and a collection of customizable attributes. The name should be used to identify it in a
    `Graph`. `Vertex` objects are compared with `==` and via hash code based on their name. The attributes you can use
    in graph algorithms. For example, you could set colors or time steps as in DFS. One should assume all operations
    that can be performed on a `Vertex` are done in `O(1)` time.

    Examples:
        To initialize a `Vertex` with a name:

            v = Vertex('a')

        To initialize a `Vertex` with some starting attributes, use keyword arguments following the name:

            v = Vertex('a', color='red', time=1)

        To add additional attributes to an existing `Vertex` using `[]` with `=`:

            v['seen'] = False

        To update or view existing attributes, use the same idea:

            x = v['color']
            v['time'] = 3

        If you try to get the value of an attribute that does not exist, a `VertexAttributeError` will be raised (e.g.
        calling `print(v['colour'])`. If you try to add a new attribute to an existing `Vertex` where the attribute's
        type is not `str`, a `TypeError` will be raised (e.g. calling `v[1] = 'blue'`).
    """

    def __init__(self, name, **attributes):
        """Initializes a `Vertex`.

        Args:
            name: The name of the `Vertex`. Make sure to read the class docstring above regarding naming of `Vertex`
                  objects.
            **attributes: Optional keyword arguments specifying attributes you want the `Vertex` to start with. See
                          the class docstring above for some possible attributes you could add.
        """
        self.__name = name
        self.__attributes = attributes

    def get_name(self):
        """Returns the name of this `Vertex`."""
        return self.__name

    def __getitem__(self, attribute):
        if attribute not in self.__attributes:
            raise VertexAttributeError(self.__name, attribute, self.__attributes)
        return self.__attributes[attribute]

    def __setitem__(self, attribute, value):
        if attribute not in self.__attributes and not isinstance(attribute, str):
            raise TypeError(f'attribute {attribute} is not of type str, has type {type(attribute)}')
        self.__attributes[attribute] = value

    def __hash__(self):
        return hash(self.__name)

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return other.__name == self.__name

    def __iter__(self):
        # Disables the users' ability to do for a in v for an Vertex v. Without disabling this, the default Python
        # __iter__ will call __getitem__ with an int. We have specified __getitem__ only accepts strings.
        raise RuntimeError(
            'Not allowed to iterate over Vertex like an iterable. Must go through attributes individually with [].')


class GraphVertexError(Exception):
    """This class is used by `Graph` to raise errors regarding invalid vertices."""

    def __init__(self, vertex_name):
        """Initializes a `GraphVertexError` that will be raised associated with a particular `Vertex`.

        Args:
            vertex_name: The string name of the `Vertex` this `GraphVertexError` is being raised in association with.
        """
        super().__init__(f'graph does not have vertex with name {vertex_name}')


class GraphEdgeError(Exception):
    """This class is used by `Graph` to raise errors regarding invalid edges."""

    def __init__(self, source_name, dest_name):
        """Initializes a `GraphEdgeError` that will be raised associated with a particular `Vertex`.

        Args:
            source_name: The string name of the source `Vertex` of the edge this `GraphVertexError` is being raised in
                         association with.
            dest_name: The string name of the destination `Vertex` of the edge this `GraphVertexError` is being raised
                       in association with.
        """
        super().__init__(
            f'graph does not have an edge from a vertex with name {source_name} to a vertex with name {dest_name}')


class Graph:
    """Represents a directed graph.

    A `Graph` represents a directed graph object whose edges can be assigned weights. The `Vertex` objects in the
    `Graph` should have unique names. For more information on this, see the class docstring of `Vertex`.

    Examples:
        To initialize a `Graph`:

            g = Graph()

        In order to add edges to a `Graph`, one must first add the `Vertex` objects that will make up that edge.

            a = Vertex('a')
            b = Vertex('b')
            g.add_vertex(a)
            g.add_vertex(b)

        Now that `a` and `b` have been added to `g`, one can add an edge between them. Note that there is no edge
        object.

            g.add_edge(a, b)

        When adding an edge, one can specify a weight (by default it is `None`):

            g.add_edge(a, b, 1)

        One can get a `cormen_lib.sets.Set` of the adjacent edges of a Vertex:

            s = g.adj(a)
    """

    def __init__(self):
        """Initializes an empty `Graph` in `O(1)` time."""
        self.__adj_lists = dict()
        self.__edge_weights = dict()

    def add_vertex(self, vertex):
        """Adds a `Vertex` to this `Graph`.

        One may assume that this operation runs in `O(1)` time with respect to the number of vertices and edges in this
        `Graph`.

        Args:
            vertex: The `Vertex` to be added to this `Graph`.
        """
        self.__adj_lists[vertex] = list()

    def add_edge(self, source, dest, weight=None):
        """Adds an edge between 2 `Vertex` objects in this `Graph`.

        This creates an edge from the source `Vertex` to the destination `Vertex`. `Graph` is directed so the edge is
        in only one direction. That is, an edge from the destination `Vertex` to the source `Vertex` will not exist. One
        can additionally provide a weight for this edge. One may assume that this operation runs in `O(1)` time with
        respect to the number of vertices and edges in this `Graph`.

        Args:
            source: The source `Vertex`.
            dest: The destination `Vertex`.
            weight: The weight for this edge (floating point, integer). By default this is `None`.

        Raises:
            GraphVertexError: If `source` or `dest` is not in this `Graph`.
        """
        self.__check_edge_vertices(source, dest)
        self.__edge_weights[(source, dest)] = weight
        self.__adj_lists[source].append(dest)

    def adj(self, vertex):
        """Gets the `Vertex` objects that are adjacent to a `Vertex`.

        This gets a `cormen_lib.sets.Set` of the `Vertex` objects that are adjacent to the vertex. Since
        `cormen_lib.sets.Set` objects preserve insertion order (see `cormen_lib.sets.Set` documentation), the
        `cormen_lib.sets.Set` will be ordered according to the order in which edges starting from the input `Vertex`
        were created. One should assume that this method runs in `O(n)` time where `n` is the number of edges going out
        of the input `Vertex`.

        Args:
            vertex: A `Vertex`.

        Returns:
            A `cormen_lib.sets.Set` containing the vertices adjacent to `vertex`.

        Raises:
            GraphVertexError: If `vertex` is not in this `Graph`.

        Examples:
            To illustrate the nature of the `cormen_lib.sets.Set` returned by this method, first set up a `Graph` and
            add some vertices and edges:

                g = Graph()
                a = Vertex('a')
                b = Vertex('b')
                c = Vertex('c')
                g.add_vertex(a)
                g.add_vertex(b)
                g.add_vertex(c)
                g.add_edge(a, b)
                g.add_edge(a, c)

            The `cormen_lib.sets.Set` returned by `g.adj(a)` will always have `b` preceding `c` since the edge from `a`
            to `b` was created before the edge from `a` to `c`.
        """
        if vertex not in self.__adj_lists:
            raise GraphVertexError(vertex.get_name())
        adjacent = Set()
        for u in self.__adj_lists[vertex]:
            adjacent.add(u)
        return adjacent

    def weight(self, source, dest):
        """Gets the weight of an edge defined by two vertices.

        One should assume that this method runs in `O(1)` time with respect to the number of vertices and edges in this
        `Graph`.

        Args:
            source: The source `Vertex` of the edge in question.
            dest: The destination `Vertex` of the edge in question.

        Returns:
            The integer or floating point weight associated with the edge from `source` to `dest`. This will be `None`
            if no weight was specified when the edge was created.

        Raises:
            GraphVertexError: If `source` or `dest` is not in this `Graph`.
            GraphEdgeError: If an edge from `source` to `dest` does not exist.
        """
        self.__check_edge_vertices(source, dest)
        if (source, dest) not in self.__edge_weights:
            raise GraphEdgeError(source, dest)
        return self.__edge_weights[(source, dest)]

    def vertices(self):
        """Gets the vertices in this `Graph`.

        One should assume that this method runs in `O(V)` time where `V` is the number of vertices added to this
        `Graph`.

        Returns:
            A `cormen_lib.sets.Set` containing the `Vertex` objects in this `Graph`. The order of the vertices in this
            `cormen_lib.sets.Set` will always be the order in which the vertices were added to this `Graph` via
            `add_vertex`.
        """
        s = Set()
        for vertex in self.__adj_lists:
            s.add(vertex)
        return s

    def __check_edge_vertices(self, source, dest):
        if source not in self.__adj_lists:
            raise GraphVertexError(source.get_name())
        if dest not in self.__adj_lists:
            raise GraphVertexError(dest.get_name())
