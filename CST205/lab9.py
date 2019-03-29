def get_sound():
  return makeSound(pickAFile())
  
# start: 30785 - 30790
# end: 58688

def clip(source, start, end):
  length = end - start
  index = 0
  empty_sound = makeEmptySound(length, 44100)
  for i in range(start, end):
    value = getSampleValueAt(source, i)
    setSampleValueAt(empty_sound, index, value)
    index = index + 1
  return empty_sound
    
  
  


def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*0.5)
  writeSoundTo(sound, "C://Developing//School//CST205//decreaseVol.wav")