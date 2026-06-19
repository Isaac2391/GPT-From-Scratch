

with open("./GPT-From-Scratch/australia_dataset_final (1).txt", "r", encoding='utf-8') as file:
    dataset = file.read()

print(dataset[:1000])

datasetLength = len(dataset)

print(f"The dataset is {datasetLength} characters long") # ~10 milion characters long

vocabulary = sorted(list(set(dataset)))
vocabularyFormatted = " ".join(vocabulary)
vocabularySize = len(vocabulary)

print(f"The vocabulary is: {vocabularyFormatted}") 

"""
 ! # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < > ? @ A B C D E F G H I 
 J K L M N O P Q R S T U V W X Y Z [ \ ] _ a b c d e f g h i j k l m n o p q r s t u v w x y z 
 { | ¢ £ § © ® ° ² ³ ¶ · º ¼ ½ ¾ à â ä é ‑ – — • … ′ ″ − ❑ ⦁
 """

print(f"The vovbulary size is {vocabularySize}") # 118 