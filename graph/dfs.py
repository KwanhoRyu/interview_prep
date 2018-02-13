###############################
# Depth First Search in Undirectied Graphs
# pros : 
# - 
# 
# cons:
# - 
#
# time complexity : O(|V|+|E|)
# space complexity : O(|V|+|E|)
###############################

class Vertex:
	def __init__ (self, id):
		self.id = id
		self.visited = False
		self.cc = None
		self.start_time = None
		self.end_time = None


class Edge:
	def __init__ (self, start_vertex_id, dest_vertex_id, weight = None):
		self.start_vertex_id = start_vertex_id
		self.dest_vertex_id = dest_vertex_id
		self.weight = weight
		

class Timer:
	def __init__ (self):
		self.timestamp = 1

	def tick(self):
		timestamp = self.timestamp
		self.timestamp += 1
		return timestamp

def dfs (vertices, edges):

	cc = 1
	timer = Timer()

	for vertex in vertices:
		if vertex.visited == False:
			explore(vertex, edges, cc, timer)
			cc += 1

def explore (vertex, edges, cc, timer):

	vertex.visited = True
	vertex.cc = cc
	vertex.start_time = timer.tick()

	for dest_vertex in edges[vertex]:
		if dest_vertex.visited == False:
			explore(dest_vertex, edges, cc, timer)

	vertex.end_time = timer.tick()

	print(vertex.id, vertex.cc, vertex.start_time, vertex.end_time)


def topological_sort (vertices):

	return 



################################################################################################################
# test cases
################################################################################################################

def main():
	testcase_1()
	testcase_2()

def testcase_1():
	print("-- testcase 1 --")
	print("(id, cc, S.T, E.T)")

	vertex_ids = range(0, 8)
	vertices = build_vertices(vertex_ids)

	edges_list = [(1,2), (1,3), (3,4), (4,5)]
	edges = build_edges(vertices, edges_list)

	dfs(vertices, edges)

def testcase_2():
	print("-- testcase 2 --")
	print("(id, cc, S.T, E.T)")

	vertex_ids = range(0, 7)
	vertices = build_vertices(vertex_ids)
	
	edges_list = [ (0,1), (0,2), (1,3), (1,4), (2,5), (2,6) ]
	edges = build_edges(vertices, edges_list)

	dfs(vertices, edges)


def build_vertices(vertex_ids):
	vertices = []

	for vertex_id in vertex_ids:
		vertices.append(Vertex(vertex_id))

	return vertices

def build_edges(vertices, edges_list):
	edges = {}

	for start_vertex in vertices:
		edges[start_vertex] = []

	for start_vertex_id, dest_vertex_id in edges_list:
		for vertex in vertices:
			if vertex.id == start_vertex_id:
				start_vertex = vertex
			if vertex.id == dest_vertex_id:
				dest_vertex = vertex
			
		edges[start_vertex].append(dest_vertex)
		# bidirectional edges -> undirected graphs
		edges[dest_vertex].append(start_vertex)

	return edges 



if __name__ == "__main__":
	main()









