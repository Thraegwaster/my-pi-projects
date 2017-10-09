program sum	!a: name of program
!An example of program structure
real :: answer,x,y
print *, 'Enter two numbers'
read *, x
read *, y
answer=x+y
print *, 'The total is ', answer
end program sum
