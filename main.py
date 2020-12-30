import screen

#paste your files that are stored in the folder \data\<emotion>
File_names = ['7_kupina_valeria.mp4', '10_volokhova_elena.mp4', '11_klok_nikita.mp4', '12_sokolova_maria.mp4',
              '13_volokhov_alexandr.mp4']
#six emotions
Emotions = ['angry', 'disgusting', 'happy', 'neutral', 'sad', 'scared']
for i in range(len(Emotions)):
    for j in range(len(File_names)):
        file_name = File_names[j]
        #person_name helps to make images
        person_name = file_name[file_name.rfind("\\")+1:len(file_name)-4]
        emotion = Emotions[i]
        screen.screenshots(person_name, emotion)


