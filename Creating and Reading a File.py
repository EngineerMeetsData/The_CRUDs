
#Creating a text file
file = open(r'C:\\Users\\thessceniza\\Desktop\\CRUD Exercise\\quiz.txt', 'w')
quiz_list1 ='Sampaguita is the National flower of the Philippines.\nThere are 15 regions in the Philippines.\nPhilippines has a total of 7,107 islands.\nBacolod City is known for its Masskara Festival.\nMayon volcano can be found in Sorsogon.\n'
quiz_list2 ='Siargao is the surfing capital of the Philippines.\nBuko pie is the famous delicacy of Cavite.\nBuko pie is the famous delicacy of Cavite.\nLucban in Quezon is famous for its Pahiyas Festival.\nMines View Park is located in Benguet.\nDurian is the famous fruit found in Kidapawan City.'
file.write(quiz_list1)
file.write(quiz_list2)
file.close()

#Reading a text file
file = open(r'C:\\Users\\thessceniza\\Desktop\\CRUD Exercise\\quiz.txt', 'r')
file.readlines()
file.close()

