print("I am abc")

--（%取模操作符）
a=10
b=3
print(a%b)

c=3.141592653
print(c%1)--c的小数部分 0.141592653
print(c%0.1)--精确到小数点后1位结果 0.041592653
print(c-c%0.1)--精确到小数点后1位结果 3.1

d=3.1
print(d%3)--0.1
print(d%-3)---2.9

--（^指数操作符）
e=9
print(e^3)--立方
print(e^0.5)--开平方
print(e^(-0.5))--开平方根的倒数

print("string")

local s1="(wo neng suo sha)"
print(string.gsub(s1,"%)", "A"))

local s2="FGHJKL%yuio"
print(string.gsub(s2,"%%","B"))

names={"Peter","Paul","Mary"}
grades={Mary=10,Paul=7,Peter=8}
function sortByGrades(names, grades)
	table.sort( names,function(n1,n2)
		return grades[n1]>grades[n2]
	end )
end

print(names[1],names[2],names[3])
sortByGrades(names,grades)
print(names[1],names[2],names[3])