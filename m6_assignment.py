# Project: Modules 6 assignments
# Purpose: Learning about string in Python
# Author: Thanh Bac Vo
# Created: 3/9/2024
# Class: COMP 660 (55408) - SDCCE.

# 1. What function is used to get the ASCII code of a character ?
# Using the ord() function to get the ASCII code of a character
char = "A"
ascii_code = ord(char)
print(f'1. Using the ord() function getting the ASCII code for example: ord("A") is {ascii_code}')

# 2. Take the following Python code that stores a string: str = 'inet addr:127.0.0.1  Mask:255.0.0.0'.
# Use find and string slicing to extract the portion of the string after the colon inet address character
# and then use the rstrip function to remove any trailing characters.

str = 'inet addr:127.0.0.1  Mask:255.0.0.0'
colon_index = str.find(':')
str2 = str[colon_index + 1:]
str3 = str2.rstrip("  Mask:255.0.0.0")
print(f'2. The final string is "{str3}".')

# 3a. Using a for loop through a string, count the number of internet addresses in the string below by
# using the split method.

str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0
inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''
# Use split() to make str to be a list
ip_list = str.split()
# The internet address start with colon mask, We will count the numbers of colon mask at the position 0.
count = 0
for th in ip_list:
    if th[0] == ':' :
        count = count + 1
print(f"3a. Number of IP addresses: {count}")
# choosing a substring to count
substr = 'inet'
# 3b. Use the count() method to return the number of occurrences of the substring in the given string.
print(f'3b. Substring "{substr}" occurrences {str.count(substr)} times')

# 4. Write a Python function to create the HTML string with tags around the word(s).

while True :
    def add_html_tags(tag,words):
        print(f'<{tag}>{words}</{tag}>')
    t = input('4. Enter your tag ("n" to end): ')
    if t == "n":
        break
    tx = input('Enter your text: ')
    add_html_tags(t,tx)

# 5. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

f_name = input('5. What is your first name?(in lowercase letters): ')
l_name = input('What is your last name?(in lowercase letters):')
print(f'Hi {f_name.capitalize()} {l_name.capitalize()}, welcome to my python greet application!')

# 6. Write a program that takes your full name as input and displays the abbreviations of the middle name
# except the first and last name which is displayed as it is.
while True:
    full_name = input('6. Enter your full name("n" to end): ')
    if full_name == "n":
        break
    fn_list = full_name.split()
    fn_list_cap = fn_list
    for cap in range (0,len(fn_list)):
        fn_list_cap[cap] = fn_list[cap].capitalize()
    final_name = fn_list_cap[0]
    if len(fn_list_cap) != 1 :
        for i in range (1, len(fn_list_cap) - 1) :
            st = fn_list_cap[i]
            final_name = final_name + ' ' + st[0] + '.'
        final_name = final_name + ' ' + fn_list_cap[-1]
    print(final_name)




