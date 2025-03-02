s = "{}"

ans = False
stack = []
CloseToOpen = {')':'(', '}':'{', ']':'['}

for i in s:
    if i not in CloseToOpen:
        stack.append(i)
    else:
        if stack and stack[-1]  == CloseToOpen[i]:
            stack.pop()
        else:
            ans = False
if not stack:
    ans = True
else:
    ans = False

print(ans)