def get_sound():
  return makeSound(pickAFile())


def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*2)
  writeSoundTo(sound, "C://Developing//School//CST205//increaseVol.wav")
    
# Before 10730: 97, 20350: -33
# After  10730: -62, 20350: -66

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*0.5)
  writeSoundTo(sound, "C://Developing//School//CST205//decreaseVol.wav")
  
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  writeSoundTo(sound, "C://Developing//School//CST205//decreaseVol.wav")
  
def maxSample(sound):
  max_val = 0
  for sample in getSamples(sound):
    max_val = max(max_val, getSampleValue(sample))
  return max_val
    
def isValue(sound, value):
  max_val = 0
  for sample in getSamples(sound):
    if value == getSampleValue(sample):
      print sample

def maxVolume(sound):
  largest = maxSample(sound)
  maxPossibleSampleValue = 32767.0
  factor=float(maxPossibleSampleValue)/largest
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  writeSoundTo(sound, "C://Developing//School//CST205//maxVolume.wav")
  
# 44409:-6663
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
  writeSoundTo(sound, "C://Developing//School//CST205//goToEleven.wav")

