string = str(input("enter the input:"))
char= str(input("to chck"))
freq = [None] * len(string);
minChar = string[0];
maxChar = string[0];

# Count each word in given string and store in array freq
for i in range(0, len(string)):
    freq[i] = 1;
    for j in range(i + 1, len(string)):
        if (string[i] == string[j] and string[i] != ' ' and string[i] != '0'):
            freq[i] = freq[i] + 1;

            # Set string[j] to 0 to avoid printing visited character
            string = string[: j] + '0' + string[j + 1:];

        # Determine minimum and maximum occurring characters
min = max = freq[0];
for i in range(0, len(freq)):
#finding the max occurence of a char
    if max < freq[i]:
        max = freq[i]
        maxChar = string[i]

print("Maximum occurring character: " + maxChar);
http://i.imgflip.com/1bij.jpg
componentDidMount() {
        fetch("https://api.imgflip.com/get_memes")
            .then(response => response.json())
            .then(response => {
                const {memes} = response.data
                console.log(memes[0])
                this.setState({ allMemeImgs: memes })
            })