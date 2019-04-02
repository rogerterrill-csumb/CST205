def get_sound():
  return makeSound(pickAFile())


def increaseVolume(sound):
  setMediaPath()
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*2)
  writeSoundTo(sound, getMediaPath() + 'increaseVol.wav')

def decreaseVolume(sound):
  setMediaPath()
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*0.5)
  writeSoundTo(sound, getMediaPath() + 'decreaseVol.wav')
  
def changeVolume(sound, factor):
  setMediaPath()
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  writeSoundTo(sound, getMediaPath() + 'changeVol.wav')
  
def maxSample(sound):
  max_val = 0
  for sample in getSamples(sound):
    max_val = max(max_val, getSampleValue(sample))
  return max_val
    
def maxVolume(sound):
  setMediaPath()
  largest = maxSample(sound)
  maxPossibleSampleValue = 32767.0
  factor=float(maxPossibleSampleValue)/largest
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  writeSoundTo(sound, getMediaPath() + 'maxVol.wav')
  
def goToEleven(sound):
  setMediaPath()
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
  writeSoundTo(sound, getMediaPath() + 'goToEleven.wav')

