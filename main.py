import random

def csquare(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
# print(csquare(255, 0, 0, "■"))

def write_words():
  w = open("words.txt")
  z = open("wordlist.txt", 'w')
  for x in w:
    word = x.strip().replace("é","e")
    if len(word) == 5 and word[0].lower() == word[0] and (not "'" in word):
      z.write(word + "\n")

  w.close()
  z.close()


f = open("wordlist.txt")
all_words = [x.strip() for x in list(f)]
word = random.choice(all_words).strip()
guess = ""
number_guesses = 0
letters_used = {}
while guess != word:
  guess = input("Guess? ")
  if len(guess) == 5:
    if guess in all_words:
      number_guesses += 1
      color_string = ""

      w = list(word)
      word_dict = {}
      for let in word:
        if let in word_dict:
          word_dict[let] += 1
        else:
          word_dict[let] = 1
      
      guess_dict = {}
      for let in guess:
        if let not in letters_used:
          letters_used[let] = 'grey'
        if let in guess_dict:
          guess_dict[let] += 1
        else:
          guess_dict[let] = 1
      
      index = 0
      green_list = []
      for let in guess:
        if let in w:
          if let == w[index]:
            green_list.append(let)
        index += 1

      index = 0
      for let in guess:
        if let in w:
          if let == w[index]:
            color_string += csquare(00, 255, 00, "■")
            letters_used[let] = 'green'
            w[index] = "."
          else:
            # https://www.reddit.com/r/wordle/comments/ry49ne/illustration_of_what_happens_when_your_guess_has/
            if word_dict[let] == 0:
              color_string += csquare(128, 128, 128, "■")
              letters_used[let] = 'grey'
            else:
              if word_dict[let] >= guess_dict[let]:
                color_string += csquare(128, 128, 00, "■")
                letters_used[let] = 'yellow'
              elif word_dict[let] < guess_dict[let] and let not in green_list:
                color_string += csquare(128, 128, 00, "■")
                letters_used[let] = 'yellow'
              else:
                color_string += csquare(128, 128, 128, "■")
                letters_used[let] = 'grey'
        else:
          color_string += csquare(128, 128, 128, "■")
          letters_used[let] = 'grey'
        index += 1
        if let in word_dict:
          word_dict[let] -= 1
      print(color_string)
      print("Letters used: ")
      l = []
      for k in sorted(letters_used.keys()):
        if letters_used[k] == 'grey':
          l.append(csquare(128, 128, 128, k))
        elif letters_used[k] == 'yellow':
          l.append(csquare(128, 128, 00, k))
        else:
          l.append(csquare(00, 255, 00, k))
      for x in l:
        print(x)

    else:
      print("Not a word")
  else:
    print("Too short/long")
print(number_guesses)


f.close()










