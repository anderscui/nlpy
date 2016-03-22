import enchant

from replacers import SpellingReplacer

replacer = SpellingReplacer()
print(replacer.replace('cookbok'))

# enchant
print(enchant.list_languages())
