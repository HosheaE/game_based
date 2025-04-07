input("Type champ name (This wont affect program):")
import random

champions = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
    "Aurelion_Sol", "Aurora", "Azir", "Bard", "Bel_Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
    "Camille", "Cassiopeia", "Cho_Gath", "Corki", "Darius", "Diana", "Dr._Mundo", "Draven", "Ekko", "Elise",
    "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas",
    "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan_IV",
    "Jax", "Jayce", "Jhin", "Jinx", "Kai_Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina",
    "Kayle", "Kayn", "Kennen", "Kha_Zix", "Kindred", "Kled", "Kog_Maw", "K_Sante", "LeBlanc", "Lee_Sin",
    "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master_Yi",
    "Mel_Medarda", "Miss_Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
    "Nilah", "Nocturne", "Nunu___Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana",
    "Quinn", "Rakan", "Rammus", "Rek_Sai", "Rell", "Renata_Glasc", "Renekton", "Rengar", "Riven", "Rumble",
    "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed",
    "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm_Kench",
    "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted_Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel_Koz", "Vex", "Vi", "Viego", "Viktor",
    "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin_Zhao", "Yasuo", "Yone", "Yorick",
    "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra", "Skarner__Reworked", "Smolder"
]

random_champion = random.choice(champions)
print("Random Champion:", random_champion)

input("Press any key to close")