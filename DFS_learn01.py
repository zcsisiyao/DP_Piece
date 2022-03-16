bool visited[Max_vertex_num];
void DFSTraverse(Graph G){
  for (v = 0; v < G.vexnum; ++v)
    visited[v] = False;
  for (v = 0; v < G.vexnum; ++v)
    if(!visited[v])
      DFS(G, v);
}
void DFS(Graph G, int v){
  visited(v);
  visited[v] = True;
  for (w = FirstNeighbor(G, v); w >= 0; w = Neighbor(G, v, w))
    if(!visited[w]){
      DFS(G, w);
    }
    }
