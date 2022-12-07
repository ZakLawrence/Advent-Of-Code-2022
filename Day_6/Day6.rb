def file_content(file_path)
    file = File.open(file_path)
    file_data = file.readlines
end

def signal_search(file_path,window)
    file_data = file_content(file_path)
    for line in file_data.each do
        chars = line.split('')
        for char,index in chars.each_with_index do
            #puts char, index
            if chars[index...index+window].uniq.length == window
                #puts chars[index...index+4]
                puts index+14
                break
            end
        end

    end
end

signal_search("Input.txt",14)