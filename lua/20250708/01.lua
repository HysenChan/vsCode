Set = {}
local mt = {}

function Set.new(l)
    local set = {}
    setmetatable(set, mt)
    for _, v in ipairs(l) do
        set[v] = true
    end
    return set
end

function Set.union(a, b)
    local res = Set.new {}
    for k in pairs(a) do
        res[k] = true
    end
    for k in pairs(b) do
        res[k] = true
    end
    return res
end

function Set.intersection(a, b)
    local res = Set.new {}
    for k in pairs(a) do
        res[k] = b[k]
    end
    return res
end

function Set.tostring(set)
    local l = {}
    for k in pairs(set) do
        l[#l + 1] = k
    end
    return "{" .. table.concat(l, ", ") .. "}"
end

function Set.print(set)
    print(Set.tostring(set))
end

local s1 = Set.new { 1, 2, 3, 4, 5 }
local s2 = Set.new { 4, 5, 6, 7, 8 }
print(getmetatable(s1))
print(getmetatable(s2))

--并集
mt.__add = Set.union
local s3 = s1 + s2
Set.print(s3)
--交集
mt.__mul = Set.intersection
Set.print(s1 * s2)

mt.__tostring = Set.tostring
local s4 = Set.new { 10, 4, 5 }
print(s4)

mt.__metatable = "not your business"

local s5 = Set.new {}
print(getmetatable(s5))
-- setmetatable(s5, {})
