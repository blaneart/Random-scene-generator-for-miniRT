import random

def ft_random_coor(f):
    f.write(str(random.randrange(-100,100,1)))
    f.write(',' + str(random.randrange(-100,100,1)))
    f.write(',' + str(random.randrange(-100,100,1)) + ' ')

def ft_random_color(f):
    f.write(str(random.randrange(0,255, 1)) + ',')
    f.write(str(random.randrange(0,255, 1)) + ',')
    f.write(str(random.randrange(0,255, 1)) + ' ')

def ft_random_norm(f):
    f.write(str(round(random.uniform(-1, 1), 3)) + ',')
    f.write(str(round(random.uniform(-1, 1), 3)) + ',')
    f.write(str(round(random.uniform(-1, 1), 3)) + ' ')

def ft_gen_sp(f):
    f.write("sp ")
    ft_random_coor(f)
    f.write(str(random.randrange(1, 10, 1)) + ' ')
    ft_random_color(f)
    f.write('\n')

def ft_gen_tr(f):
    f.write('tr ')
    ft_random_coor(f)
    ft_random_coor(f)
    ft_random_coor(f)
    ft_random_norm(f)
    ft_random_color(f)
    f.write('\n')

def ft_gen_sq(f):
    f.write('sq ')
    ft_random_coor(f)
    ft_random_norm(f)
    f.write(str(random.randrange(1, 10, 1)))
    ft_random_color(f)
    f.write('\n')

def ft_gen_pl(f):
    f.write('pl ')
    ft_random_coor(f)
    ft_random_norm(f)
    ft_random_color(f)
    f.write('\n')

def ft_gen_cy(f):
    f.write('cy ')
    ft_random_coor(f)
    ft_random_norm(f)
    f.write(str(random.randrange(1, 10, 1)))
    f.write(str(random.randrange(1, 10, 1)))
    ft_random_color(f)
    f.write('\n')

def ft_write():
    my_list = [ft_gen_cy, ft_gen_pl, ft_gen_sp, ft_gen_sq, ft_gen_tr]
    f = open("i.rt", "w+")
    f.write("R 1800 1200\n")
    f.write("A 0.2 255,255,255\n")
    f.write("c 0,0,-10 0,0,1 70\n")
    f.write("c 0,0,10 0,0,-1 70\n")
    f.write("c 10,-10,0 0.6,-0.8,0 70\n")
    f.write("c -10,10,0 -0.8,0.6,0 70\n")
    for i in range(10):
        random.choice(my_list)(f)
    print("done")

def main():
    ft_write()

if __name__ == '__main__':
    main()




