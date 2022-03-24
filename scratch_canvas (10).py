s1 = int(input('Enter the first side of triangle'))
s2 = int(input('Enter the second side of triangle'))
s3 = int(input('Enter the third side of triangle'))
if s1 == s2 and s2 == s3:
    print('Equilateral triangle')
elif(s1==s2 and s2==s3)==(s2==s3 and s2==s1)==(s1==s3==s1==s2):
    print("Isosceles triangle")
elif s1==s2 and s1==s3 == s2==s3:
    print("Scalene triangle")
