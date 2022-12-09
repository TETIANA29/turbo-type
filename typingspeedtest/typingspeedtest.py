from time import time

print('Press Enter to start typing or to break a new line')
print('Press Enter twice to finish typing')
input('---------------------------------------------------')

# record timestamp when user starts typing
start= time()
"""
text=[]
while True:
  line= input()
  if not line:
    break
text.append(line)
"""
text=input()
# record timestamp when user finishes typing 
end=time()

print('-------------------------------------------------')

elapsed_time=(end-start) / 60
#chars_count=sum(len(item) for  item in text)
#words per minute-(wPm)
# no matter what characters user typing every 5 characters is egual to a word
words_count=len(text) /5
wpm = round(words_count /elapsed_time) 
print(f'Your average Words Per Minute (WPM) is {wpm}')

if wpm < 30:
    print(' You shoud practice more technique to improve  your speed')
elif wpm < 40:
    print(' Still below average')
elif wpm < 50:
    print('You are now an average typist.But you still have significant room for improve')
elif wpm < 60:
    print('Conratulations! Nice job')
else:
    print('This is speed required for most jobs.')
 