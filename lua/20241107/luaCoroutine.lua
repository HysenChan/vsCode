co = coroutine.create(function(a, b, c)
    print("co", a, b, c)
end)

coroutine.resume(co, 1, 2, 3)

co1 = coroutine.create(function(a, b)
    coroutine.yield(a + b, a - b)
end)

print(coroutine.resume(co1, 20, 10))
