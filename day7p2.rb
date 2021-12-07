# max is 1927 min is 0
numbers = Array.new

File.open("input.txt").read().split(',').each { |n| numbers.push(n.to_i) }

ans = 0

(0..1927).each do |i|
  sum = 0
  numbers.each do |j|
    sum += ((i-j).abs.pow(2) + (i-j).abs)/2
  end
  if sum < ans || ans == 0
    ans = sum
  end
end

p ans
