def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be string")
    result = ""

    for char in text:
        #check for . , ? : 
        if char in [".", ",", "?", ":"]:
            result += char + "\n\n"
        else:
            result += char
    print(result)


  # Example usage:
text = "This is a sample text. It contains some punctuation: like . and ?. What do you think?"
text_indentation(text)  
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres"
text_indentation(text)