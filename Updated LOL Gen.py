input("Press enter")
import random

champions = [
    "Aatrox", "Ambessa", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion_Sol", "Aurora", "Azir", "Bard", "Bel_Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Cho_Gath", "Corki", "Darius", "Diana", "Dr._Mundo", "Draven", "Ekko", "Elise",
    "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas",
    "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan_IV",
    "Jax", "Jayce", "Jhin", "Jinx", "Kai_Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina",
    "Kayle", "Kayn", "Kennen", "Kha_Zix", "Kindred", "Kled", "Kog_Maw", "K_Sante", "LeBlanc", "Lee_Sin",
    "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master_Yi",
    "Mel_Medarda", "Milio", "Miss_Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
    "Nilah", "Nocturne", "Nunu_Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana",
    "Quinn", "Rakan", "Rammus", "Rek_Sai", "Rell", "Renata_Glasc", "Renekton", "Rengar", "Riven", "Rumble",
    "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed",
    "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm_Kench",
    "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted_Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel_Koz", "Vex", "Vi", "Viego", "Viktor",
    "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin_Zhao", "Yasuo", "Yone", "Yorick",
    "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]
exclude = [
    "Master_Yi", "Aurora", "Yasuo", "Vex", "Ambessa", "Nunu_Willump", "Anivia", "Lillia", "Fiora", "Vel_Koz", "Quinn", "Hecarim", "Smolder", "Elise", "Zilean",
    "K_Sante", "Qiyana", "Zac", "Skarner", "Ivern", "Brand", "Hwei", "Bel_Veth", "Nilah", "Lucian", "Taric", "Nidalee", "Graves", "Rek_Sai", "Akshan", "Veigar",
    "Xin_Zhao", "Ezreal", "Kog_Maw", "Azir", "Morgana", "Nami", "Shyvana", "Viktor", "Neeko", "Kayn", "Kindred", "Sejuani", "Kai_Sa", "Diana", "Ziggs", "Vladimir",
    "Sett", "Tryndamere", "Malzahar", "Braum", "Aurelion_Sol", "Karma", "Mel_Medarda", "Samira", "Cho_Gath", "Rammus", "Ekko", "Janna", "Milio", "Vi", "Camille", "LeBlanc",
    "Heimerdinger", "Zoe", "Urgot", "Thresh", "Senna", "Nasus", "Blitzcrank", "Kennen", "Mordekaiser", "Pyke", "Nocturne", "Rumble", "Rakan", "Sivir", "Xayah", "Gangplank"
]  

available_champs = [ch for ch in champions if ch not in exclude]

if available_champs:
    random_champs = random.choice(available_champs)
    print("Random Champion:", random_champs)

input("Press enter to close")