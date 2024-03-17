#define two set
setE={0,2,4,6,8}
setN={1,2,3,4,5}
#using union() method
union_set_method=setE.union(setN)
print("unoin using union()method:",union_set_method)
#using intersection()method
intersection_set_method=setE.intersection(setN)
print("intersection using intersection method:",intersection_set_method)

#using difference method
difference_set_method=setE.difference(setN)
print("difference using difference method:",difference_set_method)


#using symmetric difference method
symmetric_difference_set_method=setE.symmetric_difference(setN)
print("symmetric difference using symmetric method:",symmetric_difference_set_method)