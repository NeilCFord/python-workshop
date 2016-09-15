def lines
  File.open('./currencyrates.txt').readlines
end

def currency_data
	lines.map {|line| line.delete("\n").split(",")}
end

def print_data
	currency_data.each_with_index do |row, index|
    currency, rate = *row
    puts "#{index} #{currency} #{rate}"
	end
end

print_data