--节点类定义
local Node = {}
function Node:new(x, y)
    local obj = {
        x = x,       --横坐标
        y = y,       --纵坐标
        g = 0,       --起点到当前节点的实际代价
        h = 0,       --当前节点到终点的预估代价
        f = 0,       --总代价(f=g+h)
        parent = nil --父节点
    }
    setmetatable(obj, self)
    self.__index = self
    return obj
end

--地图配置(0=可通行，1=障碍)
local map = {
    { 0, 0, 0, 0, 0 },
    { 0, 1, 1, 0, 0 },
    { 0, 1, 0, 0, 0 },
    { 0, 1, 1, 1, 0 },
    { 0, 0, 0, 0, 0 },
}

--曼哈顿距离计算
local function manhattanDistance(a, b)
    return math.abs(a.x - b.x) + math.abs(a.y - b.y)
end

--获取相邻节点
local function getNeighbors(current, endNode)
    local dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } } --四方向移动
    local neighbors = {}

    for _, dir in ipairs(dirs) do
        local x = current.x + dir[1]
        local y = current.y + dir[2]

        --检查边界和障碍
        if x >= 1 and x <= #map and y >= 1 and y <= #map[1] then
            if map[x][y] == 0 then
                local node = Node:new(x, y)
                node.parent = current
                node.g = current.g + 1 --移动代价为1
                node.h = manhattanDistance(node, endNode)
                node.f = node.g + node.h
                table.insert(neighbors, node)
            end
        end
    end
    return neighbors
end

--主寻路函数
function aStar(startX, startY, endX, endY)
    local openList = {}
    local closeList = {}

    local startNode = Node:new(startX, startY)
    local endNode = Node:new(endX, endY)

    table.insert(openList, startNode)

    while #openList > 0 do
        --寻找F值最小的节点
        local currentIndex = 1
        for i = 1, #openList do
            if openList[i].f < openList[currentIndex].f then
                currentIndex = i
            end
        end

        local current = table.remove(openList, currentIndex)
        table.insert(closeList, current)

        --找到终点
        if current.x == endNode.x and current.y == endNode.y then
            local path = {}
            while current do
                table.insert(path, 1, { x = current.x, y = current.y })
                current = current.parent
            end
            return path
        end

        --处理相邻节点
        local neighbors = getNeighbors(current, endNode)
        for _, neighbor in ipairs(neighbors) do
            local inClose = false
            for _, node in ipairs(closeList) do
                if node.x == neighbor.x and node.y == neighbor.y then
                    inClose = true
                    break
                end
            end
            if not inClose then
                --检查开放列表
                local inOpen = false
                for _, node in ipairs(openList) do
                    if node.x == neighbor.x and node.y == neighbor.y then
                        inOpen = true
                        --如果新路径更优则更新
                        if neighbor.g < node.g then
                            node.g = neighbor.g
                            node.f = node.g + node.h
                            node.parent = current
                        end
                        break
                    end
                end
                if not inOpen then
                    table.insert(openList, neighbor)
                end
            end
        end
    end

    return nil --未找到路径
end

local path = aStar(1, 1, 3, 4)
if path then
    print("can find")
    for _, pos in ipairs(path) do
        print("(" .. pos.x .. "," .. pos.y .. ")")
    end
else
    print("can't find")
end