# 7.
famous_list = ''' \
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
Queen Elizabeth II (1926 – 2022) British monarch since 1954
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
Jawaharlal Nehru (1889 – 1964) Indian Prime Minister 1947 – 1964    **
Leonardo da Vinci (1452 – 1519) Italian, painter, scientist, polymath
Vincent Van Gogh (1853 – 1890) Dutch artist
Franklin D. Roosevelt (1882 – 1945) US President 1932 – 1945
Pope John Paul II (1920 – 2005) Polish Pope
Thomas Edison ( 1847 – 1931) American inventor 
Rosa Parks (1913 – 2005)  American civil rights activist
Lyndon Johnson (1908 – 1973) US President 1963 – 1969
Ludwig Beethoven (1770 – 1827) German composer
Oprah Winfrey (1954 – ) American TV presenter, actress, entrepreneur
Indira Gandhi (1917 – 1984) Prime Minister of India 1966 – 1977
Eva Peron (1919 – 1952) First Lady of Argentina 1946 – 1952
Benazir Bhutto (1953 – 2007) Prime Minister of Pakistan 1993 – 1996
George Orwell (1903 – 1950) British author
Vladimir Putin (1952 – ) Russian leader
Dalai Lama (1938 – ) Spiritual and political leader of Tibetans
Walt Disney (1901 – 1966) American film producer
Neil Armstrong (1930 – 2012) US astronaut
Peter Sellers (1925 – 1980) British actor and comedian
Barack Obama (1961 – ) US President 2008 – 2016
Malcolm X (1925 – 1965) American Black nationalist leader
J.K.Rowling (1965 – ) British author
Richard Branson (1950 – ) British entrepreneur
Pele (1940 – ) Brazilian footballer, considered greatest of 20th century.
Angelina Jolie (1975 – ) Actress, director, humanitarian
Jesse Owens (1913 – 1980) US track athlete, 1936 Olympics
John Lennon (1940 – 1980) British musician, member of the Beatles
Henry Ford (1863 – 1947) US Industrialist
Haile Selassie (1892 – 1975) Emperor of Ethiopia 1930 – 1974
Joseph Stalin (1879 – 1953) Leader of Soviet Union 1924 – 1953
Lord Baden Powell (1857 – 1941) British Founder of scout movement
Michael Jordan (1963 – ) US Basketball star
Vladimir Lenin (1870 – 1924) Leader of Russian Revolution 1917
Ingrid Bergman (1915 – 1982) Swedish actress
Fidel Castro (1926 – ) President of Cuba 1976 – 2008
Leo Tolstoy (1828 – 1910) Russian author and philosopher
Greta Thunberg (2003 – ) Environmentalist activist)
Pablo Picasso (1881 – 1973) Spanish modern artist
Oscar Wilde (1854 – 1900) Irish author, poet, playwright
Coco Chanel (1883 – 1971) French fashion designer
Charles de Gaulle (1890 – 1970) French resistance leader and President 1959 – 1969
Amelia Earhart (1897 – 1937) Aviator
John M Keynes (1883 – 1946) British economist
Louis Pasteur (1822 – 1895) French chemist and microbiologist
Mikhail Gorbachev (1931 – ) Leader of Soviet Union 1985 – 1991
Plato (423 BC – 348 BC) Greek philosopher
Adolf Hitler (1889 – 1945) leader of Nazi Germany 1933 – 1945
Sting (1951 – ) British musician
Elon Musk (1971 – ) Business magnate, and entrepreneur.
Mary Magdalene (4 BCE – 40CE) devotee of Jesus Christ
Alfred Hitchcock (1899 – 1980) English / American film producer, director
Michael Jackson (1958 – 2009) American musician
Madonna (1958 – ) American musician, actress, author
Mata Hari (1876 – 1917) Dutch exotic dancer, executed as spy
Cleopatra (69 – 30 BCE) Queen of Egypt
Grace Kelly (1929 – 1982) American actress, Princess of Monaco\
Malala Yousafzai (1997 – ) Pakistani human rights activist
Steve Jobs (1955 – 2012) co-founder of Apple computers
Ronald Reagan (1911 – 2004) US President 1981-1989
Lionel Messi (1987 – ) Argentinian footballer
Babe Ruth (1895 – 1948) American baseball player
Bob Geldof (1951 – ) Irish musician, charity worker
Roger Federer (1981 – ) Swiss Tennis player
Sigmund Freud (1856 – 1939) Austrian psychoanalyst
Woodrow Wilson (1856 – 1924) US president 1913 – 1921
Mao Zedong (1893 – 1976) Leader of Chinese Communist revolution
Katherine Hepburn (1907 – 2003) American actress
Audrey Hepburn (1929 – 1993) British actress and humanitarian
David Beckham (1975 – )  English footballer
Tiger Woods (1975 – ) American golfer
Usain Bolt (1986 – ) Jamaican athlete and Olympian
Carl Lewis (1961 – ) US athlete and Olympian
Prince Charles (1948 – )  Heir to British throne
Jacqueline Kennedy Onassis (1929 – 1994) American wife of JF Kennedy
Joe Biden (1942 – ) US President
Kim Kardashian (1980 – ) American socialiate
C.S. Lewis (1898 – 1963) British author
Billie Holiday (1915 – 1959) American jazz singer
J.R.R. Tolkien (1892 – 1973) British author
Billie Jean King (1943 – ) American tennis player and human rights activist
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
'''
while True:
    natio = input('7. Checking the country has the famous individuals: Enter the nationality ("n" to end): ')
    if natio == "n":
        break
    fam_find = famous_list.find(natio)
    if fam_find != -1:
        fam_list = ['painter', 'scientist', 'president', 'musician', 'author', 'player', 'athlete', 'singer']
        found = 0
        for it in fam_list:
            fam_find_1 = famous_list.find(natio + ' ' + it)
            if fam_find_1 != -1:
                print(f'There is an {natio} {it} in the list')
                found = 1
        if found != 1:
            print(f'There is an {natio} in the list.')
    else: print(f'There is not {natio} in the list.')
# find index of the position of the end of the first line
p = famous_list.find('\n')
l1 = famous_list[:p]
# assignment position of the end of first line
pos = len(l1)
# making a slicing string
l2 = famous_list[pos + 1:]
line_count = 2
while line_count < 21:   # take 20 first lines to find
    # find index of the position of the end of the lines
    p = l2.find('\n')
    # up-data position of the end next line to 20th line
    pos = pos + p + 1
    l2 = famous_list[pos + 1:]
    line_count = line_count + 1
while True :
    famous_individual = input('Please Enter the name of the famous individual to check for top 20("n" to end)? ')
    if famous_individual == "n":
        break
    elif famous_list.find(famous_individual.capitalize(), 0, pos) != -1:
        famous_individual = famous_individual.capitalize()
        famous_name_pos = famous_list.index(famous_individual)
        end_pos = famous_list.find('(', famous_name_pos)
        full_name_famous = famous_list[famous_name_pos : end_pos]
        print(f'Yup, {full_name_famous} did make the Top 20 cut!')
    else:
        print(f'Sorry, {famous_individual} did not make the Top 20 cut!')
