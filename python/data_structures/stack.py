browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)
last = browsing_session.pop()

print(last)
print(browsing_session)

browsing_session[-1]
print("redirect ", browsing_session)

if not browsing_session:
    print("disable")
"""pop to get the element on top of the stack 
    append to add to the stack 
    index of -1 to the the last element on the stack 
"""