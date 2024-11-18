emails = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']}
for i in emails:
    for j in emails.get(i):
        print(f"{j}@{i}")
