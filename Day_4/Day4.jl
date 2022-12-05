
function read_file(fpath)
    file = open(fpath,"r")
    line_pairs = []
    for line in readlines(file)
        first,second = split(line,",")
        first_low,first_high = split(first,"-")
        second_low,second_high = split(second,"-")
        push!(line_pairs, (collect(parse(Int,first_low):parse(Int,first_high)),collect(parse(Int,second_low):parse(Int,second_high))))
    end
    close(file)
    return line_pairs
end

function check_range(list)
    arrsubset(A,B) = issubset(Set(A),Set(B))
    arrintersect(A,B) = intersect(Set(A),Set(B))
    subsets = 0 
    intersects = 0 
    for set in list
        set1 = set[1]
        set2 = set[2]
        if ( arrsubset(set1,set2) || arrsubset(set2,set1) ) 
            subsets+=1
        end
        if (length(arrintersect(set1,set2)) > 0)
            intersects +=1
        end
    end
    return subsets, intersects
end


line_pairs = read_file("Inputs.txt")
println(check_range(line_pairs))


