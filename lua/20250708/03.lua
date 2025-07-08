t = {}

local _t = t

t = {}

local mt = {
    __index = function(t, k)
        print("*access to element " .. tostring(k))
        return _t[k]
    end,
    __newindex = function(t, k, v)
        print("*update of element " .. tostring(k) .. " to " .. tostring(v))
        _t[k] = v
    end
}
setmetatable(t, mt)
t[2] = "hello"
print(t[2])

local index = {}

local mt1 = {
    __index = function(t, k)
        print("*access to element " .. tostring(k))
        return t[index][k]
    end,
    __newindex = function(t, k, v)
        print("*update of element " .. tostring(k) .. " to " .. tostring(v))
        t[index][k] = v
    end
}

function track(t)
    local proxy  = {}
    proxy[index] = t
    setmetatable(proxy, mt1)
    return proxy
end

function readOnly(t)
    local proxy = {}
    local mt = {
        __index = t,
        __newindex = function(t, k, v)
            error("attempt to update a read-only table", 2)
        end
    }
    setmetatable(proxy, mt)
    return proxy
end

days = readOnly({ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" })
print(days[1])
days[2] = "Noday"
