
pairs = { "(": ")", "[": "]", "{": "}" }

def allBrackets( s, length, stack = None ):
   if stack == None:
      stack = []
   if len(s) == length:
     if not stack: print(s)
     return
   if stack:
     lastOpen = stack[-1]
     allBrackets( s + pairs[lastOpen], length, stack[:-1] )
   for b in pairs:
     allBrackets( s + b, length, stack + [b] )

LENGTH = 4
allBrackets( "", LENGTH )