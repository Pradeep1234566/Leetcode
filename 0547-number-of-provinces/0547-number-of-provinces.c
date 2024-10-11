void DFS(int i, int **Adj, int* visited, int isConnectedSize) {
    visited[i] = 1; 
    for (int j = 0; j < isConnectedSize; j++) {
        if (Adj[i][j] == 1 && visited[j] == 0) {
            DFS(j, Adj, visited, isConnectedSize);
        }
    }
}

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    int count = 0;
    int visited[isConnectedSize];
    for (int i=0;i<isConnectedSize;i++)
    {
        visited[i] = 0;
    }
    for(int i=0;i<isConnectedSize;i++)
    {
        if(visited[i]==0)
        {
            count ++;
            DFS(i, isConnected, visited, isConnectedSize);
        }
    }
    return count;
    
}