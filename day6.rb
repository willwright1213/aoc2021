values = [0,0,0,0,0,0,0,0,0]
File.open('input.txt').read().split(/,/).each { |x| values[x.to_i] += 1 }

(1..255).each do
  temp = values[0]
  (1..8).each { |i| values[i - 1] = values[i] }
  values[8] = temp
  values[7] += values[0]
end

print values.sum
