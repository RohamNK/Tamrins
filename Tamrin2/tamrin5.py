while True :
    second = int(input("please enter second :"))
    h = int( second / 3600 )
    m = int(( second  -( h * 3600 )) / 60 )
    s = second - (( m * 60 ) + ( h * 3600 ))
    print ("Time:" , h , ":" , m , ":" , s )