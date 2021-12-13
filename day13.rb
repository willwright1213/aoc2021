

map = Array.new(50) { Array.new(200) { '.' } }

def foldit(points, direction, position)
    fold = [0, 0]
    if direction == 'x'
        fold[0] = position
    else
        fold[1] = position
    end
    points.each_index { |i|
        unless points[i][0] - fold[0] < 0 || points[i][1] - fold[1] < 0
            xdiff = (fold[0] - (points[i][0] - fold[0])).abs
            ydiff = (fold[1] - (points[i][1] - fold[1])).abs
            points[i] = [xdiff, ydiff]
        end
    }
end


points = Array.new
File.readlines("input.txt", chomp: true).each { |line|
    unless line[0].nil?
        if line[0].ord <= 57 #if it's a numnber
            points.append(line.split(",").map(&:to_i))
        end
        if line[0] == 'x'
            foldit(points, 'x', line.split('=')[1].to_i)
        elsif line[0] == 'y'
            foldit(points, 'y', line.split('=')[1].to_i)
        end
    end
}




points.each { |p|
    map[p[1]][p[0]] = '#'
}
map.each { |m|
    m.each { |c|
        print c
    }
    print "\n"
}

print map[0][1]
