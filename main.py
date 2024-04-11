def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        def sort_on(dict):
            return dict["num"]
        file_contents = f.read()
        words = file_contents.split()
        words_dict = {}
        file_contents = file_contents.lower()
        for char in file_contents:
            if char not in words_dict:
                words_dict[char] = 1
            else:
                words_dict[char] += 1


        words_report = []
        for word in words_dict:
            if word.isalpha():
                words_report.append({"word": word, "num": words_dict[word]})
        words_report.sort(reverse=True, key=sort_on)
        print(len(words))
        print(words_dict)
        print(f'--- Begin report of {filename} ---')
        print(f'{len(words)} words found in the document')
        for word in words_report:
            print(f'The letter {word["word"]} was found {word["num"]} times')


main()
