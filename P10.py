def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(thetext)

# ---------------------------------
#  put assignment statements here
# ---------------------------------
    lentext=len(thetext)
    print('lenght for strip is',lentext)
    
    thetext2=thetext.strip()
    lenthetext2=len(thetext2)
    print('new lenght is',lenthetext2)
    print(thetext2)
    
    nothe=thetext2.count('the')
    print('number of thes is',nothe)

    ftl=thetext2.find('little')
    if thetext in thetext2:
        print('Little is found')
    else:
        thetext not in thetext2
        print('Little is not found')

    
    if "titan" in thetext2:
        print('Titan is found')
    else:
        thetext not in thetext2
        print('Titan is not found')

    tp=thetext2.find('appl')
    print('position of appl',tp)

    thetext2=thetext2.replace('Python', 'PYTHON')
    print(thetext2)
      
    return
main()
