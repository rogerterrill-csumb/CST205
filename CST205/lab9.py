def get_sound():
  return makeSound(pickAFile())

def maxSample(sound):
  max_val = 0
  for sample in getSamples(sound):
    max_val = max(max_val, getSampleValue(sample))
  return max_val
  
def maxVolume(sound):
  largest = maxSample(sound)
  maxPossibleSampleValue = 32767.0
  factor=float(maxPossibleSampleValue)/largest
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  
# Problem 1
def clip(source, start, end):
  length = end - start
  index = 0
  empty_sound = makeEmptySound(length, getSamplingRate(source))
  for i in range(start, end):
    value = getSampleValueAt(source, i)
    setSampleValueAt(empty_sound, index, value)
    index = index + 1
  return empty_sound
    
# Problem 2
def copy(source, target, start):
  source_length = getLength(source)
  for i in range(source_length-1):
    value = getSampleValueAt(source, i)
    setSampleValueAt(target, start, value)
    start = start + 1
  return start
    
# Problem 3
def silence(duration):
  sample_rate = 44100
  length = int(duration * sample_rate)
  silence_sound = makeEmptySound(length, sample_rate) 
  for i in range(length):
    setSampleValueAt(silence_sound, i, 0)
  return silence_sound

def sound_collage():
  setMediaPath()
  sound_list = []
  num_of_songs = 5
  length = 0
  index = 0
  silence_sound = silence(input("How long would you like the silence between files to be?"))
  
  for i in range(num_of_songs):
    sound_list.append(get_sound())
    
  for sound in sound_list:
    length = length + getLength(sound) + getLength(silence_sound)
  target = makeEmptySound(length, 44100)

  for song in sound_list:
    index = copy(song, target, index)
    index = copy(silence_sound,target,index)
  writeSoundTo(target, getMediaPath() + 'sound_collage.wav')
  return target

# Problem 4
def reverse(sound):
  length = getLength(sound)
  sample_rate = int(getSamplingRate(sound))
  print sample_rate
  index = 0
  reverse_sound = makeEmptySound(length, sample_rate)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValueAt(reverse_sound, length - index - 1, value)
    index = index + 1
  return reverse_sound
    
  


