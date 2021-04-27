def knight(p1, p2):
    p1, p2 = [ord(k) - 96 if k.isalpha() else int(k) for k in p1.replace("", " ")[1:-1].split()], [ord(k) - 96 if k.isalpha() else int(k) for k in p2.replace("", " ")[1:-1].split()]
        
    kx = [2, 2, -2, -2, 1, 1, -1, -1]
    ky = [1, -1, 1, -1, 2, -2, 2, -2]
    
    queue = []
    queue.append([p1[0], p1[1], 0])
    
    visited = [[False for i in range(8 + 1)] for j in range(8 + 1)]
    visited[p1[0]][p1[1]] = True
    
    while(len(queue) > 0):
    
        cell = queue[0]
        queue.pop(0)
        
        if (cell[0] == p2[0] and cell[1] == p2[1]):
            return cell[2]
        
        for i in range(8):
            x = cell[0] + kx[i]
            y = cell[1] + ky[i]
            
            if (x >= 1 and x <= 8 and y >= 1 and y <= 8 and not visited[x][y]):
                visited[x][y] = True
                queue.append([x, y, cell[2] + 1])