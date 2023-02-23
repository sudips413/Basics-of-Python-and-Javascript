# Specify that wide columns have a suffix containing words
the_code_long = pd.wide_to_long(books_brown, 
                                stubnames=['language', 'publisher'], 
                                i=['author', 'title'], 
                                j='code', 
                                sep='_', 
                                suffix='\w+')

# Print the_code_long
print(the_code_long)