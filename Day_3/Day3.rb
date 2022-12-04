
class String
    def halves
        chars.each_slice(size / 2).map(&:join)
    end
    
    def common(other)
        (self.split('') & other.split(''))
    end
end

def file_content(file_path)
    file = File.open(file_path)
    file_data = file.readlines
end

def rank(letter)
    alph_table = {}
    (('a'..'z').zip(1..26)).each { |x| alph_table[x[0]] = x[1]}
    (('A'..'Z').zip(27..52)).each { |x| alph_table[x[0]] = x[1]}
    letter.to_a.collect{ |x| alph_table[x] }
end

def line_score(line)
    first, second = line.halves
    score = rank(first.common(second))
end

class Array
    def compare
        a = self
        while a.size > 1 do
            b = []
            a.combination(2) do |first,second|
                common = first.common(second)
                b << common.join.strip
            end
            a = b.uniq
        end
        a
    end
end

#puts file_content("TestInput.txt")
file_data = file_content("Input.txt")
file_data = file_data
sum = 0
for line in file_data.each do
    first, second = line.halves
    score = rank(first.common(second))
    sum += score[0]
end
puts sum 

file_chunks = file_data.each_slice(3).to_a
scores = file_chunks.collect{|x| rank(x.compare)}

tot = 0
for score in scores.each do
    tot+=score[0]
end
puts tot




