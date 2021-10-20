#100% mosaic decoration solution
import math

w,h,a,b,m,c = map(int, input().split())

if w%a ==0 and h%b ==0:
    tot_tiles = (w/a)*(h/b)
    crates = math.ceil(tot_tiles/10)
    tot_cost = crates*m

elif h%b ==0:
    wid_tiles = math.ceil(w/a)
    tot_tiles = wid_tiles*(h/b)
    crates = math.ceil(tot_tiles/10)
    cut_len = h
    tot_cost = int(crates * m + cut_len*c)

elif w%a ==0:
    hei_tiles = math.ceil(h/b)
    tot_tiles = hei_tiles*(w/a)
    crates = math.ceil(tot_tiles / 10)
    cut_len = w
    tot_cost = int(crates * m + cut_len * c)

else:
    hei_tiles = math.ceil(h / b)
    wid_tiles = math.ceil(w / a)
    tot_tiles = hei_tiles * wid_tiles
    crates = math.ceil(tot_tiles/10)
    cut_len = w + h
    tot_cost = int(crates * m + cut_len * c)



print(tot_cost)
