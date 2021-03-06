import random

def ft_random_coor(f):
    f.write(str(random.randrange(-20, 20, 1)))
    f.write(',' + str(random.randrange(-20, 20, 1)))
    f.write(',' + str(random.randrange(-20, 20, 1)) + ' ')

def ft_random_color(f):
    f.write(str(random.randrange(0, 255, 1)) + ',')
    f.write(str(random.randrange(0, 255, 1)) + ',')
    f.write(str(random.randrange(0, 255, 1)) + ' ')

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
def ft_add_light(f):
    f.write('l ')
    ft_random_coor(f)
    f.write(' ' + str(round(random.uniform(0, 1), 3)))
    f.write(' ' + '255,255,255\n')
def ft_write():
    my_list = [ft_gen_cy, ft_gen_pl, ft_gen_sp, ft_gen_sq, ft_gen_tr]
    f = open("i.rt", "w+")
    f.write("R 1800 1200\n")
    f.write("A 0.4 255,255,255\n")
    f.write("c 0,0,-25 0,0,1 70\n")
    f.write("c 0,0,25 0,0,-1 70\n")
    f.write("c 25,0,0 -1,0,0 70\n")
    f.write("c -25,0,0 1,0,0 70\n")
    f.write("c 25,25,0 -1,-1,0 70\n")
    f.write("c -25,-25,0 1,1,0 70\n")
    for i in range(5):
        ft_add_light(f)
    for i in range(10):
        random.choice(my_list)(f)
    print("done")

def main():
    ft_write()

if __name__ == '__main__':
    main()




