shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for k, v in shopping_list.items():
    print(f"Idę do: {k.capitalize()}, kupuję tu następujące rzeczy:", [i.capitalize() for i in v], ".")