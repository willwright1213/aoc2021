

map = Array.new(100) { Array.new(100) { '.' } }


def foldit(points, direction, position)
    fold = nil
    if direction == 'x'
        fold = [position, 0]
    else
        fold = [0, position]
    end
    points.each_index { |i|
        unless points[i].nil?
            unless (points[i][0] - fold[0]) < 0 || (points[i][1] - fold[1]) < 0
                xdiff = (fold[0] - (points[i][0] - fold[0])).abs
                ydiff = (fold[1] - (points[i][1] - fold[1])).abs
                unless points.include?([xdiff, ydiff])
                    points[i] = [xdiff, ydiff]
                else
                    points[i] = nil
                end
            end
        end
    }
end


points = Array.new
File.readlines("input.txt", chomp: true).each { |line|
    unless line[0].nil?
        if line[0].ord <= 57 #if it's a numnber
            points.append(line.split(",").map(&:to_i).to_a)
        end
    end
}



foldit(points, 'x', 655)
foldit(points, 'y', 447)
foldit(points, 'x', 327)
foldit(points, 'y', 223)
foldit(points, 'x', 163)
foldit(points, 'y', 111)
foldit(points, 'x', 81)
foldit(points, 'y', 55)
foldit(points, 'x', 40)
foldit(points, 'y', 27)
foldit(points, 'y', 13)
foldit(points, 'y', 6)


points.compact().each { |p|
    map[p[1]][p[0]] = '#'
}
map.each { |m|
    m.each { |c|
        print c
    }
    print "\n"
}

print map[0][1]
