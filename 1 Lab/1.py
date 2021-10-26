input_file = open("aplusb.in")
a, b = map(int, input_file.readline().split())
output_file = open('aplusg.out', 'w')
output_file.write(str(a + b))
