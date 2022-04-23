import unittest
from dalpy.graphs import Vertex, VertexAttributeError, Graph, GraphVertexError, GraphEdgeError
from dalpy.sets import Set


class VertexTest(unittest.TestCase):
    def test_init(self):
        v = Vertex('a')
        self.assertEqual(v.get_name(), 'a')

    def test_hash(self):
        v = Vertex('a')
        self.assertEqual(hash(v), hash('a'))

    def test_equal(self):
        v = Vertex('a')
        self.assertEqual(v, Vertex('a'))

    def test_attribute(self):
        v = Vertex('a')
        v['color'] = 'blue'
        self.assertEqual(v['color'], 'blue')

    def test_invalid_attribute(self):
        v = Vertex('a')
        self.assertRaises(VertexAttributeError, lambda: v['color'])

    def test_invalid_attribute_type(self):
        v = Vertex('a')

        def invalid_type():
            v[1] = 'blue'

        self.assertRaises(TypeError, lambda: invalid_type())

    def test_init_with_attrs(self):
        v = Vertex('a', color='red', time=1, seen=False)
        self.assertEqual('red', v['color'])
        self.assertEqual(1, v['time'])
        self.assertFalse(v['seen'])


class GraphTest(unittest.TestCase):
    def test_init(self):
        g = Graph()
        v = g.vertices()
        self.assertIsInstance(v, Set)
        self.assertTrue(v.is_empty())

    def test_add_vertex(self):
        g = Graph()
        a = Vertex('a')
        g.add_vertex(a)
        v = g.vertices()
        self.assertIsInstance(v, Set)
        self.assertTrue(a in v)
        self.assertEqual(v.size(), 1)

    def test_color_vertices(self):
        g = Graph()
        names = ['a', 'b', 'c']
        for n in names:
            g.add_vertex(Vertex(n))
        v = g.vertices()
        for vertex in v:
            vertex['color'] = 'red'
        v_new = g.vertices()
        for vertex in v_new:
            self.assertEqual(vertex['color'], 'red')

    def test_add_edge(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_edge(a, b, 0)
        v = g.adj(a)
        self.assertIsInstance(v, Set)
        self.assertTrue(b in v)
        self.assertEqual(v.size(), 1)
        self.assertEqual(g.weight(a, b), 0)

    def test_no_edge(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        g.add_vertex(a)
        g.add_vertex(b)
        self.assertRaises(GraphEdgeError, lambda: g.weight(a, b))
        g.add_edge(a, b)
        self.assertRaises(GraphEdgeError, lambda: g.weight(b, a))

    def test_adj_invalid(self):
        g = Graph()
        a = Vertex('a')
        self.assertRaises(GraphVertexError, lambda: g.adj(a))

    def test_edge_invalid(self):
        a = Vertex('a')
        b = Vertex('b')
        g = Graph()
        self.assertRaises(GraphVertexError, lambda: g.add_edge(a, b, 0))
        g.add_vertex(a)
        self.assertRaises(GraphVertexError, lambda: g.add_edge(a, b, 0))
        g = Graph()
        g.add_vertex(b)
        self.assertRaises(GraphVertexError, lambda: g.add_edge(a, b, 0))

    def test_add_many_edges(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_edge(a, b, 0)
        g.add_edge(a, c, 0)
        v = g.adj(a)
        self.assertEqual(v.size(), 2)
        self.assertTrue(b in v)
        self.assertTrue(c in v)

    def test_unweighted_edge(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        g.add_vertex(a)
        g.add_vertex(b)
        g.add_edge(a, b)
        self.assertIsNone(g.weight(a, b))

    def test_GraphEdgeError(self):
        g = Graph()
        a = Vertex('a')
        b = Vertex('b')
        g.add_vertex(a)
        g.add_vertex(b)
        try:
            g.weight(b, a)
        except GraphEdgeError as e:
            self.assertEqual(e.args[0], "graph does not have an edge from a vertex with name \"b\" to a vertex with name \"a\"")



if __name__ == '__main__':
    unittest.main()
