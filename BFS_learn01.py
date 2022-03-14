""""
Breadth-first search is a hierarchical search process, not a recursive algorithm. In order to achieve layer-by-layer access, the algorithm must use an auxiliary queue to remember the vertices of the next layer of the vertex being accessed.

"""
bool visited[MAX_VERTEX_NUM]; #access tag array
void BFSTraverse(Graph G){
  for (i = 0; i < G.vexnum; ++i)
    visited[i] = False;
  InitQueue(Q);
  for (i = 0; i < G.vexnum; ++i)
    if (! visited[i])
      BFS(G, i);
}
void BFS(GRAPH G, int v){
  visit(v);
  visited[v]=True;
  Enqueue(Q, v);
  while(! isEmpty(Q)){
    DeQueue(Q, v);
    for (w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w))
      if(!visited[w]){
        visited(w);
        visited[w] = True;
        EnQueue(Q, w);
      }
  }
}
