from replacers import RegexpReplacer, RepeatReplacer, WordReplacer, CsvWordReplacer

# contraction
replacer = RegexpReplacer()
print(replacer.replace("can't is a contraction"))
print(replacer.replace("I should't done that thing I didn't do"))

# repeat letters
replacer = RepeatReplacer()
print(replacer.replace('looooove'))
print(replacer.replace('oooooh'))
print(replacer.replace('goose'))

# synonyms
replacer = WordReplacer({'bday': 'birthday'})
print(replacer.replace('bday'))
print(replacer.replace('happy'))

replacer = CsvWordReplacer('syn.csv')
print(replacer.replace('bday'))
print(replacer.replace('NLP'))
print(replacer.replace('happy'))
