def on_clicked(icon, item):
    actions = {
        "Astra": Astra,
        "Breach": Breach,
        "Brimstone": Brimstone,
        "Chamber": Chamber,
        "Cypher": Cypher,
        "Harbor": Harbor,
        "Jett": Jett,
        "KAY/O": Kayo,
        "Killjoy": Killjoy,
        "Neon": Neon,
        "Omen": Omen,
        "Phoenix": Phoenix,
        "Raze": Raze,
        "Reyna": Reyna,
        "Sage": Sage,
        "Skye": Skye,
        "Sova": Sova,
        "Viper": Viper,
        "Yoru": Yoru
    }

    item_text = str(item.text)  # Convertir l'élément en texte

    if item_text == "Exit":
        icon.stop()
    else:
        action = actions.get(item_text)
        if action:
            action()
